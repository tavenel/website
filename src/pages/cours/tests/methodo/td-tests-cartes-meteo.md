---
title: Tests d'un système de cartes météo
author: Tom Avenel
date: 2023 / 2024
---
 
\newpage{}

# Carte météo

Un système de carte météo (`CM`) doit générer des cartes avec la météo de chaque région en se basant sur les données collectées à partir des stations météo (`SM`) ou autres sources comme les ballons-sondes ou satellites. Les `SM` transmettent leurs données à un central de région (`CR`) en réponse à une requête de celui-ci. Un `CR` valide les données collectées des `SM` et les intègrent avec les données des autres sources. Les données intégrées sont archivées. En utilisant les données de cette archive et une BD de cartes numériques, le `CR` génère toutes les heures un ensemble de cartes météo locales. Ces cartes peuvent être imprimées ou affichées en différents formats.

```{render="{{plantuml.svg}}" alt="Architecture logicielle d'un système de cartes météo"}
@startuml
package DataCollection {
  rectangle Comms
  rectangle Observateur
  rectangle Satellite
  rectangle "Station météo"
  rectangle Ballon
  Comms -left- Observateur
  Comms -down- "Station météo"
  Comms -up- Satellite
  Comms -right- Ballon
}
package DataProcessing {
  rectangle "Vérification de données"
  rectangle "Intégration de données"
  "Vérification de données" - "Intégration de données"
}
package DataArchiving {
  rectangle "Map store"
  rectangle "Data store"
  rectangle "Data storage"
  "Data storage" -left- "Map store"
  "Data store" -right- "Data store"
}
package DataDisplay {
  rectangle "Interface utilisateur"
  rectangle Carte
  rectangle "Affichage de la carte"
  rectangle "Impression de carte"
  "Affichage de la carte" -left- "Interface utilisateur"
  "Affichage de la carte" -down- Carte
  Carte -right- "Impression de carte"
}
DataProcessing -left- DataCollection
DataProcessing -right- DataArchiving
DataArchiving -right- DataDisplay
@enduml
```

_Figure 1 : Architecture logicielle d'un système de cartes météo._

## Exercice 1 : Plan de test

En utilisant l'architecture de ce système, constituez un plan de test en précisant plus particulièrement : 

1. Les phases du test à prévoir ;
2. Le plan du test d'acceptation pour les utilisateurs ;
3. Les composants à tester ;
4. Les besoins en matériel et logiciel à prévoir.

## Exercice 2 : Test de système : test d'acceptation

En utilisant l'architecture donnée pour l'interface utilisateur, proposez une suite de tests à effectuer pour démontrer que le système satisfait ses charges.

## Exercice 3 : Test de système : test d'intégration

Proposez une procédure top-down et une procédure bottom-up pour effectuer le test d'intégration des composantes du système `CM`.

## Exercice 4 : Test de système : test de performance

Proposez une suite de tests qui montrent les performances en temps et aux limites du système `CM`.

# Station météo

Dans la suite, nous allons nous intéresser plus particulièrement au sous-système station météo (`SM`). Une `SM` est un ensemble d'instruments de mesure contrôlés par un logiciel. Le logiciel collecte les mesures et l'état des instruments, effectue des calculs sur les données et transmet ces données au `CR`. Les instruments inclus dans un `SM` sont : deux thermomètres (un de l'air et l'autre du sol), un anémomètre (appareil permettant de mesurer la vitesse ou la pression du vent), une manche à vent, un baromètre et un pluviomètre. Les données sont collectées périodiquement. Quand une commande de collecte arrive, le `SM` fait un rapport des données collectées et le transmet au `CR`.

Les figures ci-dessous décrivent les architectures de haut niveau et détaillée du sous-système `SM`.

```{render="{{plantuml.svg}}" alt="Architecture haut niveau du sous-système SM"}
@startuml
package "Station météo" {
  [<<subsystem>> Interface] as C1
  note right of C1
    Gère les communications externes
  end note
  [<<subsystem>> Data collection] as C2
  note right of C2
    Collecte et résume les données météo
  end note
  [<<subsystem>> Data collection] as C3
  note right of C3
    Package d'instruments pour la collecte de données brutes
  end note
  C1 -- C2
  C2 -- C3
}
@enduml
```

```{render="{{plantuml.svg}}" alt="Architecture détaillée du sous-système SM"}
@startuml
package "<<subsystem>> Interface" {
  [CommsController] as CC
  [WeatherStation] as WS
  CC -- WS
}

package "<<subsystem>> Data collection" as DC {
  [WeatherData] as WD
  [Instrument Status] as IS
  WD -- IS
  WS -- DC
}

package "<<subsystem>> Instruments" as INS {
  [Air thermometer] as INS1
  [RainGauge] as INS2
  [Anemometer] as INS3
  [Ground thermometer] as INS4
  [Barometer] as INS5
  [WindVane] as INS6
  WD --- INS
  IS --- INS
}
@enduml
```

Les cas d'utilisation de ce sous-système ainsi que le diagramme de flot des services du `SM` sont donnés dans les figures ci-dessous.

```{render="{{plantuml.svg}}" alt="Architecture détaillée du sous-système SM"}
@startuml
utilisateur as A
A --> (Startup)
A --> (Shutdown)
A --> (Report)
A --> (Calibrate)
A --> (Test)
@enduml
```

```{render="{{plantuml.svg}}" alt="Diagramme d'activité du sous-système SM"}
@startuml
[*] --> Shutdown

state "Operation" as Operation {

    Shutdown --> Waiting : startup()

    Waiting --> Calibrating : calibrate()
    Calibrating --> Testing : calibration OK

    Waiting --> Testing : test()

    Waiting --> Collecting : clock
    Collecting --> Waiting : collection done

    Waiting --> Summarising : reportWeather()

    Testing --> Transmitting : test complete
    Summarising --> Transmitting : weather summary complete
    Transmitting --> Waiting : transmission done
}
Waiting --> Shutdown : shutdown()
@enduml
```

## Exercice 5 : Test de système : test de fonctionnement

En utilisant le diagramme de flot, proposez une suite de tests pour valider le fonctionnement correct du sous-système `SM`.


Dans le cahier des charges, le cas d'utilisation Report est spécifié à l'aide de la fiche ci-dessous et du diagramme de séquence (pour l'utilisation nominale) de la figure 4.

> Système : Station météo
> Cas d'utilisation : Report
> Acteurs : Sous-système de collecte de données, Sous-système station météo
> Description : La `SM` envoie un résumé des données collectées en utilisant ses différents instruments dans la période de temps observée depuis la dernière demande. Les données envoyées sont la température minimum, maximum et moyenne de l'air et du sol, la pression maximum et minimum de l'air, la vitesse minimum et maximum du vent, le volume total de pluie et les directions du vent mesurées toutes les 5 minutes.
> Activation : Le sous-système de collecte de données établit une connexion modem avec le système de communication et demande la collecte de données.
> Effet : Le résumé des données collectées est transmis au demandeur.
> Commentaires : Les `SM` sont interrogés usuellement avec une fréquence de 1 fois toutes les heures mais cette fréquence peut être différente d'une `SM` à l'autre et peut augmenter dans le futur. 

## Exercice 6 : Test de composant : en boîte noire

En utilisant le diagramme de flot et le diagramme de classe, proposez une suite de tests pour tester la classe `WeatherStation`. Pourquoi s'agit-il de tests en boîte noire ?

```{render="{{plantuml.svg}}" alt="Diagramme de flot"}
@startuml
actor User
participant "CommsController" as CC
participant "WeatherStation" as WS
participant "WeatherData" as WD

User -> CC : request(report)
CC -> User : acknowledge()
CC -> WS : report()
WS -> WD : summarise()
WS --> CC : send(report)
CC -> User : reply(report)
User -> CC : acknowledge()
@enduml
```

```{render="{{plantuml.svg}}" alt="Diagramme de classe"}
@startuml
class WeatherStation {
  identifier
  reportWeather()
  calibrate(instruments)
  test()
  startup(instruments)
  shutdown(instruments)
}

class WeatherData {
  airTemperatures
  groundTemperatures
  windSpeeds
  windDirections
  pressures
  rainfall
  collect()
  summarise()
}

class GroundThermometer {
  temperature
  test()
  calibrate()
}

class Anemometer {
  windSpeed
  windDirection
  test()
}

class Barometer {
  pressure
  height
  test()
  calibrate()
}

WeatherStation --> WeatherData
WeatherStation ..> GroundThermometer : uses
WeatherStation ..> Anemometer : uses
WeatherStation ..> Barometer : uses
@enduml
```

## Exercice 7 : Test de composant : fonction Report

En utilisant le diagramme de séquence, proposez une suite de tests pour tester le cas d'utilisation `Report`.

## Exercice 8 :

La méthode `summarize()` de la classe `WeatherData` utilise une méthode `computeAv` spécifiée comme suit :

```java
/**
* Compute the average value of the sequence values.
* Pre-condition: values is not empty, values.length>=1
* Post-condition:
* - the average can be computed and the return is the value of the average
* or - the average cannot be computed and the result is the float constant NaN
*/
Float computeAv(Float[] values)
```

1. Donnez une partition de l'ensemble des entrées de cette méthode qui regroupe les valeurs des entrées qui génèrent les mêmes types de sorties. Pour chaque partition identifiée, écrivez une suite de cas de tests en précisant les données de test et les résultats attendus.
2. Donnez une implémentation en pseudo-code pour la méthode `computeAv` ci-dessus.
3. Écrivez une suite de tests qui couvre toutes les instructions.
4. Écrivez une suite de tests qui couvre toutes les décisions.

