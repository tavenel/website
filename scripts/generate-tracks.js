#!/usr/bin/env node
/**
 * Generate track content files from track YAML definitions.
 *
 * For each track in src/content/tracks/*.yaml:
 * - Creates src/content/docs/tracks/<slug>/index.md (landing page)
 * - Creates src/content/docs/tracks/<slug>/<chapter>.md (chapter page)
 *
 * Chapter content is copied from src/content/docs/courses/** and frontmatter adjusted.
 * YAML track files remain the single source of truth.
 *
 * Usage: node scripts/generate-tracks.js [--dry-run]
 */

import fs from 'node:fs';
import path from 'node:path';
import { load as parseYaml } from 'js-yaml';

const DRY_RUN = process.argv.includes('--dry-run');
const TRACKS_DIR = 'src/content/tracks';
const DOCS_TRACKS = 'src/content/docs/tracks';
const DOCS_COURSES = 'src/content/docs/courses';

function readTrackYaml(trackPath) {
  const content = fs.readFileSync(trackPath, 'utf8');
  try {
    return parseYaml(content) || {};
  } catch (e) {
    console.error('  [PARSE ERROR]', trackPath, e.message);
    return {};
  }
}

function parseFrontmatter(content) {
  const match = content.match(/^---\s*\n([\s\S]*?)\n---\s*\n/);
  if (!match) return { frontmatter: {}, body: content };
  try {
    const fm = parseYaml(match[1]) || {};
    return { frontmatter: fm, body: content.slice(match[0].length) };
  } catch (e) {
    console.error('  [PARSE]', e.message);
    return { frontmatter: {}, body: content };
  }
}

function serializeFrontmatter(fm) {
  let out = '---\n';
  const orderedKeys = ['title', 'description', 'type', 'sidebar', 'tags', 'license', 'icon'];
  const processed = new Set();
  
  for (const key of orderedKeys) {
    if (fm[key] === undefined || fm[key] === null) continue;
    processed.add(key);
    if (key === 'sidebar' && typeof fm[key] === 'object') {
      out += 'sidebar:\n';
      for (const [sk, sv] of Object.entries(fm[key])) {
        out += `  ${sk}: ${sv}\n`;
      }
    } else if (key === 'tags' && Array.isArray(fm[key])) {
      out += 'tags:\n';
      for (const t of fm[key]) out += `- ${t}\n`;
    } else if (key === 'license' && Array.isArray(fm[key])) {
      out += 'license:\n';
      for (const l of fm[key]) out += `- ${l}\n`;
    } else if (typeof fm[key] === 'string' && /\n/.test(fm[key])) {
      out += `${key}: |\n`;
      for (const line of fm[key].split('\n')) out += `  ${line}\n`;
    } else if (typeof fm[key] === 'string') {
      const v = fm[key];
      if (/^[\-?:,\[\]{}&*!|>'"#]|: /.test(v) || v === '' || ['true','false','null','yes','no'].includes(v)) {
        out += `${key}: "${v.replace(/"/g, '\\"')}"\n`;
      } else {
        out += `${key}: ${v}\n`;
      }
    } else if (typeof fm[key] === 'boolean' || typeof fm[key] === 'number') {
      out += `${key}: ${fm[key]}\n`;
    }
  }
  // Any remaining keys
  for (const [key, val] of Object.entries(fm)) {
    if (processed.has(key)) continue;
    if (typeof val === 'string') {
      out += `${key}: ${val}\n`;
    }
  }
  out += '---\n';
  return out;
}

function main() {
  console.log(`\n${DRY_RUN ? '🔍 DRY RUN' : '🚀'} Generating track content files\n`);
  
  if (!fs.existsSync(TRACKS_DIR)) {
    console.error(`Tracks directory not found: ${TRACKS_DIR}`);
    process.exit(1);
  }
  
  // Clean existing tracks
  if (!DRY_RUN && fs.existsSync(DOCS_TRACKS)) {
    fs.rmSync(DOCS_TRACKS, { recursive: true });
  }
  
  const trackFiles = fs.readdirSync(TRACKS_DIR).filter(f => f.endsWith('.yaml'));
  console.log(`Found ${trackFiles.length} track definitions.\n`);
  
  let totalChapters = 0;
  let errors = 0;
  
  for (const trackFile of trackFiles) {
    const track = readTrackYaml(path.join(TRACKS_DIR, trackFile));
    
    if (!track.slug || !track.chapters || !Array.isArray(track.chapters) || track.chapters.length === 0) {
      console.warn(`  ⚠️  Skipping ${trackFile}: no slug or chapters`);
      errors++;
      continue;
    }
    
    const slug = track.slug;
    const trackDir = path.join(DOCS_TRACKS, slug);
    console.log(`📁 tracks/${slug}/ (${track.chapters.length} chapters)`);
    
    // Create track index.md
    const chapters = [];
    for (let i = 0; i < track.chapters.length; i++) {
      const chapterSlug = track.chapters[i];
      // chapterSlug is like "courses/linux/cours-hardware"
      const courseFile = chapterSlug + '.md';
      // Strip 'courses/' prefix if present (YAML chunks already include it)
      const relPath = chapterSlug.startsWith('courses/') ? chapterSlug.slice(8) + '.md' : chapterSlug + '.md';
      const srcPath = path.join(DOCS_COURSES, relPath);
      
      let chapterName = chapterSlug.split('/').pop();
      if (!chapterName) chapterName = `chapitre-${i + 1}`;
      
      chapters.push({ slug: chapterSlug, name: chapterName, order: i + 1 });
      
      // Create chapter file with content from courses/
      if (fs.existsSync(srcPath)) {
        const srcContent = fs.readFileSync(srcPath, 'utf8');
        const { frontmatter: srcFm, body } = parseFrontmatter(srcContent);
        
        // Build chapter frontmatter
        const chapterFm = { ...srcFm };
        // Remove course-specific sidebar (track provides its own)
        chapterFm.sidebar = { order: i + 1 };
        // Ensure title
        if (!chapterFm.title) {
          chapterFm.title = chapterName.replace(/[-_]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        }
        // Add description if missing
        if (!chapterFm.description && chapterFm.title) {
          chapterFm.description = chapterFm.title;
        }
        
        const newContent = serializeFrontmatter(chapterFm) + body;
        const dstPath = path.join(trackDir, chapterName + '.md');
        
        if (!DRY_RUN) {
          fs.mkdirSync(path.dirname(dstPath), { recursive: true });
          fs.writeFileSync(dstPath, newContent, 'utf8');
        }
        console.log(`  📄 ${chapterName}.md (source: ${chapterSlug})`);
      } else {
        console.warn(`  ⚠️  Chapter not found: ${srcPath}`);
        errors++;
      }
    }
    
    // Create index.md for the track
    const indexFm = {
      title: track.title || slug.split('/').pop() || 'Track',
      description: track.description || `Track ${track.title}`,
      type: 'cours',
      sidebar: { order: 1 },
      icon: 'book',
    };
    
    const chapterLinks = chapters.map(c => `- [${c.name}](./${c.name})`).join('\n');
    const indexBody = `${track.description || ''}\n\n## Chapitres\n\n${chapterLinks}\n`;
    const indexContent = serializeFrontmatter(indexFm) + indexBody;
    const indexPath = path.join(trackDir, 'index.md');
    
    if (!DRY_RUN) {
      fs.mkdirSync(path.dirname(indexPath), { recursive: true });
      fs.writeFileSync(indexPath, indexContent, 'utf8');
    }
    console.log(`  🏠 index.md`);
    
    totalChapters += track.chapters.length;
  }
  
  console.log(`\n${DRY_RUN ? '🔍 DRY RUN' : '✅'} Complete.`);
  console.log(`Tracks: ${trackFiles.length}`);
  console.log(`Chapters: ${totalChapters}`);
  if (errors) console.log(`Errors: ${errors}`);
}

main();