## P1

- slides => <bug> fullscreen style fix CSS</bug>
- check robots.txt in prod

- vercel analytics
- https://vercel.com/tavenels-projects/website/speed-insights

- slides KO from sub-courses (Linux index ~> .astro, lpic, …)

---

## P2

```css
main {
	/* max-width: 1024px; */ /* TODO (breaks line below and breaks slides) */
	max-width: 90vw; /* 90 % full page */
	margin: auto;
}
```

- 404 style

- diagrams
  - mermaid => render images at build time with playwright : <https://agramont.net/blog/diagraming-with-mermaidjs-astro/>
  - fix `@startdot`
```css
	@media (prefers-color-scheme: dark) {
  .kroki svg {
    filter: invert(100%);
  }
}
```

- Head.astro => ClientRouter transitions
- JS slide => <https://www.geeksforgeeks.org/simple-swipe-with-vanilla-javascript/>
- slides => X/N slide number
- slidev => ::right::
- slidev => layout image-right
- TPs => RM Legal and generate it
- slides => generate legal
- slides => marp => color / backgroundColor
- marp => class: liens
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

## P3

- tags:[] in files and word cloud

- "favorites" :
  - link in Menu/
  - delete
  - fix favorites navigation (after astro hydration ?)
  - Favorites.astro => fix TODO

- styles :
  - cleanup CSS "TODO"
  - fix diagram style : .flowchartTitleText
	- slides => **bold** and _emphasis_
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

- <whoami.avenel.pro>
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

- move HTML emojis to web icons

---

```css
/******************************************************************************/
/*                                    TODO                                    */
/******************************************************************************/



 /* .pagefind-ui { */
 /*    --pagefind-ui-scale: 0.75; */
 /*    --pagefind-ui-primary: navy; */
 /*    --pagefind-ui-text: black; */
 /*    --pagefind-ui-border: slategrey; */
 /*    --pagefind-ui-border-width: 1px; */
 /*    --pagefind-ui-border-radius: 0.25rem; */
 /*    --pagefind-ui-font: sans-serif; */
 /**/
 /*    width: 50%; */
 /*  } */

body.dark {
  --pagefind-ui-primary: #eeeeee;
  --pagefind-ui-text: #eeeeee;
  --pagefind-ui-background: #152028;
  --pagefind-ui-border: #152028;
  --pagefind-ui-tag: #152028;
}

 /* .pagefind-ui .pagefind-ui__drawer:not(.pagefind-ui__hidden) { */
 /*    position: absolute; */
 /*    left: 0; */
 /*    right: 0; */
 /*    margin-top: 0px; */
 /*    z-index: 9999; */
 /*    padding: 0 2em 1em; */
 /*    overflow-y: auto; */
 /*    box-shadow: */
 /*      0 10px 10px -5px rgba(0, 0, 0, 0.2), */
 /*      0 2px 2px 0 rgba(0, 0, 0, 0.1); */
 /*    border-bottom-right-radius: var(--pagefind-ui-border-radius); */
 /*    border-bottom-left-radius: var(--pagefind-ui-border-radius); */
 /*    background-color: var(--pagefind-ui-background); */
 /*  } */
 /**/
 /*  .pagefind-ui .pagefind-ui__result-link { */
 /*    color: var(--pagefind-ui-primary); */
 /* color: yellow; */
 /*  } */
 /**/
 /*  .pagefind-ui .pagefind-ui__result-excerpt { */
 /*    color: var(--pagefind-ui-text); */
 /* color: red; */
 /*  } */


.material-symbols-light--dark-mode {
  display: inline-block;
  width: 24px;
  height: 24px;
  --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M12.058 20q-3.334 0-5.667-2.333T4.058 12q0-3.039 1.98-5.27t4.904-2.634q.081 0 .159.006t.153.017q-.506.706-.801 1.57T10.158 7.5q0 2.667 1.866 4.533t4.534 1.867q.951 0 1.813-.295t1.548-.801q.012.075.017.153t.006.159q-.384 2.923-2.615 4.903T12.057 20'/%3E%3C/svg%3E");
  background-color: currentColor;
  -webkit-mask-image: var(--svg);
  mask-image: var(--svg);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
}

.material-symbols-light--dark-mode-outline {
  display: inline-block;
  width: 24px;
  height: 24px;
  --svg: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23000' d='M12.058 20q-3.334 0-5.667-2.333T4.058 12q0-3.039 1.98-5.27t4.904-2.634q.081 0 .159.006t.153.017q-.506.706-.801 1.57T10.158 7.5q0 2.667 1.866 4.533t4.534 1.867q.951 0 1.813-.295t1.548-.801q.012.075.017.153t.006.159q-.384 2.923-2.615 4.903T12.057 20m0-1q2.2 0 3.95-1.213t2.55-3.162q-.5.125-1 .2t-1 .075q-3.074 0-5.237-2.162T9.158 7.5q0-.5.075-1t.2-1q-1.95.8-3.163 2.55T5.058 12q0 2.9 2.05 4.95t4.95 2.05m-.25-6.75'/%3E%3C/svg%3E");
  background-color: currentColor;
  -webkit-mask-image: var(--svg);
  mask-image: var(--svg);
  -webkit-mask-repeat: no-repeat;
  mask-repeat: no-repeat;
  -webkit-mask-size: 100% 100%;
  mask-size: 100% 100%;
}
```

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

