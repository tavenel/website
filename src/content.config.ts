import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { defineCollection, z } from 'astro:content';

// Starlight docs collection (courses + standalone pages — to be populated later)
const docs = defineCollection({
	loader: docsLoader(),
	schema: docsSchema({
		extend: z.object({
			/** Type de contenu : cours, tp, exo, projet, page */
			type: z.enum(['cours', 'tp', 'exo', 'projet', 'page']).optional(),
			/** Tags de catégorisation */
			tags: z.array(z.string()).optional(),
			/** Icône du cours (nom astro-icon) */
			icon: z.string().optional(),
		}),
	}),
});

// Tracks (chemins dédiés — curations de chapitres de cours)
const tracks = defineCollection({
	type: 'data',
	schema: z.object({
		title: z.string(),
		slug: z.string(),
		description: z.string().optional(),
		school: z.string().optional(),
		year: z.string().optional(),
		module: z.string().optional(),
		chapters: z.array(z.string()),
		roadmap: z
			.object({
				branches: z
					.array(
						z.object({
							from: z.string(),
							to: z.array(z.string()),
						})
					)
					.optional(),
			})
			.optional(),
	}),
});

export const collections = { docs, tracks };
