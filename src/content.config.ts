import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';
import { defineCollection, z } from 'astro:content';

// Starlight docs collection (courses + standalone pages + tracks)
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

export const collections = { docs };
