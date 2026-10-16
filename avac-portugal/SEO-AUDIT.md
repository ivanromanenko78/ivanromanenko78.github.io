# Clima Guia — Auditoria SEO e publicação
**Data:** 16 de outubro de 2026

## Estado verificado pelo código
- 42 páginas HTML previstas (14 em PT-PT, 14 em russo e 14 em ucraniano).
- Sitemap multilíngue `/avac-portugal/sitemap.xml`, com URLs canónicos e relações recíprocas `hreflang`.
- Títulos e metadescrições individuais, um H1 por página nos modelos atuais.
- Ligações internas: verificação de correspondência com ficheiros locais; guias PT com índice completo e âncoras funcionais.
- Imagens responsivas nas páginas iniciais (`srcset`, `sizes`, carregamento diferido), com alternativa SVG local caso falhe a imagem externa.
- Conteúdo sem testemunhos de clientes ou certificações inventadas.

## O que não foi possível comprovar nesta auditoria
- Velocidade real, Core Web Vitals, HTTP 200 de todas as URLs e acessibilidade visual em telemóveis reais.
- Visibilidade, impressões, cliques e cobertura no Google: são necessários os dados da Google Search Console.
- Os tempos e resultados de SEO não podem ser garantidos por alterações técnicas.

## Como executar verificação estática
```bash
node avac-portugal/tools/check-seo.mjs
```
Verifica metadados, links, `hreflang`, sitemap, alt/dimensões de imagens e dados estruturados; não substitui um crawler HTTP ou Lighthouse.

## Passo manual necessário — Google Search Console
1. Aceder a https://search.google.com/search-console.
2. Usar uma propriedade URL Prefix existente de `https://ivanromanenko78.github.io/` **se já estiver verificada**, ou criar a propriedade URL Prefix `https://ivanromanenko78.github.io/avac-portugal/` e concluir a verificação de propriedade.
3. Em **Indexação → Sitemaps**, enviar o URL completo: `https://ivanromanenko78.github.io/avac-portugal/sitemap.xml`.
4. Inspecionar as três páginas principais:
   - `https://ivanromanenko78.github.io/avac-portugal/`
   - `https://ivanromanenko78.github.io/avac-portugal/ru/`
   - `https://ivanromanenko78.github.io/avac-portugal/uk/`
5. Em **Resultados de pesquisa** e **Páginas**, acompanhar por país/idioma impressões, cliques, erros de indexação e páginas indexadas.
6. Testar URLs públicas no https://pagespeed.web.dev/ com vista móvel; registar LCP, INP, CLS e avisos.

Não alterar `/robots.txt` nem `/sitemap.xml` do portfólio existente na raiz sem autorização expressa, porque o projeto reside numa pasta independente.

## Próximos passos
- Criar domínio próprio `.pt` antes de apostar fortemente no SEO, para evitar migração depois.
- Fazer validação editorial das versões RU/UK e revisão dos dados legais por pessoa qualificada.
- Se as imagens externas afetarem os Core Web Vitals, descarregar e otimizar os ficheiros licenciados para distribuição a partir do domínio próprio.
- Rever os indicadores Search Console após 30, 60 e 90 dias; não confundir URLs descobertos com URLs indexados.
