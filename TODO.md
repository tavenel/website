## P1

- dedicated font with UTF-8 emojis

- W3C

- slides => <bug> fullscreen style fix CSS</bug>

- slides KO from sub-courses (Linux index ~> .astro, lpic, …)

```css
.chapter .slide-mode.slide-elt:first-child {
/* Section */

padding-left: 3.5rem;
padding-right: 3.5rem;
padding-top: 2.5rem;
padding-bottom: 2.5rem;

h1 {
  display: flex;
  flex-direction: column;
  justify-content: center;
  font-size: 5rem;
  width: -moz-fit-content;
  width: fit-content;
  position: relative;
}
```

## P2

```css
main {
  /* max-width: 1024px; */ /* TODO (breaks line below and breaks slides) */
  max-width: 90vw; /* 90 % full page */
  margin: auto;
}
```

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
  - ability to zoom images
  - styles.css => !important ?
  - better light themes
  - selected text : `::selection` => color and backgroundColor at least

- seo
  - https://github.com/hellotham/hello-astro/blob/main/src/components/seo.astro
  - https://code.juliancataldo.com/component/astro-seo-metadata/

- linter `astro.config.mjs`
  - import remarkLint from 'remark-lint';
  - import remarkPresetLintRecommended from 'remark-preset-lint-recommended';
  - import remarkLintNoDeadUrls from 'remark-lint-no-dead-urls';
  - https://github.com/remarkjs/remark-validate-links
  - remarkPlugins: [ // remarkLint, // remarkPresetLintRecommended, // remarkLintNoDeadUrls, ]

## P4

- <whoami.avenel.pro>
- tsconfig.json :	"verbatimModuleSyntax": true,
- better `date:`
- Cours : liens outils et transverses => 2 cards
- "latest" page => git history ?
- <https://adamsimpson.net/writing/openring>

- test responsive slides with : https://github.com/sindresorhus/pageres
- https://github.com/astefanutti/decktape
- https://markdalgleish.com/projects/bespoke.js/
- https://github.com/gnab/remark/issues/50#issuecomment-223887379

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


