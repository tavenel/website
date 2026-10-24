/**
 * Starlight plugin: transforms :::correction blocks into <details> elements.
 *
 * Usage:
 *   import { starlightCorrection } from './remark-plugins/remark-correction.mjs';
 *   ... starlight({ plugins: [starlightCorrection()] }) ...
 *
 * The :::correction content is processed as markdown by Starlight.
 * In a plain markdown viewer, the block shows as raw `:::correction` text.
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
                name: 'correction-block',
                containerDirective(node) {
                  if (node.name !== 'correction') return;
                  return h('details', { class: 'correction' }, [
                    h('summary', {}, [{ type: 'text', value: 'Correction' }]),
                    ...(node.children || []),
                  ]);
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