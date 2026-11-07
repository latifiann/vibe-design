# RavenXcope brochure iteration learning

Historical v01–v15 files were removed from the working tree in favor of this summary. This is a learning record, not proof of design or print approval. Current masters and QA are in `deliverables/v16/`.

## Iterations and decisions

- v01–v03 explored separate front/back and front-only compositions with authentic screenshot crops. Crops can cut UI cards or render fine labels too small at A5. GUI and headless CLI were both explored; CLI versions and permissions matter.
- v04 compared two complete concepts with editable text, vector feature illustrations and owner-supplied decorative imagery. Keep screenshots, decoration and text separate. Background sampling near 165 ppi and unprofiled sources need print review.
- v05 added an owner-supplied decorative laptop and a separate screenshot to option A. The laptop is conceptual, not evidence of an actual device. Its working cutout uses a non-generative aperture/alpha operation; original retained.
- v06–v08 iterated on full authentic screenshot placement and laptop composition. Option B used no laptop in v07. Do not combine captures from different times into one implied snapshot; screenshot perspective, mask, proportions and UI legibility require inspection.
- v09: owner chose option A for further iteration, not print approval. Six institutional logos were placed unchanged on the front only, in supplied order. Original row breached the approximate bottom safe area; small logo lettering and optical balance require physical review. Back v09 is the unchanged design now saved as the v16 back. Editable text bounds passed approximate guides, but that did not include the front logo objects. QR decoded digitally to `https://demo.ravenxcope.mataelang.net` at the time; physical scanning remained open.
- v10–v12 studied inset badges; v12 replaced glass with an opaque white badge and increased logo padding. Font selection, logo legibility, safe margins, screenshot fidelity and overlap still needed review.
- v13 introduced two owner-supplied conceptual icons as separate Smart Objects and editable labels; the revised study corrected overlaps. Working copies used alpha >8 bounds plus 25 px padding; no alpha cleanup. Original prompt/model and publication approval [NEEDS CONFIRMATION], no embedded ICC, color interpretation unverified.
- v14 moved separate foreground icons across the screen edges. v15 grouped icons and editable labels in graphite cards. Both trades increase density and risk obscuring dashboard details; check legibility at physical size, not only layer bounds.

## Retained asset provenance

- `assets/generated/Lensa inspeksi dan penanda peringatan.png` and `assets/generated/Tiga pelat inventaris grafit beraksen merah.png`: owner-supplied conceptual v13 icon sources; their working copies are `assets/generated/working/alert-analysis-v13.png` and `assets/generated/working/asset-context-v13.png` respectively. Original prompt/model, publication approval and ICC interpretation [NEEDS CONFIRMATION]. Candidates are not approved evidence of product capability.
- Owner authorized supplied product screenshots and visible data for brochure publication; repository-wide redistribution permission remains [NEEDS CONFIRMATION]. Preserve source UI and context. Brand logos must remain unchanged.
- Owner authorized the supplied conceptual hero backgrounds for the earlier comparison, not final design or print approval. Laptop source is owner supplied; permission and color assumptions remain subject to current asset review.
- Current v16 glass shell, risk and IP-flow candidate provenance and crop records: `deliverables/v16/REVIEW.md` and `deliverables/v16/asset-preparation.json`. Prompt/model and publication approval [NEEDS CONFIRMATION].

## Workflow and unresolved gates

Keep editable type, vector shapes and Smart Objects in separate layers; flattened PNG is a proof, not the master. A successful missing-font check does not establish the intended Bold Italic face. Inspect masks, safe margins, color assumptions and effective resolution; compare at 100% and simulated A5. Digital QR decoding does not replace a physical scan. No validated print PDF, printer specifications/ICC, physical proof, design approval or print approval has been established. Follow `PRINT_QA_CHECKLIST.md`; do not send to printer.
