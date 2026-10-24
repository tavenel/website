/**
 * Starlight plugin: transforms custom directives in Starlight content.
 *
 * - :::correction → <details class="correction"><summary>Correction</summary>...</details>
 * - :::exo / :::exercice → <ol class="steps"><li>...</li></ol>
 *
 * Usage:
 *   import { starlightCorrection } from './remark-plugins/remark-correction.mjs';
 *   ... starlight({ plugins: [starlightCorrection()] }) ...
 */

function h(tag, attrs, children = []) {
  return {
    type: 'paragraph',
    data: {
      hName: tag,
      hProperties: attrs || {},
    },
    children,
  };
}

export function starlightCorrection() {
  return {
    name: 'starlight-correction',
    hooks: {
      'config:setup': ({ addIntegration }) => {
        addIntegration({
          name: 'starlight-correction-processor',
          hooks: {
            'astro:config:setup': ({ config }) => {
              const processor = config.markdown?.processor;
              if (!processor || !Array.isArray(processor.options?.mdastPlugins)) return;

              processor.options.mdastPlugins.push({
                name: 'custom-directives',
                containerDirective(node) {
                  if (node.name === 'correction') {
                    return h('details', { class: 'correction' }, [
                      h('summary', {}, [{ type: 'text', value: 'Correction' }]),
                      ...(node.children || []),
                    ]);
                  }
                  if (node.name === 'exo' || node.name === 'exercice') {
                    // Render as an ordered list with steps class (mimics Starlight's Steps component)
                    return h('ol', { class: 'steps' }, (node.children || []).map(c => h('li', {}, [c])));
                  }
                },
              });
            },
          },
        });
      },
    },
  };
}

/** Alias for backward compatibility */
export default starlightCorrection;