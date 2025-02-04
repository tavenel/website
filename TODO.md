## P1

- fix all unknown files at start
- slides in Astro ? (or Marp / Slidev ?)

- diagrams
  - Astro component : better loading (add yarn dep, …) instead of inline script
  - fix `katex` : loaded but nothing
  - fix `@startdot`

## P2

- fix v-clicks (auto -> slidev)
- "favorites" :
  - delete
	- fix favorites navigation (after astro hydration ?)

- styles :
  - cleanup CSS "TODO"
  - fix diagram style : .flowchartTitleText
  - PageFind results theme : https://pagefind.app/docs/ui-usage/
	- Callouts themes : https://github.com/Microflash/remark-callout-directives
  - Callouts => correction : svg in astro.config.mjs
  - h2#chapitres => floating (right ?), always visible, collapsible
	- styles.css => !important ?
	- laserwave: 'laserwave', => neon violet
	- rose: 'rose-pine',
	- tokyonight: 'tokyo-night',
	- vesper: 'vesper', => mono orange

- seo
	- https://github.com/hellotham/hello-astro/blob/main/src/components/seo.astro
	- https://code.juliancataldo.com/component/astro-seo-metadata/

## P3

- <h2>Chapitres</h2>
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- analytics
- Cours : liens outils et transverses => 2 cards
- "latest" page
  ```js
  fetch('https://example.com/feed.rss') // Replace with your RSS feed URL
  .then(response => response.text())
  .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
  .then(data => {
    const items = data.querySelectorAll("item");
    let html = "<ul>";
    items.forEach(item => {
      html += `<li><a href="${item.querySelector("link").textContent}">${item.querySelector("title").textContent}</a></li>`;
    });
    html += "</ul>";
    document.getElementById("rss-feed").innerHTML = html; // Replace "rss-feed" with the ID of your target element
  });
	```
- merge "links" page (?) => "links" and "tools" idem ?
- merge "liens" ?

- remark-lint
	- https://github.com/remarkjs/remark-validate-links

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

