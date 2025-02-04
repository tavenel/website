---
title: TP - Affichage de la configuration du système et des périphériques et modules noyau
date: 2024 / 2025
correction: false
---

## Fichiers de logs et messages du noyau

### Généralités

Le répertoire `/var/log` est un répertoire important pour la gestion des journaux (logs) des systèmes d'exploitation Unix et Linux. Ce répertoire est utilisé pour stocker les journaux générés par divers composants du système, tels que le noyau, les services système, les applications, les serveurs web, les bases de données, ...

Les fichiers de logs sont traditionnellement des fichiers au format texte standard mais certains systèmes de logs (comme `journalctl` dans les distributions `systemd`, très présent aujourd'hui) sont au format binaire et nécessitent des commandes dédiées pour pouvoir les lire.

Pour éviter que les fichiers journaux ne deviennent trop volumineux, la plupart des distributions Linux mettent en place un mécanisme de rotation des journaux. Cela signifie que les fichiers journaux sont régulièrement archivés ou tronqués pour conserver uniquement les informations récentes. Les fichiers journaux archivés ont souvent une extension de fichier telle que `.log.1`, `.log.2`, etc.

Quelques exemples de fichiers journaux courants et de sous-répertoires :

- `/var/log/auth.log` : Ce fichier journal enregistre les informations d'authentification, telles que les tentatives de connexion réussies ou échouées.
- `/var/log/syslog` : Il contient des messages système généraux et des informations sur les événements du système.
- `/var/log/messages` : Similaire à `/var/log/syslog`, il enregistre des messages système généraux.
- `/var/log/dmesg` : Ce fichier journal enregistre les messages du noyau, y compris les informations sur le matériel au démarrage du système. Ce fichier peut être extrait par la commande `dmesg`.
- `/var/log/apache2/` : Un exemple de sous-répertoire spécifique à une application, dans ce cas, Apache, qui contient des fichiers journaux pour le serveur web Apache.
- `/var/log/mysql/` : Un autre sous-répertoire spécifique à une application, contenant les fichiers journaux pour le système de gestion de base de données MySQL.
- `/var/log/audit/` : Ce répertoire contient les fichiers journaux du service d'audit Linux (`auditd`), qui enregistre les activités de sécurité et d'audit du système.
- `/var/log/journal/` : logs gérés par `journalctl` (logs de `systemctl`).

:::tip
La commande `logger` permet d'écrire facilement un message de l'utilisateur dans le fichier `/var/log/syslog`. Écrire un log personnalisé et vérifier son apparition dans le fichier `/var/log/syslog`.
:::

### dmesg

`dmesg` affiche le fichier de logs générés par le noyau (le _kernel ring buffer_). C'est peut-être la commande la plus importante pour résoudre un problème sur un environnement de type Linux ou Unix.

Quelques options courantes :

- `dmesg --level err` : afficher uniquement les messages d'erreur
- `dmesg -H` et `dmesg -T` : affichage humain (heure + couleur) / aficher les timestamp
- `dmesg -c` : affiche les logs puis nettoie (_clean_) le _kernel ring buffer_.

:::tip
Un autre fichier de logs important est `/var/log/messages` qui contient des messages généraux du système, souvent plus "user-friendly". Ce fichier a l'inconvénient de ne pas être écrit avant l'init.
:::

## Configuration du noyau

Les paramètres du noyau Linux sont des options de configuration qui définissent le comportement du noyau. Cela offre une flexibilité précieuse pour adapter le système aux besoins spécifiques de l'utilisateur ou de l'administrateur système.

L'objectif de cette partie est d'apprendre à gérer les paramètres dynamiques du noyau et les modules. 

La commande `sysctl` est utilisée pour consulter et modifier les paramètres statiques ou dynamiques du noyau Linux en temps réel :

- `sysctl -a` : liste tous les paramètres
- `sysctl kernel.version` : affiche la valeur du paramètres `kernel.version`
- `sysctl -w net.ipv4.ip_forward=1` : change dynamiquement le paramètre `net.ipv4.ip_forward` à `1` (activation du routage IP).
- `sysctl -p` : met à jour les paramètres tels qu'indiqués dans le fichier `/etc/sysctl.conf`.

Les modifications apportées à l'aide de `sysctl` sont généralement temporaires et ne sont pas persistantes après le redémarrage du système, sauf si vous configurez explicitement les fichiers de configuration appropriés pour les paramètres du noyau.

## Les modules noyau

- Les modules noyau sont des morceaux de code qui peuvent être chargés et déchargés du noyau Linux sans nécessiter une recompilation complète du noyau. Ils étendent les fonctionnalités du noyau en ajoutant des pilotes, des fonctionnalités ou en modifiant le comportement du noyau.
- L'installation des modules sur le système est en général géré par le système de paquets : `apt`, `dnf`, ...

### Commandes utiles

- `lsmod` : liste les modules actuellement chargés dans le noyau
- `modprobe` / `modprobe -r` : charge / décharge un module. Par exemple `modprobe usb-storage` charge le module `usb-storage`. Le noyau gère automatiquement les dépendances.
- `dmesg` permet de vérifier les journaux système pour résoudre les problèmes liés aux modules

### depmod

`depmod` génère et mets à jour la base de données des dépendances des modules noyau. Cette base de données est essentielle pour le système d'exploitation afin de savoir quelles dépendances existent entre les différents modules noyau, ce qui est crucial pour charger les modules correctement et gérer les dépendances.

 - La principale fonction de `depmod` est de créer ou mettre à jour un fichier de dépendances des modules noyau. Ce fichier répertorie toutes les dépendances entre les modules noyau présents sur le système.
 - Le fichier de base pour `depmod` est généralement `/lib/modules/<version-du-noyau>/modules.dep`. Ce fichier est créé ou mis à jour par `depmod` en fonction de la configuration actuelle des modules noyau sur le système.
 - `depmod` examine chaque module noyau présent dans le répertoire des modules (`/lib/modules/<version-du-noyau>/`) et identifie les symboles (fonctions, variables, etc.) dont le module dépend, ainsi que les modules qui fournissent ces symboles. Cela permet au noyau de charger automatiquement les modules nécessaires lorsqu'ils sont requis par d'autres modules.
 - Utilisation typique : La commande `depmod` est généralement exécutée automatiquement lorsque de nouveaux modules sont installés ou lorsque le noyau est mis à jour. Cependant, vous pouvez également l'exécuter manuellement pour vous assurer que la base de données des dépendances est à jour.
 - `depmod -a` pour lister tous les modules.
 - `depmod -b` pour indiquer une version spécifique du noyau.

### Travaux Pratiques sur les modules

1. Vérifiez votre version du noyau Linux, et déplacez-vous dans le répertoire de ses modules.
2. Vérifiez la date du fichier `modules.dep`. Si elle semble ancienne, lancez une commande pour le regénérer. 
3. Listez les modules actuellement chargés. S’il n’y est pas, chargez le module `vfat` et ses dépendances. 
4. De la même manière déchargez le module `vfat` et ses dépendances. 
5. Le paramètre dynamique `arp_announce` du noyau permet de modifier les en-têtes ARP en fonction de l’adresse de destination du paquet. Sur une machine disposant de plusieurs cartes réseaux, la valeur par défaut peut poser des problèmes car Linux peut répondre avec l’adresse d’une carte quelconque. Il faut que la carte réponde avec une adresse du même sous-réseau que la destination. Vérifiez quels paramètres du noyau sont impactés.
6. Modifiez dynamiquement pour l’ensemble des adaptateurs la valeur `arp_announce` à `1` (on utilisera l'option `-w` pour modifier une valeur dynamiquement). 
7. Cette modification doit être définitive. Modifiez le fichier `/etc/sysctl.conf` et rechargez-le.

:::correction

1. Vérifiez votre version du noyau Linux, et déplacez-vous dans le répertoire de ses modules : 

```
$ uname -r 
5.15.59-0-lts

---------------------------------------------------------

$ cd /lib/modules/5.15.59-0-lts
```

2. Vérifiez la date du fichier `modules.dep`. Si elle semble ancienne, lancez une commande pour le regénérer. 

```
$ ls -l modules.dep 
-rw-r--r--    1 root     root        465979 Jul  6  2022 modules.dep

---------------------------------------------------------

$ depmod -a 
```

3. Listez les modules actuellement chargés. S’il n’y est pas, chargez le module `vfat` et ses dépendances. 

```
$ lsmod 

---------------------------------------------------------

$ lsmod | grep vfat 

---------------------------------------------------------

$ modprobe vfat 
```

4. De la même manière déchargez le module `vfat` et ses dépendances. 

```
$ modprobe -r vfat 
```

5. Le paramètre dynamique `arp_announce` du noyau permet de modifier les en-têtes ARP en fonction de l’adresse de destination du paquet. Sur une machine disposant de plusieurs cartes réseaux, la valeur par défaut peut poser des problèmes car Linux peut répondre avec l’adresse d’une carte quelconque. Il faut que la carte réponde avec une adresse du même sous-réseau que la destination. Vérifiez quels paramètres du noyau sont impactés.

```
$ sysctl -a | grep arp_announce 

net.ipv4.conf.all.arp_announce = 0 
net.ipv4.conf.default.arp_announce = 0 
net.ipv4.conf.lo.arp_announce = 0 
net.ipv4.conf.eth0.arp_announce = 0 
net.ipv4.conf.eth1.arp_announce = 0 
net.ipv4.conf.eth2.arp_announce = 0 
```

6. Modifiez dynamiquement pour l’ensemble des adaptateurs la valeur `arp_announce` à `1` (on utilisera l'option `-w` pour modifier une valeur dynamiquement). 

```
$ sysctl -w net.ipv4.conf.all.arp_announce=1 
```

**Attention : cette modification est dynamique mais n'est pas persistée ! Voir la question suivante.**

7. Cette modification doit être définitive. Modifiez le fichier `/etc/sysctl.conf` et rechargez-le.

```
$ vi /etc/sysctl.conf 
```

Ajoutez : 

```
net.ipv4.conf.all.arp_announce = 1 
```

Et sauvez. Rechargez les nouvelles valeurs : 

```
$ sysctl -p
```
:::

## Infomations sur la configuration du système

1. Chercher dans les logs du noyau les lignes correspondant aux firmwares de la machine.

:::correction
```
$ dmesg | grep firmware
```
:::

1. À l'aide de commandes dédiées, afficher la version du noyau, l'architecture du système, le hostname

:::correction
```
# version du noyau

$ uname -r

udevadm info -q path -n /dev/sdb

---------------------------------------------------------

# ou plus détaillé :

$ uname -v

#1-Alpine SMP Fri, 05 Aug 2022 07:05:02 +0000

---------------------------------------------------------

# architecture

$ uname --machine

x86_64

---------------------------------------------------------

# hostname

$ uname -n

alpine.tom
```
:::

1. Depuis combien de temps le noyau est-il en fonctionnement ?

:::correction
```
uptime
```
:::

1. Quelle est la taille de la mémoire RAM de votre système (en utilisant un fichier du système) ? Comment afficher de manière lisible pour un humain l'espace RAM et swap libres sur le système par une commande dédiée ?

:::correction
Visualiser le fichier `/proc/meminfo`. La taille de la RAM est indiquée à la ligne `Total`.

Par exemple :

```
$ cat /proc/meminfo | grep Total

MemTotal:       16262708 kB
SwapTotal:             0 kB
```

Pour afficher l'utilisation de la RAM et du swap de manière lisible, on peut utiliser la commande `free -h` :

```
              total        utilisé      libre     partagé     tamp/cache    disponible
Mémoire :     15G           2,0G        8,0G         1,1G           5,0G           11G
Swap :           2,0G        0B            2,0G
```

La sortie est divisée en deux sections principales : la section "Mémoire" et la section "Swap".

- Section "Mémoire" :
  - total : Indique la taille totale de la mémoire physique installée sur le système. Dans cet exemple, la taille totale de la mémoire est de 15 Go.
  - utilisé : Montre la quantité de mémoire actuellement utilisée par le système. Dans cet exemple, 2,0 Go de mémoire sont utilisés.
  - libre : Indique la quantité de mémoire physique qui n'est pas utilisée par le système. Dans cet exemple, il y a 8,0 Go de mémoire libre.
  - partagé : Représente la mémoire partagée entre plusieurs processus. Cela inclut généralement la mémoire partagée entre les bibliothèques partagées. Dans cet exemple, 1,1 Go de mémoire sont partagés.
  - tampon/cache : Affiche la quantité de mémoire utilisée pour les tampons et le cache système. Le cache est utilisé pour stocker des données fréquemment utilisées afin d'accélérer l'accès aux fichiers. Dans cet exemple, 5,0 Go de mémoire sont utilisés pour les tampons et le cache.
  - disponible : Indique la quantité de mémoire qui est disponible pour les nouveaux processus sans avoir besoin de recourir à la pagination (swap). Dans cet exemple, 11 Go de mémoire sont disponibles.
- Section "Swap" :
  - total : Montre la taille totale de l'espace d'échange (swap) disponible sur le système. Dans cet exemple, la taille totale de l'espace d'échange est de 2,0 Go.
  - utilisé : Indique la quantité d'espace d'échange actuellement utilisée. Dans cet exemple, aucun espace d'échange n'est actuellement utilisé (0B).
  - libre : Représente la quantité d'espace d'échange non utilisée. Dans cet exemple, il y a 2,0 Go d'espace d'échange libre.
:::

1. Quels sont les différents CPUs de votre système ?

:::correction
Visualiser le fichier `/proc/cpuinfo` :

```
$ cat /proc/cpuinfo

[...]
processor	: 3
vendor_id	: GenuineIntel
cpu family	: 6
model		: 61
model name	: Intel(R) Core(TM) i7-5600U CPU @ 2.60GHz
stepping	: 4
microcode	: 0x2d
cpu MHz		: 1642.679
cache size	: 4096 KB
physical id	: 0
siblings	: 4
core id		: 1
cpu cores	: 2
apicid		: 3
initial apicid	: 3
fpu		: yes
fpu_exception	: yes
cpuid level	: 20
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts acpi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc arch_perfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dtes64 monitor ds_cpl vmx smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefetch cpuid_fault epb invpcid_single pti ssbd ibrs ibpb stibp tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm rdseed adx smap intel_pt xsaveopt dtherm ida arat pln pts md_clear flush_l1d
vmx flags	: vnmi preemption_timer invvpid ept_x_only ept_ad ept_1gb flexpriority tsc_offset vtpr mtf vapic ept vpid unrestricted_guest ple shadow_vmcs
bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs taa itlb_multihit srbds
bogomips	: 5189.92
clflush size	: 64
cache_alignment	: 64
address sizes	: 39 bits physical, 48 bits virtual
power management:
```
:::

1. Quels sont les périphériques qui partagent la même ligne d'interruption ?

:::correction
Exécuter la commande `cat /proc/interrupts`.

Par exemple ici, les 4 CPUs (en réalité 4 coeurs) partagent les mêmes instructions :
```
           CPU0       CPU1       CPU2       CPU3       
  0:         10          0          0          0  IR-IO-APIC   2-edge      timer
  1:          0          0     498155          0  IR-IO-APIC   1-edge      i8042
  8:          0          0          0          1  IR-IO-APIC   8-edge      rtc0
  9:          0     151729          0          0  IR-IO-APIC   9-fasteoi   acpi
 12:          0   25927825          0          0  IR-IO-APIC  12-edge      i8042
 18:          5          0          0          0  IR-IO-APIC  18-fasteoi   i801_smbus
 23:          0          0          0         35  IR-IO-APIC  23-fasteoi   ehci_hcd:usb1
 40:          0          0          0          0  DMAR-MSI   0-edge      dmar0
 41:          0          0          0          0  DMAR-MSI   1-edge      dmar1
 44:          0      18216          0          0  IR-PCI-MSI 512000-edge      ahci[0000:00:1f.2]
 45:          0          0          6          0  IR-PCI-MSI 1048576-edge      rtsx_pci
 46:    5420185          0          0          0  IR-PCI-MSI 327680-edge      xhci_hcd
 47:          0         35          0          0  IR-PCI-MSI 360448-edge      mei_me
 49:          0          0          0    5477677  IR-PCI-MSI 442368-edge      snd_hda_intel:card1
 50:          0   38178760          0          0  IR-PCI-MSI 32768-edge      i915
 51:          0          0    3436350          0  IR-PCI-MSI 1572864-edge      iwlwifi
 52:          0          0          0        102  IR-PCI-MSI 49152-edge      snd_hda_intel:card0
NMI:       2580       2281       2551       2277   Non-maskable interrupts
LOC:   44097695   55894238   44288438   50978560   Local timer interrupts
SPU:          0          0          0          0   Spurious interrupts
PMI:       2579       2280       2550       2276   Performance monitoring interrupts
IWI:   19488003   39220992   19642222   26510151   IRQ work interrupts
RTR:          2          0          0          0   APIC ICR read retries
RES:    2282504    2259920    2083401    3869867   Rescheduling interrupts
CAL:   20234374   23298697   25685763   22115149   Function call interrupts
TLB:   17333302   20629355   23801626   20604782   TLB shootdowns
TRM:       1636       1636       1636       1636   Thermal event interrupts
THR:          0          0          0          0   Threshold APIC interrupts
DFR:          0          0          0          0   Deferred Error APIC interrupts
MCE:          0          0          0          0   Machine check exceptions
MCP:       1225       1226       1226       1226   Machine check polls
ERR:          0
MIS:          0
PIN:          0          0          0          0   Posted-interrupt notification event
NPI:          0          0          0          0   Nested posted-interrupt event
PIW:          0          0          0          0   Posted-interrupt wakeup event
```
:::

## Bus PCI

1. Isolez l’adresse matérielle de votre carte graphique sur le bus PCI. (Les cartes AGP et PCI Express sont vues comme un bus PCI. On cherchera un contrôleur VGA).
2. Obtenez plus de détails sur cette carte. Notamment, quel module la gère ? Ces informations peuvent être obtenues avec le -v et en spécifiant uniquement la carte avec le -s de `lspci`.

:::correction
```
# 1.
$ lspci | grep -i vga
00:02.0 VGA compatible controller: Intel Corporation HD Graphics 5500 (rev 09)

---------------------------------------------------------

# 2.
lspci -s 00:02.0 -v
00:02.0 VGA compatible controller: Intel Corporation HD Graphics 5500 (rev 09) (prog-if 00 [VGA controller])
	[...]
	Kernel driver in use: i915
```
:::

1. Récupérer les informations sur les bus PCI **SANS** utiliser la commande `lspci`.

:::correction
`lspci` utilise les informations de `/proc/bus/pci/devices`.
:::

1. Utilisez l'utilitaire `lspci` avec les options correctes pour obtenir le dessin de l'architecture P.C.I. de votre système : Combien y a-t-il de bus et de ponts P.C.I. ? Et des ponts P.C.I./I.S.A. ?

:::correction
- Exécuter la commande `lspci -tv` pour avoir l'arborescence.
- Exécuter la commande `lspci -v | grep -i bridge` pour trouver les bridges.

Par exemple ici, un seul pont PCI :
```
$ lspci -tv

-[0000:00]-+-00.0  Intel Corporation Broadwell-U Host Bridge -OPI
           +-02.0  Intel Corporation HD Graphics 5500
           +-03.0  Intel Corporation Broadwell-U Audio Controller
           +-14.0  Intel Corporation Wildcat Point-LP USB xHCI Controller
           +-16.0  Intel Corporation Wildcat Point-LP MEI Controller #1
           +-19.0  Intel Corporation Ethernet Connection (3) I218-LM
           +-1b.0  Intel Corporation Wildcat Point-LP High Definition Audio Controller
           +-1c.0-[02]----00.0  Realtek Semiconductor Co., Ltd. RTS5227 PCI Express Card Reader
           +-1c.1-[03]----00.0  Intel Corporation Wireless 7265
           +-1d.0  Intel Corporation Wildcat Point-LP USB EHCI Controller
           +-1f.0  Intel Corporation Wildcat Point-LP LPC Controller
           +-1f.2  Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode]
           +-1f.3  Intel Corporation Wildcat Point-LP SMBus Controller
           \-1f.6  Intel Corporation Wildcat Point-LP Thermal Management Controller
```

```
$ lspci -v | grep -i bridge

00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #6 (rev e3) (prog-if 00 [Normal decode])
	I/O behind bridge: [disabled] [16-bit]
	Memory behind bridge: e1100000-e11fffff [size=1M] [32-bit]
	Prefetchable memory behind bridge: [disabled] [64-bit]
00:1c.1 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3) (prog-if 00 [Normal decode])
	I/O behind bridge: [disabled] [16-bit]
	Memory behind bridge: e1000000-e10fffff [size=1M] [32-bit]
	Prefetchable memory behind bridge: [disabled] [64-bit]
00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03) 
```
:::

1. Quelles sont les options de `lspci` permettant d’établir la liste des périphériques P.C.I. `Intel` ?

:::correction
L'information de vendeur est le 1er segment affiché par `lspci -nn`.
```
$ lspci -nn | grep -i intel

00:00.0 Host bridge [0600]: Intel Corporation Broadwell-U Host Bridge -OPI [8086:1604] (rev 09)
00:02.0 VGA compatible controller [0300]: Intel Corporation HD Graphics 5500 [8086:1616] (rev 09)
00:03.0 Audio device [0403]: Intel Corporation Broadwell-U Audio Controller [8086:160c] (rev 09)
00:14.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB xHCI Controller [8086:9cb1] (rev 03)
00:16.0 Communication controller [0780]: Intel Corporation Wildcat Point-LP MEI Controller #1 [8086:9cba] (rev 03)
00:19.0 Ethernet controller [0200]: Intel Corporation Ethernet Connection (3) I218-LM [8086:15a2] (rev 03)
00:1b.0 Audio device [0403]: Intel Corporation Wildcat Point-LP High Definition Audio Controller [8086:9ca0] (rev 03)
00:1c.0 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #6 [8086:9c9a] (rev e3)
00:1c.1 PCI bridge [0604]: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 [8086:9c94] (rev e3)
00:1d.0 USB controller [0c03]: Intel Corporation Wildcat Point-LP USB EHCI Controller [8086:9ca6] (rev 03)
00:1f.0 ISA bridge [0601]: Intel Corporation Wildcat Point-LP LPC Controller [8086:9cc3] (rev 03)
00:1f.2 SATA controller [0106]: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] [8086:9c83] (rev 03)
00:1f.3 SMBus [0c05]: Intel Corporation Wildcat Point-LP SMBus Controller [8086:9ca2] (rev 03)
00:1f.6 Signal processing controller [1180]: Intel Corporation Wildcat Point-LP Thermal Management Controller [8086:9ca4] (rev 03)
03:00.0 Network controller [0280]: Intel Corporation Wireless 7265 [8086:095b] (rev 99)
```

On remarque que tous les périphériques `Intel` ont un `VendorID` à `8086` :

```
$ lspci -d 8086:

00:00.0 Host bridge: Intel Corporation Broadwell-U Host Bridge -OPI (rev 09)
00:02.0 VGA compatible controller: Intel Corporation HD Graphics 5500 (rev 09)
00:03.0 Audio device: Intel Corporation Broadwell-U Audio Controller (rev 09)
00:14.0 USB controller: Intel Corporation Wildcat Point-LP USB xHCI Controller (rev 03)
00:16.0 Communication controller: Intel Corporation Wildcat Point-LP MEI Controller #1 (rev 03)
00:19.0 Ethernet controller: Intel Corporation Ethernet Connection (3) I218-LM (rev 03)
00:1b.0 Audio device: Intel Corporation Wildcat Point-LP High Definition Audio Controller (rev 03)
00:1c.0 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #6 (rev e3)
00:1c.1 PCI bridge: Intel Corporation Wildcat Point-LP PCI Express Root Port #3 (rev e3)
00:1d.0 USB controller: Intel Corporation Wildcat Point-LP USB EHCI Controller (rev 03)
00:1f.0 ISA bridge: Intel Corporation Wildcat Point-LP LPC Controller (rev 03)
00:1f.2 SATA controller: Intel Corporation Wildcat Point-LP SATA Controller [AHCI Mode] (rev 03)
00:1f.3 SMBus: Intel Corporation Wildcat Point-LP SMBus Controller (rev 03)
00:1f.6 Signal processing controller: Intel Corporation Wildcat Point-LP Thermal Management Controller (rev 03)
03:00.0 Network controller: Intel Corporation Wireless 7265 (rev 99)
```
:::

1. À quoi sert l'utilitaire `setpci` ?

:::correction
Accéder aux périphériques P.C.I. et les configurer.
:::

1. Quelle est la température du processeur ? Utiliser l'ACPI, le chemin exact peut être dépendant du constructeur (chercher `thermal` ou `temperature`).
Attention, il faut que le service ACPI soit installé. Sur Fedora, on pourra utiliser : `sudo dnf install -y acpid && systemctl start acpid` et sur Ubuntu : `sudo apt install -y acpid && systemctl start acpid`

:::correction
Exemples de réponses :

```
$ cat /proc/acpi/thermal_zone/THM/temperature
$ cat /proc/acpi/ibm/thermal

temperatures:	41 0 0 0 0 0 0 0
```
:::

1. Branchez une clé USB sur votre PC. Si vous êtes en environnement graphique, il se peut que le gestionnaire de fichiers s’ouvre. Quels sont les mécanismes mis en œuvre ? Comment trouver des informations sur le périphérique ?

:::correction
Voici les mécanismes mis en œuvre :

- Dans un premier temps, le noyau détecte la connexion et charge le module USB correspondant. 
- Le périphérique de base est créé. Un événement est généré. 
- Le service `udev` détecte l'événement et exécute les règles associées : modification, par exemple, des droits sur le périphérique. 
- Pour l'interface graphique, un autre service, `hal` (hardware abstraction layer) est un bus de communication entre les divers éléments. Il intercepte aussi l'événement et exécute d’autres règles, cette fois dans l'espace utilisateur : il ouvre le gestionnaire de fichiers. 

Pour obtenir des informations :

- La commande `lsusb` liste les périphériques USB. On peut l'exécuter avant et après avoir inséré la clé pour vérifier qu'un nouveau périphérique est bien détecté.
- Le noyau va écrire des logs à la détection du périphérique : voir `dmesg`. C'est généralement un bon point de départ en cas de problème avec un périphérique (par exemple un module noyau manquant, voir le TP dédié).
- Il s'agit d'un périphérique de type _bloc_ : les commandes `lsblk` et `blkid` vont afficher les fichiers de périphérique associés.
:::

## udev

1. Utiliser `udev` pour afficher toutes les informations possibles sur la carte réseau du système.
2. Utiliser `udev` pour récupérer le fichier système associé au fichier de périphérique de la partition racine du système.

:::correction
```
#1.
udevadm info -p /sys/class/net/eth0 -a

---------------------------------------------------------

#2.
udevadm info -q path -n /dev/sda1
```
:::
