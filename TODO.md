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


```css
@font-face {
  font-family: "OpenMojiDemoFont";
  src: url("OpenMoji-color-glyf_colr_1.woff2") format("woff2");
  unicode-range: U+23,U+2A,U+2D,U+30-39,U+A9,U+AE,U+200D,U+203C,U+2049,U+20E3,U+2117,U+2120,U+2122,U+2139,U+2194-2199,U+21A9,U+21AA,U+229C,U+231A,U+231B,U+2328,U+23CF,U+23E9-23F3,U+23F8-23FE,U+24C2,U+25A1,U+25AA-25AE,U+25B6,U+25C0,U+25C9,U+25D0,U+25D1,U+25E7-25EA,U+25ED,U+25EE,U+25FB-25FE,U+2600-2605,U+260E,U+2611,U+2614,U+2615,U+2618,U+261D,U+2620,U+2622,U+2623,U+2626,U+262A,U+262E,U+262F,U+2638-263A,U+2640,U+2642,U+2648-2653,U+265F,U+2660,U+2663,U+2665,U+2666,U+2668,U+267B,U+267E,U+267F,U+2691-2697,U+2699,U+269B,U+269C,U+26A0,U+26A1,U+26A7,U+26AA,U+26AB,U+26B0,U+26B1,U+26BD,U+26BE,U+26C4,U+26C5,U+26C8,U+26CE,U+26CF,U+26D1,U+26D3,U+26D4,U+26E9,U+26EA,U+26F0-26F5,U+26F7-26FA,U+26FD,U+2702,U+2705,U+2708-270D,U+270F,U+2712,U+2714,U+2716,U+271D,U+2721,U+2728,U+2733,U+2734,U+2744,U+2747,U+274C,U+274E,U+2753-2755,U+2757,U+2763,U+2764,U+2795-2797,U+27A1,U+27B0,U+27BF,U+2934,U+2935,U+2B05-2B07,U+2B0C,U+2B0D,U+2B1B,U+2B1C,U+2B1F-2B24,U+2B2E,U+2B2F,U+2B50,U+2B55,U+2B58,U+2B8F,U+2BBA-2BBC,U+2BC3,U+2BC4,U+2BEA,U+2BEB,U+3030,U+303D,U+3297,U+3299,U+E000-E009,U+E010,U+E011,U+E040-E06D,U+E080-E0B4,U+E0C0-E0CC,U+E0FF-E10D,U+E140-E14A,U+E150-E157,U+E181-E189,U+E1C0-E1C4,U+E1C6-E1D9,U+E200-E216,U+E240-E269,U+E280-E283,U+E2C0-E2C4,U+E2C6-E2DA,U+E300-E303,U+E305-E30F,U+E312-E316,U+E318-E322,U+E324-E329,U+E32B,U+E340-E348,U+E380,U+E381,U+F000,U+F77A,U+F8FF,U+FE0F,U+1F004,U+1F0CF,U+1F10D-1F10F,U+1F12F,U+1F16D-1F171,U+1F17E,U+1F17F,U+1F18E,U+1F191-1F19A,U+1F1E6-1F1FF,U+1F201,U+1F202,U+1F21A,U+1F22F,U+1F232-1F23A,U+1F250,U+1F251,U+1F260-1F265,U+1F300-1F321,U+1F324-1F393,U+1F396,U+1F397,U+1F399-1F39B,U+1F39E-1F3F0,U+1F3F3-1F3F5,U+1F3F7-1F4FD,U+1F4FF-1F53D,U+1F549-1F54E,U+1F550-1F567,U+1F56F,U+1F570,U+1F573-1F57A,U+1F587,U+1F58A-1F58D,U+1F590,U+1F595,U+1F596,U+1F5A4,U+1F5A5,U+1F5A8,U+1F5B1,U+1F5B2,U+1F5BC,U+1F5C2-1F5C4,U+1F5D1-1F5D3,U+1F5DC-1F5DE,U+1F5E1,U+1F5E3,U+1F5E8,U+1F5EF,U+1F5F3,U+1F5FA-1F64F,U+1F680-1F6C5,U+1F6CB-1F6D2,U+1F6D5-1F6D7,U+1F6DC-1F6E5,U+1F6E9,U+1F6EB,U+1F6EC,U+1F6F0,U+1F6F3-1F6FC,U+1F7E0-1F7EB,U+1F7F0,U+1F90C-1F93A,U+1F93C-1F945,U+1F947-1F9FF,U+1FA70-1FA7C,U+1FA80-1FA88,U+1FA90-1FABD,U+1FABF-1FAC5,U+1FACE-1FADB,U+1FAE0-1FAE8,U+1FAF0-1FAF8,U+1FBC5-1FBC9,U+E0061-E0067,U+E0069,U+E006C-E0079,U+E007F;
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

