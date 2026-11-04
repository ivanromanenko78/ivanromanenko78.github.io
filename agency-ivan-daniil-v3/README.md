# Ivan & Daniil — independent creative studio / variant 3

A separate multipage website at `/agency-ivan-daniil-v3/`. Existing variants remain in their original folders.

## Pages

33 fully rendered HTML pages: home, four service landing pages, contact, Journal index, three articles, and media/privacy credits, each in Portuguese, English and Russian. Main language is Portuguese; Russian starts at `ru/index.html`, English at `en/index.html`.

Content follows the project brief dated 29 October 2026: €400/month, 1 visit up to 2h, 2 videos up to 30s, 4 posts, 4 Stories, Portuguese copy, Instagram/Facebook publishing, one revision round, brief report. Advertising is separate. Counting of publications, VAT, travel, timelines and payment are confirmed in a written proposal. No invented clients, testimonials or performance claims.

## Editing

Edit `src/content.json`, then run `python3 src/build.py` from this directory. The dependency-free generator writes all locale pages and `sitemap.xml`. The website itself has no build or runtime dependencies; GitHub Pages serves the committed HTML. Shared CSS and JavaScript are in `assets/`.

## SEO

Unique titles and descriptions, canonical URLs, matching PT/EN/RU alternate links and x-default, one H1 per page, semantic heading structure, crawlable service/blog links, Organization/WebSite/WebPage/Service/BlogPosting/BreadcrumbList structured data, local social preview image, and a 33-URL sitemap. The root robots.txt additionally advertises the new sitemap. These provisions do not establish actual indexing or rankings; those need Search Console and subsequent monitoring.

## Media and licenses

Licensed visual references with scene-specific captions. Author and license links are retained on the credits page; the media are not presented as client case studies or team portraits.

- Mixkit: **Employee serving a cup of coffee from a machine**, asset 41860. Source: https://mixkit.co/free-stock-video/employee-serving-a-cup-of-coffee-from-a-machine-41860/ . The individual source page identifies commercial and personal use under the Mixkit Stock Video Free License: https://mixkit.co/license/#videoFree . Download used: https://assets.mixkit.co/videos/41860/41860-720.mp4 . Checked 2026-11-04.
- Pexels / **Amar Preciado**: **A Videographer Holding a Camera**, asset 7112246. Source: https://www.pexels.com/video/a-videographer-holding-a-camera-7112246/ . License: https://www.pexels.com/license/ . Source download resolved by Pexels: https://videos.pexels.com/video-files/7112246/7112246-hd_1080_1812_25fps.mp4 . Checked 2026-11-04.
- Motion demonstration, favicon and social preview are original code-generated graphics. Typeface uses the visitor's system Arial/Helvetica; no third-party font files.

Optimisation: H.264 MP4, CRF 28, no audio, 24 fps, fast-start metadata; coffee trimmed to 8 seconds at 1280px wide, camera at 480px wide. WebP posters, `preload=none`, source attachment only on viewport visibility or play click, pause when offscreen or the page is hidden. Save-Data and reduced-motion preferences disable automatic playback. Visible playback controls remain available.

## Contact and privacy

The contact form asks for required name and task plus an optional business field, then opens WhatsApp directly on submit with a prepared message. Valid service context is retained from landing-page links without adding another form field. The visitor confirms sending in WhatsApp; the website does not claim delivery. It has no backend storage. No trackers or advertising pixels. Hosting access logs and WhatsApp are covered by their respective providers.

## Validation

All 33 pages checked for internal asset links, fragment links, unique page titles, descriptions, canonicals, alternate-language links, single H1 and valid JSON-LD. JavaScript syntax checked with Node. Desktop and mobile PT/RU home layouts inspected in browser. Russian contact form and service preselection verified without sending a message. External source licenses checked. Video playback verified in browser.

## Contact and interaction update

- Short contact form in PT/EN/RU, native required-field validation, immediate WhatsApp handoff, no extra review step.
- Open Graph locale and image dimensions/type/alt, complete Twitter preview metadata, ContactPage and blog CollectionPage types.
- Button arrows, pressed states, article links, FAQ and form focus interactions. Reduced-motion preferences disable animation.
- Existing real publication dates retained; no invented testimonials or case studies.

Validation for this update: 12 contact-message checks across all three languages, including valid and invalid service contexts; all 33 pages checked for links, language alternates, JSON-LD and social metadata. Asset URLs use content hashes to avoid stale CSS/JavaScript after deployment.

Optional business context update: added a clearly optional business field and descriptive name/task placeholders in PT/EN/RU. Filled business context is included in the WhatsApp message; empty business values are omitted. No response-time promises were added.

## Approved monthly packages

Start €400: 1 shoot up to 2h, 2 videos up to 30s, 4 posts, 4 Stories. Business €800 (recommended): 1 shoot up to 4h, 4 videos, 8 posts, 8 Stories. Premium from €1,200: 2 shoots up to 3h each, 6 videos, 12 posts, 12 Stories. Video duration is up to 30 seconds in all packages. All include ideas, planning, editing, Portuguese copy, Instagram/Facebook publishing, one revision round and a brief monthly report. Videos are additional to posts; cross-posting does not double quantities. Advertising spend is separate and paid directly to Meta/Google; advertising setup and management are also quoted separately. Travel, timelines, payment and VAT are agreed before starting. Selected package is retained in the WhatsApp brief.

## Varied media update

Different assets are used for the homepage hero, café example, barbershop example, service pages and the three article covers. Current-article cards are excluded from related articles to avoid repeating their cover on the same page. Stock-source badges and stock wording have been removed from the main experience at the owner's request. Source and license documentation remains on the credits page and here.

New assets: Mixkit 44069 (film set), Mixkit 43241 (barber); Pexels photos 5081926 by cottonbro studio, 4164088 by The Lazy Artist Gallery, 11025648 by Amar Preciado, 12433033 by Hanna Pad, 14540964 by Alan Quirván. Individual source links are listed on the credits page. Mixkit pages state commercial use under the Free License; Pexels items are covered by the Pexels License. Video trims and compression retain the existing silent H.264/fast-start/lazy-load policy.
