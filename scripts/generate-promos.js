#!/usr/bin/env node
/**
 * Generate track content files from track YAML definitions.
 *
 * For each course in src/content/promos/*.yaml:
 * - Creates src/content/docs/<slug>/index.md (landing page)
 * - Creates src/content/docs/<slug>/<chapter>.md (chapter page)
 *
 * Chapter content is copied from src/content/docs/courses/** and frontmatter adjusted.
 * YAML track files remain the single source of truth.
 *
 * Usage: node scripts/generate-promos.js [--dry-run]
 */

import fs from 'node:fs';
import path from 'node:path';
import { load as parseYaml } from 'js-yaml';

const DRY_RUN = process.argv.includes('--dry-run');
const PROMOS_SRC = 'src/content/promos';
const DOCS_DIR = 'src/content/docs';
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
  for (const [key, val] of Object.entries(fm)) {
    if (processed.has(key)) continue;
    if (typeof val === 'string') {
      out += `${key}: ${val}\n`;
    }
  }
  out += '---\n';
  return out;
}

function collectTrackSlugs() {
  const slugs = [];
  if (!fs.existsSync(PROMOS_SRC)) return slugs;
  for (const f of fs.readdirSync(PROMOS_SRC).filter(f => f.endsWith('.yaml'))) {
    const track = readTrackYaml(path.join(PROMOS_SRC, f));
    if (track.slug && Array.isArray(track.chapters)) {
      slugs.push(track.slug);
    }
  }
  return slugs;
}

function createIntermediateIndexes(dir) {
  // Find child dirs that are track containers (have subdirectories with index.md)
  const childDirs = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (!entry.isDirectory()) continue;
    childDirs.push(entry.name);
  }
  childDirs.sort();
  for (const name of childDirs) {
    const childDir = path.join(dir, name);
    const relPath = childDir.replace(DOCS_DIR + '/', '').replace(DOCS_DIR, '');
    // If this child already has an index.md, it's a track — skip
    if (fs.existsSync(path.join(childDir, 'index.md'))) continue;
    // Check if this child has subdirectories (tracks inside it)
    const subDirs = fs.readdirSync(childDir, { withFileTypes: true })
      .filter(e => e.isDirectory())
      .map(e => e.name)
      .sort();
    if (subDirs.length === 0) continue;
    // Create index.md for this container directory
    const parentName = name.replace(/[-_]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
    const links = subDirs.map(sd => {
      const sdIndex = path.join(childDir, sd, 'index.md');
      const sdTitle = fs.existsSync(sdIndex)
        ? (parseFrontmatter(fs.readFileSync(sdIndex, 'utf8')).frontmatter.title || sd)
        : sd;
      return `- [${sdTitle}](./${sd}/)`;
    }).join('\n');
    const body = `## ${parentName}\n\n${links}\n`;
    const fm = { title: parentName, type: 'cours', sidebar: { order: 1 } };
    fs.writeFileSync(path.join(childDir, 'index.md'), serializeFrontmatter(fm) + body, 'utf8');
    console.log(`  🏠 ${relPath}/index.md (intermediate)`);
    // Recurse into subdirs
    for (const sd of subDirs) {
      createIntermediateIndexes(path.join(childDir, sd));
    }
  }
}

function main() {
  console.log(`\n${DRY_RUN ? '🔍 DRY RUN' : '🚀'} Generating track content files\n`);
  
  if (!fs.existsSync(PROMOS_SRC)) {
    console.error('Promos source dir not found: ' + PROMOS_SRC);
    process.exit(1);
  }
  
  const trackFiles = fs.readdirSync(PROMOS_SRC).filter(f => f.endsWith('.yaml'));
  console.log(`Found ${trackFiles.length} track definitions.\n`);
  
  let totalChapters = 0;
  let errors = 0;
  
  for (const trackFile of trackFiles) {
    const track = readTrackYaml(path.join(PROMOS_SRC, trackFile));
    
    if (!track.slug || !Array.isArray(track.chapters) || track.chapters.length === 0) {
      console.warn(`  Skipping ${trackFile}: no slug or chapters`);
      errors++;
      continue;
    }
    
    const slug = track.slug;
    const trackDir = path.join(DOCS_DIR, slug);
    console.log(`  promo: ${slug}/ (${track.chapters.length} chapters)`);
    
    const chapters = [];
    for (let i = 0; i < track.chapters.length; i++) {
      const chapterSlug = track.chapters[i];
      const relPath = chapterSlug.startsWith('courses/') ? chapterSlug.slice(8) + '.md' : chapterSlug + '.md';
      const srcPath = path.join(DOCS_COURSES, relPath);
      
      let chapterName = chapterSlug.split('/').pop();
      if (!chapterName) chapterName = `chapitre-${i + 1}`;
      
      chapters.push({ slug: chapterSlug, name: chapterName, order: i + 1 });
      
      if (fs.existsSync(srcPath)) {
        const srcContent = fs.readFileSync(srcPath, 'utf8');
        const { frontmatter: srcFm, body } = parseFrontmatter(srcContent);
        
        const chapterFm = { ...srcFm };
        chapterFm.sidebar = { order: i + 1 };
        if (!chapterFm.title) {
          chapterFm.title = chapterName.replace(/[-_]/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
        }
        if (!chapterFm.description && chapterFm.title) chapterFm.description = chapterFm.title;
        
        const newContent = serializeFrontmatter(chapterFm) + body;
        const dstPath = path.join(trackDir, chapterName + '.md');
        
        if (!DRY_RUN) {
          fs.mkdirSync(path.dirname(dstPath), { recursive: true });
          fs.writeFileSync(dstPath, newContent, 'utf8');
        }
        console.log(`    ${chapterName}.md`);
      } else {
        console.warn(`    NOT FOUND: ${srcPath}`);
        errors++;
      }
    }
    
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
    console.log(`    index.md`);
    
    totalChapters += track.chapters.length;
  }
  
  // Create intermediate index pages for multi-level slugs
  if (!DRY_RUN && fs.existsSync(DOCS_DIR)) {
    const createdBefore = fs.readdirSync(DOCS_DIR, { withFileTypes: true }).filter(e => e.isDirectory()).length;
    createIntermediateIndexes(DOCS_DIR);
    const createdAfter = fs.readdirSync(DOCS_DIR, { withFileTypes: true }).filter(e => e.isDirectory()).length;
    if (createdAfter > 0) console.log(`\nIntermediate indexes: created for ${createdAfter - createdBefore} container directories`);
  }
  
  console.log(`\n${DRY_RUN ? 'DRY RUN' : 'Done.'}`);
  console.log(`Promos: ${trackFiles.length}`);
  console.log(`Chapters: ${totalChapters}`);
  if (errors) console.log(`Errors: ${errors}`);
}

main();
