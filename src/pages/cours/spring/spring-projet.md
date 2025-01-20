---
title: Projet Spring / Hibernate
author: Tom Avenel
---

L'objectif de ce projet est la création d'une application fullstack en utilisant le framework Spring Boot. La persistance des données sera assurée par le framework Hibernate.

# Présentation de l'application

L'application possède plusieurs fonctionnalités rendues disponibles à l'utilisateur à travers la couche de présentation permettant : 

- La création, l'édition, la suppression et le listing de produits consommables. La vue de création d'un produit permet de renseigner au minimum le nom, le code du produit, la quantité et la date de péremption. Le listing permet d'afficher le nom, le code du produit, la quantité, le nombre de jours restant avant péremption, et une information visuelle si le produit est périmé.
- La création d'un compte client, le login d'un utilisateur et l'affichage du compte utilisateur courant (partie V)

# Travail attendu

Le projet est à réaliser en trinôme.

Chaque trinôme pourra au choix :

- Soit fournir un lien vers un hébergement centralisé de code source (GitHub, Bitbucket, GitLab, …) dans le rapport : cette méthode est à privilégier si possible.
- Soit fournir une archive contenant l'ensemble du code source de l'application, en même temps que l'envoi du rapport.

L'application devra être une application Web fullstack Spring/JSP avec persistance de données via Hibernate. Il n'est pas attendu de configuration de la base de données, on pourra utiliser une base en mémoire H2 pour le développement et le rendu final.

Il est attendu dans le rapport du projet :

- Une description de l'application et des choix techniques effectués
- La liste des entités persistées en expliquant votre choix 
- Le cycle de vie des sessions Hibernate (quand les sessions sont-elles créées et supprimées ?) en expliquant votre choix 
- Les principales classes créées ayant un impact sur l'architecture du projet, en expliquant cet impact
- Un ou plusieurs diagrammes de classe modélisant la ou les utilisation(s) du pattern MVC dans votre application. L'utilisation d'un diagramme au formalisme rigoureux (type UML) n'est pas obligatoire.

**Une partie importante de la note finale sera liée au rapport du projet.**


# Introduction : Récupérer l'application et la lancer

## Récupération du template

Récupérer le template d'application fourni par l'encadrant :

```
git clone https://avenelt@bitbucket.org/avenelt/springhibernate2021.git
```

Cette application utilise l'outil de build Gradle comme gestionnaire de dépendances, ordonnanceur de la compilation et lanceur d'application. Le fonctionnement de Gradle est très similaire à Maven.

Un exécutable `gradlew` (Linux) ou `gradlew.bat` (Windows) est fourni dans le répertoire de travail de l'application : il n'est donc pas nécessaire d'installer Gradle sur sa machine de travail.

Gradle utilise le plugin Java et attend l'arborescence suivante :

- Les fichiers source `*.java` dans `src/main/java`
- Les ressources (fichiers de propriétés, etc) dans `src/main/resources`
- Les vues JSP dans `src/main/webapp`

## Lancement de l'application

Pour démarrer l'application, il faut :

1. Se placer dans le répertoire de l'application
2. lancer la commande : `gradlew appRun`

Cette commande va lancer un container Tomcat embarqué et déployer automatiquement l'application dans celui-ci.

L'application est alors accessible à l'URL : <http://localhost:8080/B3-Spring/home>

## Développement de l'application

Afin de faciliter l'apprentissage des différentes technologies, on procèdera à un développement itératif par couches. La plupart des méthodes de gestion de projet récentes préfèrent éviter ce découpage (méthodes agiles par exemple), car chaque couche peut imposer des contraintes techniques et architecturales fortes, ce qui remettrait en cause les couches précédentes.

Ainsi, on commencera par développer le code métier de l'application à l'exception de la gestion des utilisateurs (partie I), pour s'intéresser ensuite à la persistance des entités métier (parties II et III). On utilisera ensuite le pattern MVC pour fournir une couche de présentation (partie IV). On finira par ajouter les fonctionnalités liées aux utilisateurs : login, persistance des comptes et stockage de l'utilisateur courant dans un Cookie.

Les parties II et III sont dépendantes, les autres parties peuvent être réalisées indépendamment mais il est conseillé de suivre l'ordre proposé dans le sujet.


# Partie I : Spring Framework et application multi-couche

Afin de faciliter l'architecture et la configuration de l'application, nous allons déléguer à Spring un certain nombre de comportements. Nous allons également rendre notre application multi-couches.

## I.1 Génération d'un ApplicationContext

Spring stocke l'ensemble de ses configurations, ses composants, ... sous forme de `Bean`. Un Bean correspond à l'instance unique d'une classe (singleton) définie dans le framework Spring (il est possible de créer plusieurs instances d'une classe en cas de besoin spécifique, en changeant la configuration de la classe dans Spring ou en créant des Beans manuellement).

L'ensemble des beans (i.e. l'ensemble des instances de classes connues de Spring) sont rattachés à un singleton particulier appelé `ApplicationContext`.

Il existe de nombreuses manières de générer un `ApplicationContext`, nous allons nous contenter de l'instance par défaut qui gère une application par annotations :

```java
ApplicationContext myApplicationContext = new AnnotationConfigApplicationContext("org.epsi");
```

Attention : cet objet doit donc être un singleton dans votre application, et être disponible à chaque fois que nécessaire !

## I.2 Injection de dépendances - notions

Spring est avant tout un framework d'injection de dépendances.

L'injection de dépendances est un design pattern qui consiste à ne plus fournir directement les dépendances d'une classe de manière statique, mais à laisser le framework “injecter” ces dépendances dynamiquement lorsque nécessaire.

Par exemple : 

Afin d'enregistrer une classe comme composant Spring et comme candidat pouvant être injecté dans une autre classe, on utilisera :

- l'annotation `@Component` (ou les annotations qui en dérivent comme `@Service`, ...) sur le prototype d'une classe

- ou l'annotation `@Bean` sur une méthode dont le type de retour est une instance de cette classe

Afin d'injecter une instance de classe ou une implémentation d'interface, on utilisera l'annotation `@Autowired` sur l'objet à instancier, par exemple :

```java
@Component

public class MaDependance {

[...]

}

@Component

public class MaClasseAvecDependance {

@Autowired

private MaDependance maDependance;

}
```

Si `MaClasseAvecDependance` est récupérée depuis le contexte Spring (voir note ci-dessous), alors `maDependance` sera automatiquement instanciée et injecté dans cette classe – il n'est donc plus nécessaire de fournir explicitement une instance pour `maDependance`.

Il existe également de nombreuses autres méthodes permettant de définir et d'injecter les dépendances : fichier XML, constructeur, setter, …

### Note sur l'injection de dépendances

Attention : Pour profiter de l'injection de dépendances, il faut laisser Spring “prendre la main” sur ses composants. Cela veut dire qu'il ne faut jamais instancier soi-même un composant Spring (pas de mot-clé `new`) !!

Une conséquence est que tant qu'un composant Spring n'a pas été récupéré depuis l' `ApplicationContext`, il n'est pas possible d'injecter des dépendances dans ce composant (par exemple avec l'annotation `Autowired`) : en effet, le framework Spring n'est pas encore actif sur la classe courante, et l'application exécute alors du “pure” code Java et les appels aux dépendances retournent des `NullPointerException` puisque ces dépendances n'ont pas été injectées.

Pour récupérer l'instance d'un composant générée par Spring, il est possible d'utiliser la méthode `getBean()` de l'`ApplicationContext` :

```java
ApplicationContext appContext = ...

appContext.getBean(ProductDAO.class);
```

Ainsi, pour obtenir une instance de ProductDAO avec injection de dépendances, il ne faut pas utiliser :

```java
new ProductDAO();
```

mais plutôt :

```java
appContext.getBean(ProductDAO.class);
```

`ProductDAO` peut maintenant profiter de l'injection de dépendance, ainsi que toutes les dépendances de cette classe (récursivement).

## I.3 Application multi-couches

Tout au long du projet, utiliser l'injection de dépendances de Spring pour faciliter la séparation en différentes couches de l'application. Cela permet d'améliorer grandement l'architecture de l'application en isolant chaque responsabilité dans une couche différente.


# Partie II : Hibernate

La deuxième partie du TP consiste à faire évoluer la couche de persistance vers `Hibernate`.

Pour cela, il va falloir :

1. Définir les entités métier à persister
2. Définir et implémenter un mapping objet-relationnel à appliquer
3. Définir et implémenter le cycle de vie des sessions
4. Configurer Hibernate pour gérer les connections avec la base de données et pour instancier les mappings
5. Réaliser les appels à la base de données au travers d'Hibernate

Avant toute chose, décommenter dans le fichier `build.gradle` la ligne correspondant à hibernate afin de rajouter les dépendances dans le projet.

## II.1. Choix des entités métier à persister

Analyser l'application pour définir les entités à persister en base de données, et à quel moment la persistance doit être réalisée.

## II.2. Mapping objet-relationnel

Une fois les entitées à persister définies, il faut ensuite réaliser un mapping Objet-Relationnel pour définir quels sont les attributs à persister et comment.

Implémenter ensuite ce schéma, soit par l'utilisation d'un fichier xml soit par l'utilisation d'annotations (les 2 méthodes sont équivalentes).

Exemple d'un fichier XML `MyEntity.hbm.xml` situé dans le même package que la classe `MyEntity` :

```xml
<hibernate-mapping>

<class name="org.myPackage.MyEntity"

table=”MY\_ENTITY”>

<id name="id">

<generator class="native"/>

</id>

<property name="myString" type="string"

not-null=”true” />

</class>

</hibernate-mapping>
```

Attention : dans le cas d'un fichier XML, celui-ci devra être placé dans le répertoire `src/main/resources` de l'application pour être lu. A cause de cette contrainte, il faudra donc spécifier le nom complet de la classe précédé du package dans le champ `<class name=...>`

Exemple d'une classe `MyEntity` annotée :

```java
@Entity

@Table(name = "MY\_ENTITY")

public class MyEntity {

private Integer myId;

private String myString;

@Id

public Integer getMyId() {

@Basic(optional = false)

public String getMyString() {

return myId;

}

return myString;

}
```

## II.3. Cycle de vie des sessions

Rappel : tout dialogue avec la base de données doit être réalisé dans une transaction !

Avant de déléguer le contrôle de la base de données à Hibernate, il faut donc se poser la question du cycle de vie d'une `Session` (quand la créer, quand la libérer), et du cycle de vie de la `SessionFactory`.

Note : le `commit` ou `rollback` d'une transaction ferment en général la session, sauf dans des architectures où la session a un cycle de vie un peu spécial.

Pour plus d'information : <https://docs.jboss.org/hibernate/core/3.3/reference/en/html/transactions.html#transactions-basics-uow>

**Demander à l'encadrant de valider le choix d'architecture retenu pour le cycle de vie des sessions.**

## II.4. Configuration d'Hibernate

### II.4.1 Fichier de configuration

Hibernate se configure à l'aide d'un fichier `hibernate.cfg.xml` à placer dans `src/main/resources`

Ce fichier contient à la fois la configuration de la connexion à la BD, le cycle de vie des sessions, et les options d'Hibernate (cache, ...) mais également les références vers les différents mappings à importer.

Un exemple de configuration est fourni dans le répertoire `resourcesEtudiants` à la racine du projet.

Pour chaque mapping utilisant des annotations, ajouter une ligne de la forme :

```xml
<!-- Names the annotated entity class -->

<mapping class="org.epsi.b3.MyEntity"/>

Pour chaque mapping utilisant un fichier XML, ajouter une ligne de la forme :

<!-- Names the XML mappings -->

<mapping resource="MyEntity.hbm.xml"/>
```

### II.4.2 Génération de la SessionFactory

Nous allons créer une instance de `SessionFactory`, qui va nous servir de point d'entrée pour utiliser Hibernate.

On pourra utiliser le code suivant :

```java
new Configuration().configure().buildSessionFactory()
```

Attention à bien respecter le cycle de vie de la `SessionFactory` ! Utiliser un design pattern adéquat pour partager la même instance de `SessionFactory` dans les différentes classes de votre code lorsque nécessaire.

### II.5. Transaction BD déléguée à Hibernate

Il est maintenant temps de réaliser les requêtes en base de données en utilisant des méthodes ORM (Object-Relational Mapping) directement.

On pourra utiliser les méthodes `save()`, `update()`, `delete()` de la classe `Session` pour effectuer des opérations de modification sur les données persistées et les méthodes “queries” de la classe `Session` pour lister les données persistées.

Pour rappel, toute opération doit avoir lieu dans une transaction : on pourra démarrer cette transaction avec la méthode `beginTransaction()` de l'objet `Session`.

Pour que les opérations soient réellement effectuées, on devra également exécuter la transaction : on pourra utiliser la méthode `commit()` de l'objet `Transaction`, et la méthode `rollback()` en cas d'erreur.


# Partie III : Configurer Hibernate directement à travers Spring

Dans cette partie, nous allons utiliser Spring pour configurer Hibernate. Cela va nous permettre de demander à Spring d'auto-générer du code de la couche de transactions, afin d'éviter de réécrire des parties de code qui sont redondantes.

Décommenter dans le fichier `build.gradle` la ligne correspondant à `spring-orm`.

## III.1 Configuration d'Hibernate depuis un bean Spring

Le module spring-orm va nous permettre d'injecter la configuration d'Hibernate directement depuis un bean de configuration de Spring.

Pour cela, nous allons créer une nouvelle classe annotée `@Configuration`.

Cette annotation indique à Spring de créer une instance unique de cette classe, utilisée comme configuration et rattachée à l' `ApplicationContext`.

Un exemple de configuration pour hibernate est disponible dans le répertoire `resourcesEtudiants/SpringHibernateConfig.java`

On remarque notamment qu'une méthode `sessionFactory()` est annotée `@Bean`. Cette annotation indique à Spring de générer un singleton ayant le même nom que la méthode (`sessionFactory`) et de le rattacher à l' `ApplicationContext` .

Spring peut donc gérer pour nous la création et le cycle de vie de la `SessionFactory`, qui est désormais disponible comme Bean dans l' `ApplicationContext` .

Nous pouvons donc maintenant supprimer le fichier de configuration d'Hibernate : `src/main/resources/hibernate.cfg.xml`

## III.2 Déléguer la gestion des transactions à Spring

Spring intègre la gestion et la propagation des transactions au travers de ses composants (les transactions sont en principe définies dans la couche d'architecture dite de “Service” d'une application, mais ce n'est qu'une bonne pratique de modélisation et Spring n'impose aucune contrainte sur l'implémentation des transactions).

Il existe notamment une implémentation pour les transactions Hibernate :

```java
org.springframework.orm.hibernate3.HibernateTransactionManager
```

Une transaction est définie grâce à l'annotation `@Transaction` sur une méthode ou sur un composant (dans ce cas, toutes les méthodes sont par défaut transactionnelles).

Utiliser les transactions Spring pour simplifier la gestion des transactions dans le code.

Pour cela :

1. Configurer Spring en créant un bean `TransactionManager` en utilisant une implémentation `HibernateTransactionManager`.
   Voir la classe `SpringHibernateConfig.java` fournie pour un exemple de création de ce bean.
1. Créer un composant Spring qui va contenir le code métier exécuté dans les transactions :
  - Créer une nouvelle classe, lui ajouter l'annotation `@Component`
  - Créer des méthodes dédiées dans le nouveau composant Spring et refactorer le code existant pour déplacer le code métier des transactions (par exemple `currentSession.save(myEntity)` ) dans ces nouvelles méthodes.
  - Ajouter des annotations `@Transactional` lorsque nécessaire (sur les méthodes du composant, ou directement sur la classe)
1. A la place du code Hibernate réalisant la persistance des données au sein de transactions, appeler maintenant directement la nouvelle méthode du nouveau composant, sans se soucier de la création ou du commit de la transaction

**ATTENTION : Pour pouvoir utiliser le mode transactionnel de Spring, il faut utiliser le composant comme bean Spring et non pas comme un object Java standard ! (Voir Note sur l'injection de dépendances).**

## III.3 Séparation des couches

Utiliser l'injection de dépendances de Spring pour isoler la partie persistance de l'application dans des couches dédiées. En essaiera notamment d'utiliser une couche service pour la gestion des transactions et/ou la gestion de la persistance.

# Partie IV : Spring MVC et Spring Boot

## Spring Boot

Spring Boot est un framework étendant les différents composants Spring, pour faciliter grandement la configuration d'une application Spring en suivant des pratiques standardisés. Cela permet d'accélérer le développement et facilite la maintenance applicative.

Spring Boot est très majoritairement utilisé avec des “starters”, qui sont des regroupements de dépendances.

Dans la suite de ce projet, nous allons utiliser Spring Web MVC. Nous pourrions ajouter la dépendance spring-webmvc et la configurer, mais pour simplifier le développement nous utiliserons le starter Spring Boot Web.

Note : Spring Boot possède de nombreux starters offrant des fonctionnalités très poussées pour une application standard : par exemple, le `spring-boot-starter-data-jpa` permet d'auto-générer la couche DAO faisant le lien entre les contrôleurs et les entités à persister (mais en laissant très peu de liberté au développeur). Nous n'utiliserons pas ces autres starters dans ce projet : on se limitera au starter Web.

## Configuration de Spring MVC

1. Récupérer le fichier `resourcesEtudiant/build.gradle`. Ce fichier de build ajoute les plugins Spring Boot (et enlève les plugins précédents nécessaires au packaging) et remplace les dépendances de la partie I par le Spring Boot starter Web.
1. Attention : le déploiement précédent utilisait le packaging `war` pour créer le livrable et un plugin `getty` supplémentaire pour déployer l'application en test (`gradlew appRun`). Avec le nouveau plugin Spring Boot, tout est géré directement par le plugin. L'application sera maintenant lancée par la commande suivante : `gradlew bootRun`
1. Spring Boot propose une nouvelle annotation `@SpringBootApplication`:
   - Cette annotation permet de créer une application web Spring utilisant le pattern MVC en générant un `ApplicationContext` qui scanne le répertoire et sous-répertoires de la classe annotée `@SpringBootApplication`.
  - Il n'est donc plus nécessaire de générer et injecter nous-même le singleton `ApplicationContext` créé précédemment. On pourra à la place utiliser la classe `Application.java` fournie dans le répertoire `resourcesEtudiant/`. Cette classe scanne et affiche l'ensemble des beans enregistrés par Spring Boot au démarrage.
1. Spring Boot utilise des fichiers `application.properties` (fichier `property=value`) ou `application.yml` (fichier de propriétés en `yaml`) pour configurer l'ensemble de l'application. Cet usage est très pratique pour pouvoir définir différents fichiers de propriétés en fonction de l'environnement d'exécution (machine personnelle du développeur, environnement d'intégration continue, production, ...)
  - Déplacer le fichier `application.yml` dans le répertoire `src/main/resources/`
  - On pourra compléter ce fichier si nécessaire pendant le projet.

Maintenant que Spring Boot Web est configuré, notre application peut maintenant utiliser une architecture Modèle-Vue-Contrôleur.

## Composants Model

`Spring-mvc` impose très peu de restrictions sur les entités à utiliser comme modèle.

Une simple classe avec un constructeur public permettant d'initialiser les attributs de la classe suffit.

Note : les entités du modèle ne sont pas des composants à ajouter à Spring.

## Composants “view”

`Spring-mvc` fournit des librairies de tags pouvant être utilisées dans les vues `jsp`.

Nous allons utiliser les tags de formulaire Spring permettant d'utiliser la notion de `ModelAttribute`. Cela va nous permettre d'utiliser directement dans la vue une entité du modèle.

Pour cela on pourra utiliser les 2 `taglib` suivantes dans les vues possédant des formulaires :

```jsp
<%@ taglib prefix="spring" uri="http://www.springframework.org/tags"%>

<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
```

- Utiliser la nouvelle balise `<form:form>` qui contiendra des balises `<form:label>` et `<form:input>` pour générer les formulaires.
- La balise `<form:form>` possède un nouvel attribut `modelAttribute` qui référence le nom de l'entité à passer au controleur.
- Les balises `<form:label>` et `<form:input>` possèdent un attribut `path` qui référence le nom d'une propriété de l'entité à instancier.

Nous verrons dans la section contrôleur comment récupérer cet objet.

Par exemple, pour une classe :

```java
public class MyEntity {

    private String attributA;

    public MyEntity(String attributA) {
        this.attributA = attributA;
    }
}
```

On pourra utiliser le formulaire suivant :

```jsp
<form:form method="POST" action="/monAction" modelAttribute="myEntity">

<form:label path="attributA">Attribut A</form:label>

<form:input path="attributA" />

<input type="submit" value="Submit"></input>

</form:form>
```

Des templates de vues `jsp` sont fournies dans le répertoire `resourcesEtudiant/` .

Les vues doivent être placées dans un sous-répertoire de `src/main/webapp`, défini dans le fichier de propriétés `application.yml` (par exemple : `src/main/webapp/WEB-INF/views/` ).

## Composants “controller”

Nous allons maintenant créer la couche des contrôleurs du modèle MVC.

Pour cela, créer une nouvelle classe par contrôleur et annoter cette classe avec l'annotation Spring-mvc : `@Controller`

Spring gère les interactions du pattern MVC en utilisant une méthode par requête.

Pour chaque requête, créer une nouvelle méthode et l'annoter avec l'annotation `@RequestMapping`.

Cette annotation prend en paramètres le path de la requête et le verbe HTTP utilisé, par exemple :

```java
@RequestMapping(path = "/createMyEntity", method = {GET, POST})
```

Il existe de nombreuses manières de faire dialoguer le modèle avec la vue.

Nous allons principalement utiliser les paradigmes suivants :

- Récupérer des informations fournies dans une URL. Par exemple, pour récupérer la valeur `myValue` du paramètre `paramA` dans l'URL `/myUrl?paramA=myValue` on ajoutera à la méthode du contrôleur un paramètre avec l'annotation `@RequestParam` :

  ```java
  public Object myUrlMethod(@RequestParam String paramA) {
      [ ... ]
  }
  ```
- Récupérer l'instance de `ModelAttribute` générée dans le formulaire de la vue. On ajoutera un nouveau paramètre à la méthode du contrôleur avec l'annotation `@ModelAttribute` :

  ```java
  public Object myActionMethod(@ModelAttribute MyEntity myEntityInstance) {
      [ ... ]
  }
  ```
- Si nécessaire, on pourra aussi récupérer et mettre à jour directement le modèle complet généré dans la vue en ajoutant un paramètre de type `Model` ou `ModelMap` à la méthode du contrôleur. Par exemple :

  ```java
  public Object myActionMethod(ModelMap fullViewModel) {
      [ ... ]
  }
  ```
- Pour générer la vue `jsp` et lui injecter son modèle, on changera la méthode du contrôleur pour retourner une instance `ModelAndView` :

  ```java
  public ModelAndView myActionMethod() {
      ModelAndView result = new ModelAndView(“nameOfTheView”);
      result.addObject(“myInstance”, myEntityInstance);
      return result;
  } 
  ```

- On pourra ensuite récupérer l'objet `myInstance` injecté dans la vue JSP `nameOfTheView.jsp` en utilisant la syntaxe : `${myInstance}` .

- Note 1 : On utilise en principe un seul contrôleur pour gérer le dialogue entre l'ensemble des vues d'une entité du modèle. Par exemple, on pourra gérer le routage vers les vues `createMyEntity` et `showMyEntities` dans un contrôleur unique `EntityController` si celles-ci utilisent toutes le modèle `MyEntity`.
- Note 2 : `@Controller` étant une spécialisation de l'annotation `@Composant` de Spring, la classe annotée `@Controller` est donc un `Bean` injecté dans l' `ApplicationContext` de Spring. Cela signifie que nous pouvons maintenant utiliser toutes les fonctionnalités de Spring dans cette classe, par exemple des `@Autowired` sur les attributs de la classe.

# Partie V : Comptes utilisateurs

Dans cette partie, nous allons ajouter la gestion des utilisateurs.

Spring Boot fournit un starter permettant d'ajouter une gestion avancée de la sécurité. Notre besoin est ici limité, nous allons donc réaliser ces opérations directement dans le code.

## Création d'un compte utilisateur

Créer un formulaire permettant d'enregistrer un nouvel utilisateur. Le formulaire permet de fournir un login, un prénom, un nom d'utilisateur, un mot de passe et une adresse postale.

## Fonctionnalité de login

L'utilisateur doit être en mesure de se connecter sur le site en utilisant son login et son mot de passe. Une fois connecté, une vue dédiée permet d'afficher les informations de compte de l'utilisateur connecté.

L'utilisateur courant sera stocké dans un Cookie. La récupération et l'enregistrement de Cookies est possible en Spring en utilisant un filtre pendant le parcours de la requête. Un template est fourni dans le répertoire `resourcesEtudiant` : `CookieFilter.java`

## Pour aller plus loin

**[Partie optionnelle]** On pourra sécuriser l'accès aux fonctionnalités liées aux produits (création / édition / suppression / affichage) si l'utilisateur n'est pas connecté.

On pourra également ajouter un booléen à la création du compte utilisateur permettant la modification d'un produit. Si ce booléen est à faux, alors seul le listing des produits doit être possible une fois connecté.

Pour ces changements, on pourra utiliser `spring-security` et sécuriser le(s) contrôleur(s) lié(s) aux produits
