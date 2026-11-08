# PhotoCraft Workflow for Agentic Editing

## Current v20 candidate

v20 editing uses `deliverables/v20/edit_v20.py` and disposable source copies; independent rebuild not verified. Reopened masters yielded pixel-identical exports.




## Clean-checkout prerequisites and safety

The active front and back masters and their PNG proofs are tracked; historical masters and full-size proofs were removed. Source and working assets used by the current build, Python scripts, placement metadata and review records are retained. See `README.md` for exact active paths. Prior iteration lessons are in `research/LEARNING.md`.

The recorded production environment used PhotoCraft CLI 0.20.2. Font sources, licensing, and independent-machine reproducibility remain [NEEDS CONFIRMATION].

On 8 November 2026, a disposable copy made solely from the staged Git index was tested using the local environment. Both active masters converted successfully and their RGB pixels matched the tracked proofs. Rebuilding `--only a-front` in that copy also matched the front proof in RGB. CLI raster export warns that layers are flattened in PNG; the source masters remain layered. This is not an independent fresh-machine install, GUI edit test, font-availability audit, or back regeneration test. Output equivalence on another machine remains unverified.

Run `photocraft-cli --version` and verify required assets and fonts. Edit only disposable copies and write new versions; v20 source masters and historical builders were removed, so the v20 script cannot independently rebuild from them.


## Historical learning

See `research/LEARNING.md`; previous build scripts and masters are not retained.

## 1. Purpose

Use PhotoCraft as the editable image-composition and raster/vector editing environment for the Ravenxcope brochure. The agent must follow the design rules in this workspace; PhotoCraft's ability to execute commands does not authorize the agent to invent assets or redesign the brand.

Official repository:
https://github.com/storytold/photocraft

PhotoCraft describes an agent-ready workflow through its UI, CLI, JSON control channel, and MCP server. The repository documents commands such as `photocraft-cli run`, `photocraft-cli batch`, and `photocraft-cli mcp`. Exact command availability can change by version.

## 2. Verify the local installation first

Device audit, 7 November 2026: PhotoCraft GUI and CLI 0.20.2 were installed. A local MCP server handshake succeeded, but PhotoCraft MCP was not connected to OpenCode. CLI test document retained groups, editable type, shape and Smart Object after reopening, and exported a PNG. Both v01 masters reopened through CLI inspection with separate type, shapes and Smart Objects. GUI editing and print export remain untested.

Before automating:
1. Check the installed PhotoCraft version.
2. Check `photocraft-cli --help`.
3. Check `photocraft-cli run --help` and `photocraft-cli batch --help` if those subcommands are available.
4. Check the current MCP setup instructions for the installed build.
5. Do not assume command IDs, parameters, export options, or file-format support without checking the installed version.

Never invent a PhotoCraft command or MCP method.

## 3. Recommended agent workflow

1. Inspect the source document and assets.
2. Create a working copy.
3. Set up A5 canvas dimensions and resolution, including bleed.
4. Create separate front and back documents if two-sided page management is not reliably supported.
5. Establish background, guides, grid, and safe area.
6. Place the approved logo asset.
7. Add editable typography layers.
8. Place actual product screenshots and validated diagrams.
9. Add vector shapes and restrained brand geometry.
10. Save the editable master.
11. Export front/back proof images.
12. Review at 100% and at simulated A5 print size.
13. Only after approval, prepare final print output using a verified color/PDF workflow.

## 4. Layer discipline

Keep these groups separate:
- Guides and bleed
- Background
- Logo
- Headline and copy
- Product screenshot
- Technical diagram
- Geometric brand elements
- Feature labels
- QR and contact
- Footer

Use editable text layers where possible. Do not rasterize text prematurely.

## 5. File format strategy

- Preserve a native PhotoCraft project if supported by the installed version.
- Preserve a layered PSD master when interoperability is needed and verified.
- Keep exported PNG proofs for review.
- Use TIFF or another print-approved format only if requested by the printer.
- Do not assume PhotoCraft creates a compliant PDF/X-4 file. If a print-ready PDF is required, use a verified publishing/PDF workflow and inspect the exported file.
- Never label an export `print-ready` unless dimensions, bleed, resolution, color profile, and font handling have been checked.

## 6. Headless and attached operation

- Headless CLI/MCP is appropriate for repeatable operations, batch processing, export, and deterministic edits.
- Attached/UI control is appropriate when visual inspection, manual composition, typography adjustment, or review of the actual canvas is necessary.
- The agent may combine both, but it must inspect a rendered proof after significant layout changes.
- Do not trust command success alone as proof of visual quality.

## 7. Reference links

- Repository and README: https://github.com/storytold/photocraft
- Agent instructions in repository: https://github.com/storytold/photocraft/blob/main/AGENTS.md
- Read the current `docs/` in the installed/repository version for control protocol and CLI details.
