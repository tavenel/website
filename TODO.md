-> PDFs
https://github.com/inokawa/remark-docx
https://github.com/remcohaszing/rehype-mermaid
https://github.com/akebifiky/remark-simple-plantuml
https://github.com/inokawa/remark-pdf

https://github.com/sergioramos/remark-hint?tab=readme-ov-file

https://github.com/remarkjs/remark-validate-links

-> use <Picture /> <https://docs.astro.build/en/guides/images/#images-in-astro-files> for covers
-> Marp (or all in slidev ?)
-> astro markdown => mermaid, plantuml, …
-> astro : icon-link (h1, …) only on hover
-> astro : fix ALL image imports => use MDX in promotions/
-> fix ::: (corrections, …)
-> better `date:`
-> C-k shortcut => launch search
-> Copyright 2025
-> "Fun"
-> promotions/

---

-> How-to upgrade Astro : `npx @astrojs/upgrade`

https://github.com/rehypejs/rehype/blob/HEAD/doc/plugins.md#list-of-plugins
https://github.com/remarkjs/remark/blob/main/doc/plugins.md#list-of-plugins

---

# Java

Latest Java versions (> 17) introduced :

- `Records`
- `Sealed` classes
- `switch` instructions with patterns

Examples below :

```java
package java17;

public class RecordsAndSealedClasses {

    record MyRecord(int x) implements MySealedClass {

        MyRecord() {
            this(42); // must call canonical constructor
        }

        MyRecord {
            // canonical constructor
            assert x > 0;
        }
    }

    sealed interface MySealedClass
    permits MyRecord, SealedSubclass, UnsealedClass
    {}

    sealed static class SealedSubclass
        implements MySealedClass
        permits MyFinalClass
    {}

    non-sealed static class UnsealedClass
        implements MySealedClass
    {}

    static final class MyFinalClass
        extends SealedSubclass
    {}

}
```

```java
package java17;

import java17.RecordsAndSealedClasses.*;

import java.util.List;
import java.util.Random;

public class SwitchWithPattern {

    static String test(MySealedClass instance) {

        return switch (instance) {
            case null -> "NULL";
            case MyFinalClass __ -> "FinalClass";
            case SealedSubclass __ -> "SealedSubclass";
            case UnsealedClass __ -> "UnsealedClass";
            case MyRecord record && record.x() == 42 -> "Default Record";
            // JDK18 ? case MyRecord(43) -> "Record with 43";
            case MyRecord record -> "Another Record with : " + record.x();
        };
    }

    public static void main(String[] args) {
        var instances = List.of(
                new MyFinalClass(),
                new SealedSubclass(),
                new UnsealedClass(),
                new MyRecord(),
                new MyRecord(11),
                new MyRecord(43)
                // NPE in List.of null
        );
        var rand = new Random().nextInt(instances.size());
        System.out.println(
                SwitchWithPattern.test(instances.get(rand))
        );
    }
}
```

