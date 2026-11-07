# v16 — Four translucent foreground cards

Front A candidate, owner review pending. Current front master and proof: `option-a/ravenxcope-a5-front-a-v16.pcraft` and corresponding PNG. Files ending `v16-draft` are an earlier draft with tighter label padding, not current output. The back is the unchanged preserved v09 master and proof, copied to `option-a/ravenxcope-a5-back-a-v16.pcraft` and `option-a/ravenxcope-a5-back-a-v16.png`; this is not a newly designed v16 back.

## Composition

Four separate glass shell Smart Objects group conceptual raster icons above single-line editable labels: Analitik peringatan, Konteks aset, Prioritas risiko, Alur komunikasi IP. The latter two are candidate copy grounded in risk-matrix and IP-flow capabilities in the authoritative product knowledge. No new product claims or generated images. Upper cards cross screen edges; lower cards cross body/keyboard edges. Main dashboard title, central graph and donut remain visible; right shell crosses the far-right metric/panel edge. Transparency does not guarantee readability behind cards. Headline, main copy, laptop, screenshot, institutional badge and back were not redesigned.

## Asset preparation and limitations

New owner-supplied sources: `assets/generated/Cangkang kartu kaca asap transparan (1).png`, `assets/generated/Matriks prioritas risiko.png`, `assets/generated/Alur komunikasi IP premium.png`. Each is 1254 × 1254 RGBA with no embedded ICC or DPI. Original prompt/model and publication approval [NEEDS CONFIRMATION]. Sources unchanged. Crop records: `asset-preparation.json`; alpha values unmodified. Shell crop removes exterior margins including some very-low-alpha pixels; check for clipping of glow at physical size. Center alpha is about 30/255, not opaque; reflections are baked raster details, not dynamic blur/refraction. No opaque fill was added. Older icon provenance: `../../research/LEARNING.md`.

## Digital checks

After removal of the v01–v15 archives, a disposable copy containing the prospective tracked files was tested locally. Both masters exported with RGB pixels matching their proofs, and the front rebuilt with matching RGB pixels. The back was not regenerated. Fonts and independent-machine reproducibility remain unverified.

8 November 2026: the v09 back master and proof were copied unchanged into v16. Both active masters exported from a staged-files-only copy; RGB pixels matched their respective proofs. The v16 front rebuilt in that copy and matched its proof. The back was not rebuilt; `build_v16.py` builds only the front. A fresh digital QR decode could not be completed in this environment; earlier v09 checks do not replace a new test or a physical scan.

Reopened master: 1819 × 2551 px, 300 ppi. Re-export pixel-identical; proof embeds sRGB. Shells and icons remain Smart Objects; labels remain Type layers. Shell object bounds are 340 × 340 px, x=160 or 1320; all four and their labels lie inside approximate safe guides x=130–1689, y=130–2421. Label size is 7 pt; no wrapping. Labels are inside shell object bounds, but visible-rim padding is smaller and requires owner review. Source effective sampling: shell approximately 968 ppi, most icons 1875 ppi, IP-flow icon 1765 ppi. Sampling is not proof of optical quality.

Full draft composition inspected; final text bounds checked after a uniform adjustment from 7.5 to 7 pt. Native crop and reduced preview exported. Physical A5 text readability, low-alpha haze and glow edge clipping remain unverified. Four cards add visual density; owner review required. Screenshot perspective/mask/source proportions, explicit Bold Italic face and source color assumptions remain unresolved. No QR retest or physical scan, vendor specifications/ICC, validated print PDF, physical proof or design/print approval. Not print-ready.
