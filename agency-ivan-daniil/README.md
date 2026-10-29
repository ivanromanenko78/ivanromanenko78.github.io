# Ivan & Daniil studio prototype

Private design prototype requested by Ivan, using Lusion (https://lusion.co/) as the reference. The reference animation engine, CSS, temporary media and fonts are retained locally. Preserve third-party license headers. Portfolio imagery and the reel are explicitly labeled as temporary Lusion references and are not claimed as the agency's own work.

Agency copy follows TZ_Agency_Ivan_Daniil_v1(1).md (29 October 2026). Current display name is provisional. The €400 package is a draft offer; IVA and final terms remain to be confirmed.

## Structure

- `dist/index.html`: Portuguese landing page and content.
- `dist/studio.css`: agency adjustments and responsive video fallback.
- `dist/studio.js`: capability-aware entry, contact links and temporary video modal.
- `dist/engine/`: original scene engine and styling, with analytics removed and audio disabled.
- `dist/assets/`: temporary local media, WebGL models, textures and fonts.

No build or dependency installation is required. Site serves `dist/`.

## Verification

JavaScript syntax checked; browser verified desktop fallback, navigation, video dialog and 390px responsive viewport with no horizontal overflow. The QA browser has WebGL disabled, so the full 3D scene cannot be visually verified in this environment. Browsers with WebGL receive the original scene engine; browsers without it receive a responsive video fallback.

Next content pass: final brand name, own reel, own project images, final public contacts and package terms. Do not remove temporary-media attribution until those media have been replaced.

## Languages and GitHub Pages

PT: index.html; EN: en.html; RU: ru.html. Navigation preserves the project subdirectory. Resources are local and shared by all languages. Upload the complete dist directory contents to agency-ivan-daniil/ in ivanromanenko78.github.io. The engine directory avoids Jekyll underscore exclusions. No build is required.
