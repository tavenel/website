// @ts-check
import { defineConfig, fontProviders } from "astro/config";

import icon from 'astro-icon';
import mermaid from 'astro-mermaid';
import starlight from '@astrojs/starlight';
import starlightImageZoom from 'starlight-image-zoom';
import starlightLinksValidator from 'starlight-links-validator';
import { visualizer } from "rollup-plugin-visualizer";

// import { remarkDiagram } from './remark-plugins/mermaid.mjs'; // Custom plugin -- Force loading Mermaid
// import { remarkModifiedTime } from './remark-plugins/modified-time.mjs'; // Custom plugin -- last time file was modified

// import rehypeExternalLinks from 'rehype-external-links';

// https://astro.build/config
export default defineConfig({
	site: 'https://www.avenel.pro',
	output: 'static',

	integrations: [
		icon(),
		mermaid({
			theme: 'neutral',
			autoTheme: true,
			mermaidConfig: {
				startOnLoad: false,
				logLevel: 'error',
				securityLevel: 'strict'
			}
		}), // ⚠️ Must come BEFORE starlight
		starlight({
			plugins: [
				starlightImageZoom(),
				starlightLinksValidator(),
			],
			title: 'avenel.pro',
			defaultLocale: 'fr',
			sidebar: [
				{ label: 'Cours 2026-2027', collapsed: true, items: [
					{ autogenerate: { directory: 'epsi' } },
					{ autogenerate: { directory: 'esgi' } },
					{ autogenerate: { directory: 'cesi' } },
					{ autogenerate: { directory: 'estiam' } },
				] },
				{ label: 'Tous les modules', collapsed: true, items: [{ autogenerate: { directory: 'courses' } }] },
				{ slug: 'other' },
				{ slug: 'tools' },
				{ label: 'Références et liens', link: '/liens/' },
				{ slug: 'website' },
				{ label: 'About me', link: '/about/', attrs: { style: 'font-style: italic' },},
			],
			social: [
        { icon: 'sourcehut', label: 'SourceHut', href: 'https://sr.ht/~toma' },
        { icon: 'gitlab', label: 'Gitlab', href: 'https://gitlab.com/tavenel' },
        { icon: 'github', label: 'Github', href: 'https://github.com/tavenel' },
        { icon: 'discord', label: 'Discord', href: 'https://astro.build/chat' }, // TODO
      ],
			disable404Route: false,
			components: {
				// Sidebar: '@components/Sidebar.astro',
				// Footer: '@components/StarlightFooter.astro',
			},
			customCss: [
				// 'src/styles/custom.css',
			],
		}),
	],

	vite: {
		plugins: [
			visualizer({ // analyse bundle size
				emitFile: true,
				filename: "stats.html",
			})
		]
	},

	fonts: [
		{
			name: "Inter",
			cssVariable: "--font-main",
			provider: fontProviders.fontsource(),
			// Download only font files for characters used on the page
			subsets: ["latin"],
		},
	],
})
