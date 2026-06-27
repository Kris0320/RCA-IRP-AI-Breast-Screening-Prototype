# Readyology Slides — Typography Specification
## Canvas: 1920 × 1080px · Font: Montserrat

---

## Scale Mapping

Your web type scale (left) mapped to SVG slide canvas (right).
Multiplier ≈ 1.8–2x, adjusted for slide viewing distance.

| Token     | Web scale | SVG slide | Weight   | Use case                                        |
|-----------|-----------|-----------|----------|-------------------------------------------------|
| DISPLAY   | 48px      | **80px**  | 700      | Dark slide hero text (05, 12, 14, 21)           |
| H1        | 36px      | **68px**  | 700      | Main heading — every light slide                |
| H2        | 28px      | **36px**  | 700      | Column/section heading within a slide           |
| H3        | 20px      | **28px**  | 700      | Card heading, stat label (bold label under num) |
| BODY      | 18px      | **22px**  | 400      | Bullet body, subheading descriptor line         |
| PARAGRAPH | 16px      | **18px**  | 400      | Supporting detail, description under bullets    |
| LABEL     | 13px      | **14px**  | 400/600  | Internal tags, footnotes, photo notes           |
| SECTION   | 13px      | **13px**  | 600      | Header label (CONTEXT / RESEARCH…) + slide no.  |
| CAPTION   | 12px      | **12px**  | 400      | Citation, attribution (bottom right)            |
| DATA      | 24px      | **96px**  | 900      | Big statistics (slide 03, 09)                   |
| TAKEAWAY  | —         | **28px**  | 700      | Blue so-what line (bottom of light slides)      |

---

## Usage Rules

### Every light slide
```
SECTION LABEL (13, 600, BLUE)   ·   rule   ·   slide number (13, 400, MID)
H1 (68, 700, #111827)           ← heading tells the story
BODY (22, 400, #6B7280)         ← subheading qualifies the takeaway
── content ──
TAKEAWAY line (28, 700, #124BCE) ← so what? answer in one sentence
```

### Every dark (atmospheric) slide
```
SECTION LABEL (13, 600, #7B8DA0) · rule · slide number (13, 400, #7B8DA0)
DISPLAY (80, 300, #7B8DA0)      ← setup / context line
DISPLAY (80, 700, #FFFFFF)      ← the punch line
```

### Stats slides (03, 09)
```
DATA (96, 900, #124BCE)         ← the number
H3 (28, 700, #111827)           ← what it means
PARAGRAPH (18, 400, #6B7280)    ← one-line context
```

### Column cards (10, 13, 15, 20)
```
H2 (36, 700, colour)            ← column heading
rule
BODY (22, 400, #111827)         ← each bullet point
```

---

## Line / Divider Rule

> **Only add a line if the content on either side has no natural visual separation.**
> If the adjacent sections already have their own containers, distinct colour, or strong typographic contrast (size, weight, colour), a decorative line is redundant — omit it.

| Situation | Line needed? |
|-----------|-------------|
| Header label `CONTEXT · 3/21` at top | ✅ Yes — thin rule at y=74 anchors the header zone on every slide |
| Between two columns that already have bold coloured headings (`The Promise` / `The Reality`) | ❌ No |
| Above a stats row when numbers are 96px blue | ❌ No — size + colour already divides |
| Between stats and a section that opens with a blue section label (`Expert Consultations`) | ❌ No — the coloured label is sufficient |
| Below sub-section cards that have their own border/container | ❌ No |
| Between content area and takeaway when takeaway has distinct size + colour | ❌ No |
| Inside a chart as axis or grid | ✅ Yes — functional data lines, always keep |
| Inside a chart legend to show curve colour | ✅ Yes — functional |
| Annotation brackets (e.g. THE GAP orange bracket) | ✅ Yes — functional annotation |

**Applied in v4:** slide-03 (−5 lines), slide-04 (−4 lines), slide-06 (−6 lines).

---

## Sizes NOT to use

The following sizes appeared in the current slides but fall outside the spec and should be eliminated:

| Currently used | Replace with |
|---------------|-------------|
| 17px          | 18px (PARAGRAPH) |
| 19px          | 18px (PARAGRAPH) |
| 20px          | 22px (BODY) or 18px (PARAGRAPH) |
| 21px          | 22px (BODY) |
| 24px (body)   | 22px (BODY) |
| 30px          | 28px (TAKEAWAY) |
| 32px          | 36px (H2) |
| 34px          | 36px (H2) |
| 40px          | 36px (H2) or 68px (H1) |
| 44px, 46px, 48px, 52px | 68px (H1) |
| 72px          | 68px (H1) |
| 100px, 108px  | 96px (DATA) |
| 120px         | keep on slide 21 only (close hero) |
| 148px         | keep on slide 01 only (cover wordmark) |

---

## Colour use

| Token  | Hex       | Use                              |
|--------|-----------|----------------------------------|
| DARK   | #111827   | All headings and body (light bg) |
| MID    | #6B7280   | Subheadings, descriptors, labels |
| LITE   | #9CA3AF   | De-emphasised supporting text    |
| BLUE   | #124BCE   | Section labels, accent, takeaway |
| WHITE  | #FFFFFF   | All text on dark bg              |
| DLITE  | #7B8DA0   | Muted text on dark bg            |

---

## Exceptions (intentional, do not change)

| Slide | Element           | Size   | Reason                          |
|-------|-------------------|--------|---------------------------------|
| 01    | Wordmark "R"      | 148px  | Cover hero treatment            |
| 01    | Cover tagline     | 46px   | Intermediate between 148px & 28px — cover only |
| 14    | Brand wordmark    | 108px  | Dark intro hero                 |
| 21    | "Thank you."      | 120px  | Close slide impact              |
| 21    | Brand wordmark    | 108px  | Matches slide 01/14             |
| 06    | Stats row         | 88px   | Slightly smaller — 4 col tight  |
| 17,18 | Dense table text  | 12-14px| BMC/Blueprint — content density |

---

*Last updated: 2026-06-25 · Batch applied. 20/21 slides on-spec. Slide-01 cover tagline 46px kept as intentional exception. Line-reduction rule added and applied to slides 03, 04, 06.*
