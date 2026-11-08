# RavenXcope Product Brochure Workspace

## Current v20 candidate

v20 front and back are unapproved candidates; see `deliverables/v20/REVIEW.md`.




## Start here

Active candidates: [v20 review](deliverables/v20/REVIEW.md); editable front and back masters and proofs are in `deliverables/v20/option-a/`. Not print-ready.

Open the two `.pcraft` files in PhotoCraft. Build scripts, source assets, placement metadata and reviews are retained for editing and investigation; see [PhotoCraft workflow](PHOTOCRAFT_WORKFLOW.md) for prerequisites and safe rebuild instructions. A staged-files-only test on the local environment exported both masters and rebuilt the front with matching proof pixels; independent installation and fonts remain unverified. No LFS is required for the active masters.

`assets/` contains source and working assets; `deliverables/` contains the active masters and versioned reviews; `research/LEARNING.md` summarizes prior iterations; historical archives are not retained. Draft proof, visual reference PNGs and routine build logs are excluded from Git. `raven-edit-sendiri.png` remains tracked pending review.

Permissions for individual assets vary. Screenshot publication for the brochure does not automatically authorize redistribution of source files; assess all assets and references before making the repository public. No repository-wide asset license is implied.

## Historical learning

Prior iterations are summarized in `research/LEARNING.md`; their archives are no longer retained.

## Project

RavenXcope is a distributed NIDS focused on network alerts and asset criticality. The deliverable is an Indonesian-language, two-sided A5 portrait brochure for an exhibition. The demo CTA is https://demo.ravenxcope.mataelang.net. See `CONTENT_GUIDELINES.md` for the exact Indonesian source copy and `assets/product-documents/ravenxcope/knowledge-ravenxcope.md` for authoritative product facts.

The art direction is dark enterprise cybersecurity editorial, with restrained vermilion accents, authentic screenshots and editable layers. The `DEFENCE CENTER` label in screenshots is original UI, not the brochure category. Publication of supplied screenshots is authorized by the owner; this does not approve the design or print output.

## Documentation

- `AGENTS.md`: agent rules, authority, language and synchronization.
- `BRAND_GUIDELINES.md` and `DESIGN_RULES.md`: identity and visual rules.
- `CONTENT_GUIDELINES.md` and `BROCHURE_LAYOUT.md`: Indonesian copy and composition.
- `ASSET_MANIFEST.md`: asset inventory, provenance and permissions.
- `PHOTOCRAFT_WORKFLOW.md` and `PRINT_QA_CHECKLIST.md`: production workflow, review and approvals.
- `project.json`: structured project metadata.

## Assets and status

Official raster logos are in `assets/`; original screenshots are in `assets/ravenxcope/`. Create working copies in `assets/screenshots/ravenxcope/working/` as needed and keep reviewed processed versions in `approved/`. Other asset directories are reserved for architecture, additional brand masters, photography, contacts and printer specifications. An official vector master, validated architecture diagram and printer ICC specifications have not been supplied.

Prior iterations are summarized in `research/LEARNING.md`. Small UI labels and decorative-image resolution require physical-size review. QR must be retested digitally and physically. No verified print PDF or physical print proof has been completed. See `ASSET_MANIFEST.md`, `deliverables/v20/REVIEW.md`, and `PRINT_QA_CHECKLIST.md` for unresolved gates.
