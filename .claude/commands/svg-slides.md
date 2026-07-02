# SVG Slides Design System

A portable design system for creating 1920 × 1080 SVG presentation slides with
consistent typography, spacing, colour, and layout.

Invoke with `/svg-slides` at the start of any slide-creation session.

---

## HOW TO USE

1. Fill in the **Project Config** block below (once per project).
2. Tell Claude which slide you need, e.g. "Build a Type C stats slide for Section 02."
3. Claude applies all tokens and rules exactly.

---

## PROJECT CONFIG ← fill this in for each new project

```
PROJECT_NAME:     [e.g. "Readyology"]
TEAM_NAME:        [e.g. "Team 42"]
INSTITUTION:      [e.g. "Royal College of Art"]
DATE:             [e.g. "June 2026"]

COLOR_PRIMARY:    #124BCE   ← main brand colour
COLOR_ACCENT:     #E8693C   ← accent / callout
COLOR_DARK:       #111827   ← H1 titles, bold body
COLOR_MID:        #6B7280   ← subtitles, body, captions
COLOR_LITE:       #9CA3AF   ← footnotes, muted labels
COLOR_BG:         #EFF0F2   ← slide background
COLOR_WHITE:      #FFFFFF   ← card backgrounds, Type B divider
COLOR_GRID:       #C4C8D2   ← divider lines, borders

FONT_PRIMARY:     Montserrat   ← Google Fonts
FONT_FALLBACK:    'Helvetica Neue', Arial, sans-serif

SECTIONS:         [e.g. 01 CONTEXT · 02 RESEARCH · 03 PROBLEM · 04 SOLUTION]
```

---

## DESIGN TOKENS

| Token           | Default   | Usage                                              |
|-----------------|-----------|----------------------------------------------------|
| `COLOR_PRIMARY` | `#124BCE` | Section labels, stat numbers, highlights           |
| `COLOR_DARK`    | `#111827` | H1 titles, bold body                               |
| `COLOR_MID`     | `#6B7280` | Subtitle, secondary body, captions                 |
| `COLOR_LITE`    | `#9CA3AF` | Footnotes, muted labels                            |
| `COLOR_ACCENT`  | `#E8693C` | Accent callouts, phase labels                      |
| `COLOR_BG`      | `#EFF0F2` | Slide background                                   |
| `COLOR_WHITE`   | `#FFFFFF` | Card backgrounds, Type B slides                    |
| `COLOR_GRID`    | `#C4C8D2` | Divider lines, borders                             |

---

## TYPOGRAPHY

**Always use `<text>` elements — never outline paths.**

```svg
<defs>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,600;0,700;1,700&display=swap');
    text { font-family: Montserrat, 'Helvetica Neue', Arial, sans-serif; }
  </style>
</defs>
```

| Role               | Size  | Weight | Colour          | Notes                                   |
|--------------------|-------|--------|-----------------|-----------------------------------------|
| Section label      | 14px  | 600    | `COLOR_PRIMARY` | UPPERCASE · letter-spacing 3px          |
| Slide counter      | 14px  | 400    | `COLOR_MID`     | Right-aligned                           |
| H1 — large         | 64px  | 700    | `COLOR_DARK`    | x=160 · line-height 120%               |
| H1 — medium        | 52px  | 700    | `COLOR_DARK`    | x=160 · line-height 120%               |
| Subtitle           | 24px  | 400    | `COLOR_MID`     | line-height 150%                        |
| Stat hero number   | 96px  | 700    | `COLOR_PRIMARY` or `COLOR_ACCENT` | Never dark    |
| Stat label         | 24px  | 700    | `COLOR_DARK`    | Below hero · line-height 120%           |
| Stat description   | 18px  | 400    | `COLOR_MID`     | line-height 120% (22px)                 |
| Body text          | 18px  | 400    | `COLOR_MID`     | line-height 150% (27px)                 |
| Card label / tag   | 11px  | 700    | `COLOR_WHITE`   | UPPERCASE · letter-spacing 1.5          |
| Quote / statement  | 36px  | 700    | `COLOR_PRIMARY` | Centred on white bg                     |
| Takeaway body      | 24px  | 400    | `COLOR_MID`     | line-height 150% · bottom of slide      |
| Takeaway headline  | 32px  | 700    | `COLOR_PRIMARY` | Below takeaway body · line-height 120%  |
| Footnote           | 12px  | 400    | `COLOR_MID`     | italic · right-aligned · bottom         |

---

## CANVAS & GRID

**Canvas:** 1920 × 1080 px · **All y-coordinates must be multiples of 4.**

```
Left margin:   x = 160     Right margin:  x = 1760
Content width: 1600         Header label:  y = 56
Header line:   y = 68       Bottom zone:   y = 1040–1060
```

### Standard Header (Type C / D / E / F)
```svg
<text x="160" y="56" font-size="14" font-weight="600"
      fill="COLOR_PRIMARY" letter-spacing="3">SECTION NAME</text>
<line x1="160" y1="68" x2="1760" y2="68"
      stroke="COLOR_GRID" stroke-width="1"/>
<text x="1760" y="56" text-anchor="end"
      font-size="14" font-weight="400" fill="COLOR_MID">N / TOTAL</text>
```

### Fixed Baselines
```
H1:               y = 148
Subtitle:         y = 204   (gap from H1 ~56px)
Takeaway divider: y = 780
Takeaway body:    y = 841
Takeaway headline:y = 889
```

### Baseline-to-Baseline Reference
| Transition                        | Distance |
|-----------------------------------|----------|
| Section label → H1                | ~91px    |
| H1 → Subtitle                     | ~56px    |
| Stat hero → Stat label            | ~50px    |
| Stat label → Stat desc first line | ~29px    |
| Stat desc line-to-line            | 22px     |
| Takeaway body → Takeaway headline | ~49px    |

**B2B formula:**
`B2B = (line-height_upper − cap-height_upper)/2 + gap + cap-height_lower + (line-height_lower − cap-height_lower)/2`
Cap-height ≈ font-size × 0.72

---

## SIX SLIDE TYPES

### Type A — Cover
Dark/photo background · large project name · subtitle 18–22px white ·
bottom-left: institution + year · bottom-right: team · pill badges for tag/date

### Type B — Section Divider
White background · section name top-left 80px 700 PRIMARY ·
section number bottom-right 360px 700 PRIMARY (10% opacity) · no header, no counter

### Type C — Stats Grid
BG background · standard header · H1 + subtitle ·
2–4 stat blocks (96px hero → 24px label → 18px desc) · takeaway block

### Type D — Three-Column Cards
BG background · standard header · H1 + subtitle ·
3 white cards rx=6–8 · each: tag + stat + divider + title (20px bold) + body (14px) + source (12px italic) ·
bottom: bold PRIMARY statement

### Type E — Quote / Statement
White background · no header · single statement centred 36–52px 700 PRIMARY ·
optional smaller gray supporting text above

### Type F — Diagram / Process
BG background · standard header · H1 + subtitle ·
numbered cards or horizontal flow · active step: PRIMARY fill/border ·
bottom: italic summary + bold PRIMARY conclusion

---

## COMPONENT SPECS

### White Card
```
fill: COLOR_WHITE · rx: 6–8px · padding: 24px (never flush)
optional top bar: h=6, rx=3, colour matches section phase
```

### Tag / Badge
```
fill: COLOR_PRIMARY or COLOR_ACCENT
text: COLOR_WHITE · 11–12px · 700 · UPPERCASE · letter-spacing 1.5
rx: 4–6px · padding: 6px 12px
```

### Pill Badge (soft)
```
fill: #E5E7EB · text: COLOR_DARK · 12–14px · 600 · rx: 20px
```

### Lucide Icons (inline SVG)
To place an 18px icon centred at (cx, cy):
```svg
<g transform="translate(CX-9, CY-9) scale(0.75)"
   fill="none" stroke="COLOR" stroke-width="2"
   stroke-linecap="round" stroke-linejoin="round">
  <!-- paste Lucide path data here -->
</g>
```

---

## SLIDE GENERATION RULES

1. Read Project Config first — apply all token substitutions before writing SVG
2. Identify slide type (A–F) before writing code
3. Header first: section label + divider + counter (not on Type A or B)
4. Titles at y=148, subtitles at y=204
5. Stat numbers always in PRIMARY or ACCENT — never DARK
6. Takeaway block at bottom of every content slide (y=780/841/889)
7. Footnotes bottom-right, italic, COLOR_LITE
8. Minimum 60px between major content blocks
9. Maximum 3 type sizes per slide
10. Card padding: always 24px internal
11. Line heights: body/subtitle = 150%; H1/stat/headline = 120%
12. 4px grid: every y-coordinate must be a multiple of 4
13. Text as `<text>` elements, never outlined paths

---

## QUICK-START SHELL

```svg
<svg width="1920" height="1080" viewBox="0 0 1920 1080" xmlns="http://www.w3.org/2000/svg">
<defs>
  <style>@import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;0,600;0,700;1,700&display=swap');
  text { font-family: Montserrat,'Helvetica Neue',Arial,sans-serif; }</style>
</defs>
<rect width="1920" height="1080" fill="#EFF0F2"/>
<!-- Header -->
<text x="160" y="56" font-size="14" font-weight="600" fill="#124BCE" letter-spacing="3">SECTION</text>
<line x1="160" y1="68" x2="1760" y2="68" stroke="#C4C8D2" stroke-width="1"/>
<text x="1760" y="56" text-anchor="end" font-size="14" font-weight="400" fill="#6B7280">N / TOTAL</text>
<!-- Title -->
<text x="160" y="148" font-size="52" font-weight="700" fill="#111827">Title Here</text>
<text x="160" y="204" font-size="24" font-weight="400" fill="#6B7280">Subtitle here</text>
<!-- YOUR CONTENT -->
<!-- Takeaway -->
<line x1="160" y1="780" x2="1760" y2="780" stroke="#C4C8D2" stroke-width="1"/>
<text x="160" y="841" font-size="24" font-weight="400" fill="#6B7280">Takeaway body</text>
<text x="160" y="889" font-size="32" font-weight="700" fill="#124BCE">Bold takeaway headline.</text>
</svg>
```

---

## ADAPTING FOR A NEW PROJECT

1. Edit the **Project Config** block with your values
2. Replace default hex values in the Quick-Start Shell with your `COLOR_*` tokens
3. Update `SECTIONS` to match your deck structure
4. The technical rules (grid, B2B, components, Lucide icons) never change
