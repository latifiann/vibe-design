# AGENTS.md — RavenXcope Brochure Workspace

## Repository tracking

Track the current editable front and back masters, their proofs, required source assets, scripts and review metadata. Historical v01–v15 archives were removed; `research/LEARNING.md` records key lessons. Visual reference PNGs and routine build logs remain excluded by `.gitignore`. Update exceptions and documentation when the active candidate changes. Rebuild only in a disposable copy; staged-files-only front build was tested locally, but independent-machine reproducibility remains unverified. Keep active source assets and provenance intact.

## Current v16

Current front candidate is v16: four translucent supplied glass shells with icons above single-line editable labels. Back is the unchanged v09 design in `deliverables/v16/option-a/`. See `deliverables/v16/REVIEW.md`. Not print-ready.

## Historical learning

Prior iterations and provenance are summarized in `research/LEARNING.md`. Option A is the sole direction; institutional logos are front-only, in supplied order, without stretching.

## Mission and authority

Create and revise a professional B2B cybersecurity exhibition brochure: one A5 portrait sheet, front and back. Product: RavenXcope, a distributed NIDS focused on network alerts and asset criticality. Never use Corvus features as RavenXcope claims. The `DEFENCE CENTER` label in screenshots is original UI, not the brochure category.

Priority: latest explicit owner instructions; this file; `BRAND_GUIDELINES.md` and `DESIGN_RULES.md`; product knowledge and relevant content, layout, workflow and QA documents; agent aesthetic preferences. The authoritative product-fact source is `assets/product-documents/ravenxcope/knowledge-ravenxcope.md`. If an identity, product-accuracy or print-readiness conflict remains, stop and ask the owner.

## Languages and synchronization

- Internal documentation and descriptive metadata are in English. Conversation with the owner is in Indonesian. Brochure copy is in Indonesian; preserve the exact approved Indonesian text in `CONTENT_GUIDELINES.md`. Keep original UI labels, proper names, URLs and code identifiers unchanged.
- When product facts, assets, paths, layout, workflow, or approval status change, update affected documents and structured metadata in the same task. Check references and paths after moves or deletions. Maintain one authoritative source per subject; link to it instead of duplicating large passages.
- Report changed documents, missing assets, unverified claims and checks not performed. Publication permission for assets is not design approval or print approval.

## Non-negotiable rules

1. Generative decorative and conceptual assets may be proposed or produced as candidates and reviewed with the owner before approval. Record provenance, prompt and model when known, and review status; mark unknowns `[NEEDS CONFIRMATION]`. Do not generate or alter official logos or product screenshots, or invent UI, incident data, statistics, real topology, certifications or testimonials. Conceptual imagery is not evidence of product capability. Keep generated assets separate from editable text and layout; do not create a single flattened image containing the entire layout and text. Both options may use authentic screenshots; v07 B has no laptop.
2. Never recreate, trace, distort, recolor, decorate or otherwise modify the supplied logo. Use the owner-approved files unchanged; check effective print resolution.
3. Keep the orange-red/vermilion brand accent; do not substitute pure red, cyan or mint. Original screenshot UI colors remain unchanged.
4. Do not invent screenshots, incident data, topology, devices, certifications, statistics, testimonials or customer logos. Use only product claims in the current knowledge source or explicitly confirmed by the owner. Do not call it an IPS or promise automatic blocking.
5. Do not copy Fortra or ITSEC assets or layouts pixel-for-pixel. Preserve original source files; work on copies. Never flatten all layers before design approval.
6. Never send to a printer or claim print readiness before completing `PRINT_QA_CHECKLIST.md`, obtaining vendor specifications and approval, and reviewing a physical proof.

## Workflow

Before editing, inspect available files and assets; identify originals, placeholders, missing material, and any existing document dimensions, resolution, color mode and layer structure. Read relevant project guidance. Present a short plan covering sides, retained and added elements, and required assets. Mark unknown facts `[NEEDS CONFIRMATION]`; never guess.

During design, use editable text, vector shapes and separately named layers; use actual product screenshots, verified diagrams, and relevant owned or licensed photographs. Follow the grid, safe area, typography, brand color and approved copy. Screenshots currently supplied are authorized for publication, including visible data; review new assets separately. Do not treat captures from different times as one snapshot or alter their meaning.

After design, save versioned editable front and back masters and export proof PNGs. Inspect at 100% and simulated A5 print size. Review brand fidelity, NIDS claims and screenshot context, hierarchy and readability, QR destination and prepress criteria in `PRINT_QA_CHECKLIST.md`. Report critical, major and minor issues and outstanding approvals; do not redesign the whole brochure unless requested.

Suggested layer groups: `00_GUIDES_AND_BLEED`, `01_BACKGROUND`, `02_BRAND_MARK`, `03_HEADLINE_AND_COPY`, `04_HERO_PRODUCT_SCREENSHOT`, `05_TECHNICAL_DIAGRAM`, `06_GEOMETRIC_BRAND_ELEMENTS`, `07_FEATURES_AND_LABELS`, `08_QR_AND_CONTACT`, `09_FOOTER`. Do not merge editable text into backgrounds or screenshots.

Version examples: `ravenxcope-a5-front-v01.pcraft`, `ravenxcope-a5-back-v01.pcraft`, corresponding PNGs, and `ravenxcope-a5-proof-v01.pdf` only through a validated PDF workflow. Never overwrite an approved version; use a new version for major revisions.
