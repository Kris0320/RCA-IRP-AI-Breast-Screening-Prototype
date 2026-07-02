# SKILL: Readyology Presentation Design System

## Purpose
This skill encodes the complete visual design system for Team 42's Readyology IRP 
presentation. Load this at the start of any session involving slide creation, 
consistency review, or style edits.

**Always apply these rules exactly. Never invent new colours, font sizes, or layout 
patterns unless the user explicitly requests a change.**

---

## DESIGN TOKENS

### Colour Palette
| Token       | Hex       | Usage                                               |
|-------------|-----------|-----------------------------------------------------|
| `--blue`    | `#124BCE` | Primary: section labels, stat numbers, CTA text, highlights |
| `--dark`    | `#111827` | H1 titles, bold body text                           |
| `--mid`     | `#6B7280` | Subtitle, secondary body, captions                  |
| `--lite`    | `#9CA3AF` | Footnotes, muted labels, disabled states            |
| `--orange`  | `#E8693C` | Accent / warning callouts, pilot/scale phase labels |
| `--bg`      | `#F0F1F3` | Slide background (light warm gray)                  |
| `--white`   | `#FFFFFF` | Card backgrounds, section divider slides            |
| `--grid`    | `#C4C8D2` | Divider lines, borders                              |

### Typography
**Font:** Montserrat (Google Fonts). Fallback: `'Helvetica Neue', Arial, sans-serif`

| Role               | Size  | Weight       | Colour                 | Notes                               |
|--------------------|-------|--------------|------------------------|-------------------------------------|
| Section label      | 14px  | 600 SemiBold | `--blue`               | UPPERCASE · letter-spacing 3px      |
| Slide counter      | 14px  | 400 Regular  | `--mid`                | Right-aligned                       |
| H1 — large         | 64px  | 700 Bold     | `--dark`               | Left-aligned · x=160 · line-height 120%  |
| H1 — medium        | 52px  | 700 Bold     | `--dark`               | Left-aligned · x=160 · line-height 120%  |
| Subtitle/caption   | 24px  | 400 Regular  | `--mid`                | line-height 150%                    |
| Stat hero number   | 96px  | 700 Bold     | `--blue` or `--orange` | Never dark · single line            |
| Stat label         | 24px  | 700 Bold     | `--dark`               | Directly below hero · line-height 120%  |
| Stat description   | 18px  | 400 Regular  | `--mid`                | line-height 120% (22px) · compact   |
| Stat inline emph   | 18px  | 700 Bold     | `--blue`               | Key callout within stat description |
| Body text          | 18px  | 400 Regular  | `--mid`                | line-height 150% (27px) · regular   |
| Card label/tag     | 11px  | 700 Bold     | `--white` on `--blue`  | UPPERCASE · letter-spacing 1.5      |
| Quote / statement  | 36px  | 700 Bold     | `--blue`               | Centred on white bg                 |
| Footnote / source  | 12px  | 400 Regular  | `--mid` #6B7280        | italic · right-aligned · bottom     |
| Takeaway body      | 24px  | 400 Regular  | `--mid`                | line-height 150% · bottom of slide  |
| Takeaway headline  | 32px  | 700 Bold     | `--blue`               | Below takeaway body · line-height 120% |

### Spacing Tokens
| Token    | Value | Usage |
|----------|-------|-------|
| tight    | 4px   | Internal gaps: between tag and text, between icon and label |
| standard | 12px  | Gap between adjacent elements (e.g. H1 → Subtitle, card sections) |

**IMPORTANT — two kinds of spacing:**
- **Figma auto-layout gap** = space between bounding boxes (pure empty space, does NOT include line-height). Use this when thinking about design intent.
- **SVG baseline-to-baseline** = distance between `y` coordinates of consecutive text elements. INCLUDES the line-height of both elements. Use this when writing SVG `y` values.

**Figma gaps (between bounding boxes, pure empty space):**
- Section label → H1: **20px**
- H1 → Subtitle: **12px** (= standard spacing token)
- H1/Subtitle block → Stat hero: use remaining space proportionally

**SVG baseline-to-baseline distances (y coordinate differences):**
- Section label → H1: **~91px**
- H1 → Subtitle: **~56px**
- Stat hero → Stat label: **~50px**
- Stat label → Stat desc first line: **~29px**
- Stat desc line-to-line (18px × 120%): **22px**
- Takeaway body → Takeaway headline: **~49px**

**Formula:** B2B = (line-height_upper − cap-height_upper) / 2 + gap + cap-height_lower + (line-height_lower − cap-height_lower) / 2
Approximate cap-height for Montserrat ≈ font-size × 0.72

---

## SLIDE CANVAS & GRID (SVG: 1920 × 1080px)

```
Left margin:    x = 160px
Right margin:   x = 1760px
Content width:  1600px
Top (header):   y = 56px (label baseline)
Header line:    y = 68px
Bottom:         y = 1040–1060px
```

### Standard Header (every content slide)
```
Section label   x=160, y=56,  14px, 600, --blue, UPPERCASE, letter-spacing 3
Divider line    x1=160 y1=68, x2=1760 y2=68, stroke=--grid, width=1
Slide counter   x=1760, y=56, 14px, 400, --mid #6B7280, text-anchor=end
```

### Title Block
```
H1 title        x=160, y=147  (baseline)  64px, 700, --dark, line-height 120%
Subtitle        x=160, y=203  (baseline)  24px, 400, --mid,  line-height 150%
                Gap H1→subtitle baseline: ~56px
```

### Takeaway Block (bottom of content slides)
```
Divider line    y=780
Body text       x=160, y=841,  24px, 400, --mid,  line-height 150%
Headline        x=160, y=889,  32px, 700, --blue, line-height 120%
                Gap body→headline baseline: ~48px
```

---

## SIX SLIDE TYPES

### Type A — Cover Slide
- Near-black or dark photo background
- Large project name: mixed script + sans-serif treatment
- Subtitle: 18–22px, regular, light/white text
- Bottom-left: institution · year (small, white/gray)
- Bottom-right: team members (small, white/gray)
- Team tag and date as pill badges (light gray bg, dark text)

### Type B — Section Divider
- Pure white background (#FFFFFF)
- Section name: top-left, **80px**, 700, **--blue**
- Large section number: bottom-right, **360px**, 700, **--blue**
- No header bar, no slide counter

### Type C — Stats Grid Slide
- Background: `--bg`
- Standard header
- H1 title (64px, 700, --dark) + Subtitle (24px, 400, --mid)
- 2–4 stat blocks:
  - Hero number: **96px**, 700, `--blue` or `--orange`
  - Label: **24px**, 700, `--dark` (line-height 120%)
  - Description: **18px**, 400, `--mid` (line-height 120%, 22px)
- Bottom: takeaway block

### Type D — Three-Column Card Slide
- Background: `--bg`
- Standard header
- H1 + subtitle
- 3 white cards equal width, rx=6–8, fill=`--white`
- Each card: tag label (uppercase, coloured), stat or number, divider, title (20px bold), body (14px), source (12px italic, `--lite`)
- Bottom: key statement in `--blue` bold

### Type E — Quote / Statement Slide
- Pure white background
- No header bar
- Single statement centred vertically and horizontally
- 36–52px, 700, `--blue`
- Optional smaller gray supporting text above

### Type F — Diagram / Process Slide
- Background: `--bg`
- Standard header
- H1 + subtitle
- Process steps as numbered cards or horizontal flow
- Active/highlighted step: `--blue` fill or border
- Bottom: italic summary + bold `--blue` conclusion

---

## COMPONENT SPECS

### White Cards
```
fill:     #FFFFFF
rx:       6–8px
padding:  24px inside
optional top bar: 6px height, rx=3, colour matches section phase
```

### Coloured Tag / Badge
```
fill:    --blue or --orange
text:    #FFFFFF, 11–12px, 700, UPPERCASE, letter-spacing 1.5
rx:      4–6px
padding: 6px 12px
```

### Pill Badge (soft)
```
fill:    #E5E7EB (light gray)
text:    --dark, 12–14px, 600
rx:      20px
```

### Divider Lines
```
Full-width separator:  stroke=--grid, width=1
Accent/HMW emphasis:   stroke=--blue, width=2
Card internal:         stroke=#E5E7EB, width=1
```

### Footnote Format
```
Italic · --mid #6B7280 · 12px · right-aligned · bottom of slide
Format: Author/Organisation · Publication · Year
Multiple: stacked lines, same style, 22px line spacing
```

---

## SECTION STRUCTURE (21-slide deck)

| Slide | Type | Section Label |
|-------|------|---------------|
| 1     | A    | Cover         |
| 2     | —    | TODAY (Agenda)|
| 3     | B    | CONTEXT 01    |
| 4–10  | C/D/F | CONTEXT      |
| 11    | B    | RESEARCH 02   |
| 12–16 | C/D/F | RESEARCH     |
| 17    | B    | PROBLEM 03    |
| (continuing per deck structure)   |

---

## SLIDE GENERATION RULES

When asked to generate or edit a slide:

1. **Identify the slide type** (A–F) before writing any code
2. **Apply all tokens exactly** — no new colours, no invented sizes
3. **Header first**: section label + divider + counter on every content slide
4. **Titles at y=148–180**, subtitles immediately below
5. **Stat numbers always** in `--blue` or `--orange` — never `--dark`
6. **Takeaway block always at bottom** of content slides: body line then bold blue headline
7. **Footnotes bottom-right**, italic, `--lite`
8. **Whitespace matters** — leave minimum 60px between major content blocks
9. **Maximum 3 type sizes per slide** (H1, body, label)
10. **Section label matches current section** (CONTEXT / RESEARCH / PROBLEM / SOLUTION / VALIDATION / OUTCOMES)
11. **Card padding**: always 24px internal, never flush text
12. **Line heights**: regular text (body/subtitle/takeaway body) = **150%**; compact/tight text (H1, stat desc, stat label, takeaway headline) = **120%**

---

## USAGE

At the start of any new session involving slides, say:
> "Use the Readyology design system skill"

Or paste the relevant sections of this document into the conversation before requesting slide generation.

To register as a permanent skill: **Settings → Capabilities → Add Skill** and upload this file.
