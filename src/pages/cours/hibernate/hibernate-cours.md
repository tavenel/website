---
marp: true
paginate: true
#footer: _© 2024 Tom Avenel under 󰵫  BY-SA 4.0_
title: Hibernate
keywords:
- hibernate
---

![bg left:40% 80%](https://hibernate.org/images/hibernate-logo.svg)

# Persistence client-serveur : Object-relational mapping

## Hibernate

_Tom Avenel_

<https://www.avenel.pro/>

---

# Compétences à acquérir

- Définir et utiliser la persistance des données
- Traiter la conservation de l'état des applications d'une exécution à une autre

---

# Hibernate : un outil de mapping objet-relationnel

---

# Hibernate

Hibernate est une solution open source de type `ORM` (Object Relational Mapping) qui permet de faciliter le développement de la couche persistance d'une application.

**Hibernate permet donc de représenter une base de données en objets Java et vice versa** 

Ceci afin d’abstraire l’implémentation de la base de données du code (La plupart des BD sont supportées).

> The database is a detail (Robert Martin)

---

# Composants

```ditaa

+---------------------------------+
|           Application           |
+---------------------------------+
| Classes encapsulant les données |
+---------------------------------+    +---------------------+
| cBLU                            |<---| fichiers de mapping |
|                                 |    +---------------------+
|          Hibernate              |    +-----------------------------+
|                                 |<---| propriétés de configuration |
+---------------------------------+    +-----------------------------+
|{s}       Base de données        |
+---------------------------------+

```

---

# Persistent Objects

- Objets mono-threadés à vie courte
- Contenant :
  + Un état persistant
  + Du code métier
- Objets ordinaires (JavaBean, POJO)
- Associés avec une (et une seule) Session.
- Dès que la Session est fermée, ils sont détachés et libres d'être utilisés par n'importe quelle couche de l'application (par exemple de et vers la présentation).

---

# Persistent Objects

```ditaa

+--------------------------+
|       Application        |
|                          |
|   +==================+   |
+---|Persistent Objects|---+
|   +==================+   |
|                          |
|       Hibernate          |
|                          |
| +==========+ +=======+   |
| |hibernate.| |XML    |   |
| |properties| |Mapping|   |
| +==========+ +=======+   |
|                          |
+--------------------------+
|       Database           |
+--------------------------+

```

---

# Exemple de POJO 

```java
public class MyEntity {


    private Integer myId;
    private String myString;

    public Integer getMyId() {
        return myId;
    }

    public String getMyString() {
        return myString;
    }
```

---

# Architecture modulaire

![](https://docs.jboss.org/hibernate/orm/3.2/reference/fr/shared/images/lite.gif)

![](https://docs.jboss.org/hibernate/orm/3.2/reference/fr/shared/images/full_cream.gif)

_Architecture Hibernate. Source et crédits: <https://docs.jboss.org/hibernate/orm/3.2/reference/fr/html/architecture.html>_

---

# Session

- objet mono-threadé, à durée de vie courte
- représente une conversation entre l'application et l'entrepôt de persistance
- encapsule une connexion JDBC
- fabrique des objets Transaction
- la Session contient un cache (de premier niveau) des objets persistants, qui sont utilisés lors de la navigation dans le graphe d'objets ou lors de la récupération d'objets par leur identifiant.
 
---

# Unité de travail

- Séquences de requêtes à la BD pour effectuer une opération atomique dans l’application
  + => 1 session par opération métier, et pas 1 session par requête BD !
  + En web, souvent 1 session par requête
    * `SessionFactory.getCurrentSession()`
- Hibernate supporte aussi d’autres patterns beaucoup plus complexes
- Toute opération (lecture et/ou modification) doit avoir lieu dans une transaction

---

# SessionFactory

- Responsable du cycle de vie des sessions
- Objet complexe, coûteux et thread-safe
- Prévu pour n'être instancié qu'une seule fois via une instance Configuration en général au démarrage de l'application.

---

# Au contraire, la Session

- N'est pas coûteuse, non-threadsafe
- Ne devrait être utilisé qu'une seule fois pour une requête unique, une conversation, une unité de travail unique et devrait être relâché ensuite.

---

# Résumé

- La `SessionFactory` génère des `Session`
  + Par exemple : `SessionFactory.getCurrentSession()`
- Les `Session` modélisent une utilisation atomique de la base de données
  + Par exemple : recherche d’un produit et mise à jour d’un de ses champs
- Les `Session` génèrent des Transaction (obligatoires pour tout dialogue avec la BD)
  + Session.beginTransaction()
  + `Transaction.commit()`, `Transaction.rollback()`
 
---

# Configuration

Hibernate supporte de nombreux modes de configuration (programmatique, fichier `hibernate.properties`, fichier `hibernate.cfg.xml`, …)

Il est recommandé de :

- Configurer les propriétés générales (JDBC, …) dans un fichier hibernate.properties ou `hibernate.cfg.xml`
- Déclarer les classes d’objets à persister dans le fichier `hibernate.cfg.xml`
- Initialiser hibernate et ses fichiers de configuration lors de la génération de la `SessionFactory`

---

- `hibernate.properties` : principales propriétés JDBC
- `hibernate.connection.driver_class` => driver JDBC
- `hibernate.connection.url` => URL JDBC
- `hibernate.connection.username`
- `hibernate.connection.password`
- `hibernate.connection.pool_size` => nombre maximum de connexions dans un pool

---

Initialisation d’Hibernate et génération d’une `SessionFactory` classique :

```
new Configuration().configure().buildSessionFactory()
```

Hibernate fournit également de nombreuses possiblités d’intégration dans un serveur J2EE : réutilisation des connexions JDBC (par JNDI), binding JNDI et Java Transaction API (JTA) automatique, JMX déploiement, ...

---

# Classe de persistance

Les classes persistées par Hibernate sont des entitées décrites par des POJO (Plain Old Java Object) :

- Constructeur public sans paramètre
- Les attributs sont de type simple (int, float, String, Date, ...)
- Chaque attribut doit avoir un getter et un setter
- Penser à redéfinir les méthodes `equals()` et `hashCode()` pour éviter les mauvaises surprises
- Les POJO peuvent contenir des méthodes métier non utilisées par hibernate

---

# ORM

Bases du Mapping Objet-Relationel (ORM) :
- Les entitées persistées sont en principe enregistrées en BD selon un schéma très proche :
  + 1 table par entité
  + 1 colonne par attribut
- Les relations entre classe/table et attribut/colonne sont définies soit dans un fichier XML dédié `nomDeLaClasse.hbm.xml` dans le même package, soit par annotation dans la classe Java

---

# POJO à persister

```java
public class MyEntity {

    private Integer myId;
    private String myString;

    public Integer getMyId() {
        return myId;
    }

    public String getMyString() {
        return myString;
    }
```

---

# Exemple de mapping `MyEntity.hbm.xml`

```xml
<hibernate-mapping>
    <class name="MyEntity" table=”MY_ENTITY”>
        <id name="id">
            <generator class="native"/>
         </id>
         <property name="myString" type="string" not-null=”true” />
    </class>
</hibernate-mapping>
```

---

# Exemple d'annotation Java

```java
@Entity // il s’agit d’une classe à persister
@Table(name = "MY_ENTITY") // la table à utiliser en BD pour cette classe
public class MyEntity {


    private Integer myId;
    private String myString;
    @Id // @Id indique une clé primaire
    public Integer getMyId() {
        return myId;
    }

    @Basic(optional = false) // @Basic désigne un type simple (int, float, String, …) automatiquement mappé en BD pour une colonne par Hibernate.
    public String getMyString() {
        return myString;
    }
```

---

# Utilisation d’Hibernate ORM

- L’ORM permet de directement sauver / éditer / supprimer / lister les entités persistées sans avoir à écrire de requête SQL (ou à utiliser JDBC).
- L’objet Session possède un ensemble de méthodes (`save()`, `delete()`, `update()`, …) qui prennent directement un object en paramètre et réalisent le mapping et la persistance en BD
  + Exemple : `currentSession.save(myEntity)`

---

<!-- class: liens -->

# Références

- Tutoriel Hibernate de J.M.Doudoux : https://www.jmdoudoux.fr/java/dej/chap-hibernate.htm
- Architecture Hibernate : https://docs.jboss.org/hibernate/orm/3.5/reference/fr-FR/html/architecture.html
- Hibernate ORM mapping : https://docs.jboss.org/hibernate/orm/6.0/quickstart/html_single/ 

---

<!-- class: legal -->

# Legal

- Oracle and Java are registered trademarks of Oracle and/or its affiliates.
- Other names may be trademarks of their respective owners

---

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
