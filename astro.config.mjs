// @ts-check
import { defineConfig, fontProviders } from "astro/config";

import icon from 'astro-icon';
import mermaid from 'astro-mermaid';
import starlight from '@astrojs/starlight';
import starlightFullViewMode from 'starlight-fullview-mode';
import starlightImageZoom from 'starlight-image-zoom';
import starlightLinksValidator from 'starlight-links-validator';
import { visualizer } from "rollup-plugin-visualizer";
import { starlightCorrection } from './remark-plugins/remark-correction.mjs';

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
				starlightFullViewMode(),
				starlightImageZoom(),
				starlightLinksValidator({
					errorOnLocalLinks: false, // skip localhost or 127.0.0.1
					failOnError: false,
				}),
				starlightCorrection(),
			],
			title: 'avenel.pro',
			description: 'Tom Avenel personal website. Tech articles and teachings.',
			editLink: {
				baseUrl: 'https://github.com/tavenel/website/edit/main/', // 'https://gitlab.com/tavenel/website/-/edit/main/',
			},
			lastUpdated: true, // show "last updated: " in footer
			components: {
				Sidebar: '@components/SidebarWithFilter.astro',
				Footer: '@components/LicenseFooter.astro',
			},
			customCss: [
				'src/styles/custom.css',
			],
			sidebar: [
				{ label: 'Cours 2026-2027', collapsed: true, items: [
					{ autogenerate: { directory: 'epsi', collapsed: true } },
					{ autogenerate: { directory: 'esgi', collapsed: true } },
					{ autogenerate: { directory: 'cesi', collapsed: true } },
					{ autogenerate: { directory: 'estiam', collapsed: true } },
				] },
				{ label: 'Tous les supports', collapsed: true, items: [{ autogenerate: { directory: 'courses', collapsed: true } }] },
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
