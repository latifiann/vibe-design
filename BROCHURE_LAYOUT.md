# RavenXcope A5 Two-Sided Brochure Layout

## Current v16

v16 places two glass cards across screen edges and two across body/keyboard edges, icons above single-line labels. All shells square, 7 pt labels. Primary graph/donut remain visible; right shell crosses the far-right dashboard edge. Review: `deliverables/v16/REVIEW.md`.

## Historical learning

Prior iterations and limitations are summarized in `research/LEARNING.md`.

## Initial specification

One unfolded portrait sheet, front and back. Trim: 148 × 210 mm; initial bleed: 3 mm each side; full document: 154 × 216 mm. Safe margin: at least 8 mm from trim. At 300 DPI, approximately 1819 × 2551 px including bleed and 1748 × 2480 px at trim. Store front and back as separate layered masters. Confirm bleed, safe area, CMYK/ICC and final format with the printer. Use at most two main font families and preferably 9.5–11 pt body text; do not sacrifice readability for density.

## Front — attention and positioning

1. Official unmodified RavenXcope lockup.
2. Indonesian product category, headline and short positioning from `CONTENT_GUIDELINES.md`.
3. One authentic analytics hero screenshot; `192316` is a candidate. Crop proportionally without changing context; retain original UI colors.
4. A concise strip emphasizing asset recognition, context and prioritization, using Indonesian copy approved for the design.

## Back — capabilities and action

- Lead with the Indonesian benefit statement from `CONTENT_GUIDELINES.md`.
- Candidate visual: risk matrix capture `192442`, large enough to read at A5. It and `192316` are different captures, not one snapshot.
- Four editorial blocks, translated into concise Indonesian brochure copy:
  1. Asset inventory and context: hosts, networks, source and destination assets.
  2. Risk prioritization: severity, criticality and risk matrix.
  3. Analytics and investigation: trends, classification, protocols, IP flow and sensor/time/IP/port filters.
  4. Alert triage: details and false-positive marking.
- Closing statement, CTA and demo URL from `CONTENT_GUIDELINES.md`. A QR may link to that URL; verify destination and scan a physical proof.

Owner review of final copy and composition is required. Avoid unconfirmed deployment or integration claims, fabricated metrics and automatic-blocking claims. Do not reconstruct the risk matrix as new UI. Omit architecture diagrams unless verified source material exists. Retain negative space, consistent grid, a single hero and legible text.
