#!/usr/bin/env node
/**
 * Clima Guia: zero-dependency static SEO audit.
 * Run from any folder: node avac-portugal/tools/check-seo.mjs
 */
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = fileURLToPath(new URL('../', import.meta.url));
const prefix = '/avac-portugal/';
const origin = 'https://ivanromanenko78.github.io';
const sections = [
  '', 'guias/ar-condicionado/', 'guias/precos-instalacao/',
  'guias/bombas-de-calor/', 'guias/ventilacao/',
  'guias/split-multisplit-vrf/', 'guias/erros-instalacao/',
  'guias/manutencao-ar-condicionado/', 'guias/como-escolher-potencia/',
  'autoria-e-fontes/', 'recursos/checklist-orcamento/',
  'recursos/modelo-email-orcamento/', 'pesquisa/', 'politica-de-privacidade/'
];
const variants = [['pt-PT', ''], ['ru', 'ru/'], ['uk', 'uk/']];
const problems = [];
const match = (html, re) => html.match(re)?.[1] || '';
const fileFor = (slug) => path.join(root, slug, 'index.html');
const checkTarget = (href) => {
  const clean = href.split('#')[0].split('?')[0];
  if (!clean.startsWith(prefix)) return true;
  const slug = clean.slice(prefix.length);
  const local = path.join(root,slug);
  return fs.existsSync(local) && fs.statSync(local).isFile() ||
    fs.existsSync(path.join(local,'index.html'));
};
const expected = new Set();
for (const section of sections) {
  for (const [code, variant] of variants) {
    const slug = variant + section;
    const filename = fileFor(slug);
    const display = prefix + slug;
    expected.add(origin + display);
    if (!fs.existsSync(filename)) { problems.push('Missing: ' + display); continue; }
    const html = fs.readFileSync(filename, 'utf8');
    const canonical = match(html, /<link rel="canonical" href="([^"]+)"/);
    if (canonical !== origin + display) problems.push('Canonical: ' + display);
    const title = match(html, /<title>([^<]+)<\/title>/);
    const meta = match(html, /<meta name="description" content="([^"]+)"/);
    const lang = match(html, /<html lang="([^"]+)"/);
    if (!title || !meta || lang !== code) problems.push('Metadata: ' + display);
    if ((html.match(/<h1\b/g) || []).length !== 1) problems.push('H1: ' + display);
    if (/<meta[^>]+name="robots"[^>]+noindex/i.test(html)) problems.push('Noindex: ' + display);
    const alternates = [...html.matchAll(/<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"/g)];
    for (const [altCode, altPrefix] of [['pt-PT',''],['ru','ru/'],['uk','uk/'],['x-default','']]) {
      const expectedUrl = origin + prefix + altPrefix + section;
      if (!alternates.some(m => m[1] === altCode && m[2] === expectedUrl))
        problems.push('Hreflang ' + altCode + ': ' + display);
    }
    const ids = new Set([...html.matchAll(/\bid="([^"]+)"/g)].map(m => m[1]));
    for (const m of html.matchAll(/href="#([^"]+)"/g)) {
      if (!ids.has(m[1])) problems.push('Missing anchor #' + m[1] + ': ' + display);
    }
    for (const m of html.matchAll(/(?:href|src)="(\/avac-portugal\/[^"]+)"/g)) {
      if (!checkTarget(m[1])) problems.push('Broken local link ' + m[1] + ': ' + display);
    }
    for (const img of html.match(/<img\b[^>]*>/g) || []) {
      if (!img.includes(' alt=')) problems.push('Image without ALT: ' + display);
      if (!/\bwidth="/.test(img) || !/\bheight="/.test(img)) problems.push('Image without dimensions: ' + display);
    }
    for (const m of html.matchAll(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/g)) {
      try { JSON.parse(m[1]); } catch { problems.push('Invalid structured data: ' + display); }
    }
  }
}
const sitemap = fs.readFileSync(path.join(root, 'sitemap.xml'), 'utf8');
const listed = [...sitemap.matchAll(/<loc>([^<]+)<\/loc>/g)].map(m => m[1]);
for (const url of expected) if (!listed.includes(url)) problems.push('Missing sitemap URL: ' + url);
if (new Set(listed).size !== expected.size) problems.push('Unexpected sitemap count: ' + listed.length);
for (const [code] of variants) {
  if ((sitemap.match(new RegExp('hreflang="' + code + '"','g')) || []).length !== expected.size)
    problems.push('Sitemap alternate count for ' + code);
}
console.log('Clima Guia audit: ' + expected.size + ' pages, ' + variants.length + ' languages');
if (problems.length) {
  console.error('ERRORS (' + problems.length + '):\n' + problems.join('\n'));
  process.exitCode = 1;
} else {
  console.log('PASS — Canonical, language, metadata, sitemap, links, images and JSON-LD.');
}
