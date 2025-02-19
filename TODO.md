## P1

- slides => <bug> fullscreen style fix CSS</bug>
- jenkins/TP ~> MD
- TODOs in tableau-bord-cours
- TODOs in all files
- check robots.txt in prod

---

## P2

- picture => legend from _alt_ text
- slides => **bold** and _emphasis_
- slides => X/N slide number
- slidev => ::right::
- TPs => RM Legal
- slides => generate legal
- slides => marp => title, section, subtitle, lead
- slides => marp => color / backgroundColor
```md
# TITLE

_Tom Avenel_

<https://www.avenel.pro/>

---

# Legal

| [![󰵫  License: CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](http://creativecommons.org/licenses/by-sa/4.0/) | CC BY-SA 4.0 |
| ---------------------------------------------------------------- | ------------------------------------------ |
| ![BY](https://mirrors.creativecommons.org/presskit/icons/by.svg) | Attribution : vous devez créditer l'auteur |
| ![SA](https://mirrors.creativecommons.org/presskit/icons/sa.svg) | Partage dans les mêmes conditions          |

- Ce fichier est mis à disposition selon les termes de la Licence Creative Commons Attribution - Partage dans les Mêmes Conditions 4.0 International. Pour plus d'informations : <http://creativecommons.org/licenses/by-sa/4.0/>
- Le code source au format `Markdown` de ce document est disponible sur le [site web][site-perso]

[site-perso]: https://www.avenel.pro/
```

- diagrams
  - Astro component : better loading (add yarn dep, …) instead of inline script
  - fix `katex` : loaded but nothing
  - fix `@startdot`

## P3

- src/pages/todo/
- tags:[] in files and word cloud

- "favorites" :
  - link in Menu/
  - delete
  - fix favorites navigation (after astro hydration ?)

- styles :
  - cleanup CSS "TODO"
  - fix diagram style : .flowchartTitleText
  - PageFind results theme : https://pagefind.app/docs/ui-usage/
  - Callouts themes : https://github.com/Microflash/remark-callout-directives
  - Callouts => correction : svg in astro.config.mjs
  - h2#chapitres => floating (right ?<- only if @media landscape), always visible, collapsible
	- ability to zoom images
	- styles.css => !important ?
	- laserwave: 'laserwave', => neon violet
	- rose: 'rose-pine',
	- tokyonight: 'tokyo-night',
	- vesper: 'vesper', => mono orange

- seo
	- https://github.com/hellotham/hello-astro/blob/main/src/components/seo.astro
	- https://code.juliancataldo.com/component/astro-seo-metadata/

- linter `astro.config.mjs`
	- import remarkLint from 'remark-lint';
	- import remarkPresetLintRecommended from 'remark-preset-lint-recommended';
	- import remarkLintNoDeadUrls from 'remark-lint-no-dead-urls';
	- 		remarkPlugins: [
	- 			// remarkLint,
	- 			// remarkPresetLintRecommended,
	- 			// remarkLintNoDeadUrls,

## P4

- <h2>Chapitres</h2>
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- analytics
- Cours : liens outils et transverses => 2 cards
- https://adamsimpson.net/writing/openring
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

- test responsive slides with : https://github.com/sindresorhus/pageres
- https://github.com/astefanutti/decktape
- https://markdalgleish.com/projects/bespoke.js/
- https://github.com/gnab/remark/issues/50#issuecomment-223887379

---

https://docs.astro.build/en/guides/testing/

  yarn playwright test
    Runs the end-to-end tests.

  yarn playwright test --ui
    Starts the interactive UI mode.

  yarn playwright test --project=chromium
    Runs the tests only on Desktop Chrome.

  yarn playwright test example
    Runs the tests in a specific file.

  yarn playwright test --debug
    Runs the tests in debug mode.

  yarn playwright codegen
    Auto generate tests with Codegen.

We suggest that you begin by typing:

    yarn playwright test

And check out the following files:
  - ./tests/e2e/example.spec.ts - Example end-to-end test
  - ./tests-examples/demo-todo-app.spec.ts - Demo Todo App end-to-end tests
  - ./playwright.config.ts - Playwright Test configuration

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

