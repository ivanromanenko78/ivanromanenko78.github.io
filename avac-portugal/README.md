# Clima Guia — AVAC Portugal

Site editorial independente em português europeu sobre climatização, bombas de calor e ventilação.

## Publicação
- Projeto inteiramente isolado em `/avac-portugal/` dentro do repositório GitHub Pages.
- URL temporário: https://ivanromanenko78.github.io/avac-portugal/
- Alojamento: GitHub Pages do repositório existente. Pode migrar para Cloudflare Pages e domínio .pt posteriormente.
- Tecnologia: HTML, CSS e JavaScript estáticos. Sem dependências de build, sem base de dados.
- Não alterar a pasta `/magic-clima/`, outras páginas do portfólio ou ficheiros na raiz.

## Ficheiros
- `index.html`: página inicial.
- `styles.css`: design responsivo.
- `script.js`: menu móvel e calculadora indicativa de BTU.
- `guias/*/index.html`: páginas editoriais para SEO.
- `politica-de-privacidade/index.html`: informação básica de privacidade.
- `sitemap.xml`: mapa apenas deste projeto.
- `assets/*`: ilustração e favicon locais, sem imagens externas.

## SEO
Os URLs canónicos estão temporariamente definidos com a URL do GitHub Pages. Ao ligar um domínio próprio, atualizar os URLs canónicos, Open Graph, sitemap e os dados estruturados em **todos** os documentos. A estrutura de URLs deve manter-se quando possível. É possível submeter `https://ivanromanenko78.github.io/avac-portugal/sitemap.xml` na Search Console depois de verificar a propriedade.

## Personalização para venda
A marca editorial temporária é "Clima Guia". Antes de transformar o projeto num website empresarial, rever o posicionamento, a identidade, as páginas legais, os contactos e os conteúdos. Não publicar testemunhos, certificações ou instalações fictícias.

## Calculadora
Estimativa simplificada: 100 W/m² ajustados de forma grosseira ao isolamento e à exposição solar; convertidos para BTU/h e aproximados à capacidade comercial seguinte. Não representa um projeto técnico e não substitui o dimensionamento por profissional qualificado.

## Redesign visual (outubro de 2026)
- Página inicial renovada com sistema visual premium em `premium.css`, `premium.js` e `index.html`.
- Referências de design/código: [ZEPHYR](https://github.com/uiuxlabz/ac-repair-html-template) e [Astro Landing Page](https://github.com/mhyfritz/astro-landing-page), ambos MIT. O código desta integração foi implementado especificamente para Clima Guia, sem copiar componentes completos.
- Fotografias exibidas a partir do CDN Pexels, sob [licença Pexels](https://www.pexels.com/license/): IDs 6588599, 7614543, 20078063, 7587368, 6316065. Antes da venda, é preferível descarregar, otimizar e alojar os ficheiros localmente; conservar documentação de licença e autoria.
- O simulador de temperatura é ilustrativo e não controla nenhum equipamento.
- Não inclui avaliações de clientes, certificações, equipas ou serviços fictícios.

## Melhoria de conteúdo, outubro 2026
- 4 novos guias: comparação Split/Multi-split/VRF, dimensionamento, erros de instalação e manutenção.
- Conteúdo de referência e transparência editorial em /autoria-e-fontes/.
- Calculadora de potência heurística com volume, isolamento, insolação, ocupação, piso e uso da divisão; resultados são intervalo didático, não projeto de AVAC.
- Checklist imprimível e PDF autónomo em /recursos/checklist-orcamento/checklist-orcamento.pdf; modelo de email e pesquisa local de artigos.
- Novo percurso do utilizador na homepage, links cruzados e sitemap local atualizado.
- Informação técnica baseada em DECO, APA, DGEG e texto legislativo europeu, sem alegar certificação profissional.

## Traduções (outubro 2026)
O website tem três versões estáticas: português (original), russo em `/ru/` e ucraniano em `/uk/`. A navegação mantém a mesma página temática em cada idioma. O ficheiro `locale.css` apresenta o seletor PT/RU/UK. A script `localized.js` implementa calculadora, pesquisa, cópia do modelo e menu nos idiomas traduzidos. O sitemap inclui URLs alternativos com hreflang para as 14 páginas de cada idioma.
Os guias são adaptações editoriais em russo e ucraniano, mantendo notas de limitação do cálculo. Os PDFs atualmente disponíveis para download estão em português (PT); versões traduzidas da checklist podem ser impressas ou guardadas em PDF diretamente pelo navegador.
