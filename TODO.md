- https://code.juliancataldo.com/component/astro-terminal-player/
- https://code.juliancataldo.com/component/astro-seo-metadata/
- https://code.juliancataldo.com/component/astro-code-editor/

- https://github.com/sergioramos/remark-hint?tab=readme-ov-file
- https://github.com/remarkjs/remark-validate-links

- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- analytics
- Cours : liens outils et transverses => 2 cards
- "latest" page
- seo : https://github.com/hellotham/hello-astro/blob/main/src/components/seo.astro
- fix all unknown files at start
- RSS :     <link rel='alternate' type='application/rss+xml' title={SiteMetadata.title} href={`${Astro.site}rss.xml`} />
- merge "links" page (?) => "links" and "tools" idem ?


- promotions => https://docs.astro.build/en/guides/content-collections/#the-collection-config-file

- diagrams
  - Astro component : better loading (add yarn dep, …) instead of inline script
  - fix style : .flowchartTitleText
  - fix `katex` : loaded but nothing
  - fix `@startdot`

- slides in Astro ? (or Marp / Slidev ?)
  - fix v-clicks (auto -> slidev)

- theme :
  - PageFind results theme : https://pagefind.app/docs/ui-usage/
  - h2#chapitres => floating (right ?), always visible, collapsible
	- styles.css => !important ?
	- laserwave: 'laserwave', => neon violet
	- rose: 'rose-pine',
	- tokyonight: 'tokyo-night',
	- vesper: 'vesper', => mono orange

- Callouts (`:::`) : <https://github.com/Microflash/remark-callout-directives>
  - warning, exo, correction, strong, link

- "favorites" :
  - delete
	- fix favorites navigation (after astro hydration ?)

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

