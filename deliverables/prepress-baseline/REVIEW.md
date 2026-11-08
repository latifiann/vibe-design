# General prepress baseline — review only

Status: historical baseline built from unapproved front v21 and back v24 candidates, now consolidated byte-for-byte into v25; not print-ready. No master was changed, no CMYK conversion made, and no file sent to a printer. Owner design approval remains pending. Current package: `deliverables/v25/REVIEW.md`.

## Baseline and review PDF

- `ravenxcope-a5-review-baseline.pdf` is a two-page raster review PDF: front, then back. It is not PDF/X and is not a production print file. It has no editable or embedded text fonts: each page is a single raster image with its embedded sRGB profile. Editable text remains in the original `.pcraft` masters.
- MediaBox and BleedBox are 154 × 216 mm; centered TrimBox is 148 × 210 mm, giving 3 mm per side. No crop marks or imposition. These are assumed boxes applied to the existing composition, not a verified original trim or vendor specification.
- Full canvas mapped to exact baseline dimensions, without changing source pixels: 1819 × 2551 px renders at approximately 300 ppi. Source physical dimensions at exactly 300 ppi are approximately 154.0087 × 215.9847 mm; mapping changes physical scale by less than 0.01% independently on each axis. No master or source image was resized. Check original trim/bleed coverage before production.
- `pdfinfo -box` confirmed two pages and intended boxes. `pdfimages -list` reported one ICC-based RGB 8-bit image per page at rounded 300 × 300 ppi. `pdffonts` reports none, as expected for raster pages. No PDF/X output intent or PDF/X validation is claimed.
- Rendered both pages at 300 ppi using Poppler. Result dimensions 1819 × 2552 reflect page-size pixel rounding. Chromium BarcodeDetector decoded the rendered back page to `https://demo.ravenxcope.mataelang.net`. Physical scan, PDF print-size scan and URL availability remain untested; a renderer may resample the artwork.
- Source proof PNGs had previously been compared pixel-for-pixel with fresh master exports. PDF rendering was not checked pixel-for-pixel against source due to scale, renderer and color-management differences. Visual fidelity, dark detail, gradients and bleed coverage remain unverified for this PDF.

## Assumptions and outstanding checks

- Safe margin target: 8 mm inside trim. Under this hypothetical trim, front LEN logo's bottom bound is approximately 8 mm inside trim; rounding, tolerance and real trim position leave no meaningful safety allowance. Owner/vendor review before any local adjustment.
- Recommended stock, not selected: 260 gsm art carton, matte lamination both sides. Actual stock, duplex orientation, vendor ICC, total ink limit, output PDF standard, marks and manufacturing tolerances remain unknown.
- Effective resolution and proportions of individually placed logos and screenshots remain unverified. Raster PDF's 300 ppi is page sampling, not proof of original placed asset resolution. Font availability in masters is unverified. QR quiet-zone adequacy, bleed coverage, actual A5 reading and physical QR scans remain open.
- Confirm candidate masters, design, shell and triage icon publication rights [NEEDS CONFIRMATION], proof and final print authorization. Validate production workflow, ICC/output intent, color, transparency, overprint and PDF/X with vendor. Review physical vendor proof before print release.

`build_review.py` builds this review PDF from the tracked proof PNG paths using Pillow; it refuses to overwrite an existing PDF. If proofs or masters change, repeat proof-to-master checks and all affected QA. PDF regeneration is not a substitute for vendor preflight.
