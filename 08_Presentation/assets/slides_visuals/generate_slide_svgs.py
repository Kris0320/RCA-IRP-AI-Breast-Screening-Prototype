from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent
W, H = 1920, 1080

BLUE = "#2368A2"
BLUE_SOFT = "#EAF3FA"
AMBER = "#D99A22"
AMBER_SOFT = "#FFF4D9"
RED = "#C94040"
INK = "#111827"
MUTED = "#5E6B7A"
LIGHT = "#F7F9FB"
LINE = "#D9E2EC"
GREY = "#EEF2F6"
WHITE = "#FFFFFF"


def t(x, y, text, size=32, fill=INK, weight=400, anchor="start", family="IBM Plex Sans"):
    return (
        f'<text x="{x}" y="{y}" font-family="{family}, Arial, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">'
        f"{escape(text)}</text>"
    )


def title_block(title, kicker=None, subtitle=None):
    parts = []
    if kicker:
        parts.append(t(96, 92, kicker.upper(), 22, BLUE, 700))
    parts.append(t(96, 160 if kicker else 122, title, 56, INK, 700, family="Newsreader"))
    if subtitle:
        parts.append(t(98, 214 if kicker else 178, subtitle, 26, MUTED, 400))
    return "\n".join(parts)


def rect(x, y, w, h, fill=WHITE, stroke=LINE, sw=2, rx=18):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def line(x1, y1, x2, y2, color=LINE, sw=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"{d}/>'


def arrow(x1, y1, x2, y2, color=LINE, sw=3):
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" '
        f'stroke-linecap="round" marker-end="url(#arrow)"/>'
    )


def circle(x, y, r, fill=WHITE, stroke=LINE, sw=2):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def pill(x, y, text, fill=BLUE_SOFT, color=BLUE, w=None):
    w = w or max(130, len(text) * 12 + 34)
    return rect(x, y, w, 44, fill, "none", 0, 22) + t(x + w / 2, y + 29, text, 18, color, 700, "middle")


def card(x, y, w, h, heading, body="", accent=BLUE):
    parts = [rect(x, y, w, h)]
    parts.append(line(x + 24, y + 22, x + w - 24, y + 22, accent, 6))
    parts.append(t(x + 28, y + 72, heading, 28, INK, 700))
    if body:
        for i, ln in enumerate(wrap(body, 34)):
            parts.append(t(x + 28, y + 112 + i * 31, ln, 21, MUTED))
    return "\n".join(parts)


def wrap(text, n=36):
    words = text.split()
    lines, cur = [], ""
    for word in words:
        if len(cur) + len(word) + 1 > n:
            lines.append(cur)
            cur = word
        else:
            cur = f"{cur} {word}".strip()
    if cur:
        lines.append(cur)
    return lines


def node(x, y, w, h, label, fill=WHITE, stroke=LINE, color=INK):
    parts = [rect(x, y, w, h, fill, stroke, 2, 16)]
    lines = wrap(label, max(12, int(w / 19)))
    start = y + h / 2 - (len(lines) - 1) * 14 + 9
    for i, ln in enumerate(lines):
        parts.append(t(x + w / 2, start + i * 30, ln, 22, color, 700, "middle"))
    return "\n".join(parts)


def svg(name, body, title=None, subtitle=None, kicker=None):
    header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
<path d="M0,0 L10,5 L0,10 z" fill="{LINE}"/>
</marker>
<style>
.small {{ font-family: IBM Plex Sans, Arial, sans-serif; }}
</style>
</defs>
<rect width="{W}" height="{H}" fill="{LIGHT}"/>
<rect x="0" y="0" width="{W}" height="{H}" fill="url(#none)" opacity="0"/>
'''
    content = []
    if title:
        content.append(title_block(title, kicker, subtitle))
    content.append(body)
    content.append(t(96, 1012, "Readyology | RCA Service Design IRP", 18, "#8A97A6"))
    Path(OUT / name).write_text(header + "\n".join(content) + "\n</svg>\n", encoding="utf-8")


def service_line():
    xs = [250, 560, 870, 1180, 1490]
    labels = ["Mammogram", "Human + AI", "Disagreement", "Review", "Learning"]
    colors = [WHITE, BLUE_SOFT, AMBER_SOFT, BLUE_SOFT, BLUE_SOFT]
    strokes = [LINE, BLUE, AMBER, BLUE, BLUE]
    parts = [t(960, 220, "Readyology", 86, INK, 700, "middle", "Newsreader")]
    parts.append(t(960, 275, "A lightweight service layer for AI-human disagreement in breast cancer screening.", 30, MUTED, 400, "middle"))
    for i in range(len(xs) - 1):
        parts.append(arrow(xs[i] + 95, 540, xs[i + 1] - 95, 540, BLUE if i > 1 else LINE, 4))
    for x, lab, fill, stroke in zip(xs, labels, colors, strokes):
        parts.append(circle(x, 540, 82, fill, stroke, 4))
        parts.append(t(x, 548, lab, 22, INK, 700, "middle"))
    parts.append(t(960, 704, "Helping radiologists detect, resolve and learn from AI-human disagreement.", 28, INK, 500, "middle"))
    svg("slide01-cover-service-line.svg", "\n".join(parts))


def opening_story():
    panels = [
        ("Radiologist reviews image", "Human judgement: normal", BLUE),
        ("AI highlights area", "High-confidence AI flag", AMBER),
        ("Service question", "How should review be supported?", BLUE),
    ]
    parts = []
    x = 150
    for i, (h, b, accent) in enumerate(panels):
        px = x + i * 560
        parts.append(rect(px, 300, 440, 430))
        parts.append(line(px + 28, 325, px + 412, 325, accent, 6))
        if i == 0:
            parts.append(circle(px + 150, 480, 62, BLUE_SOFT, BLUE, 3))
            parts.append(rect(px + 232, 415, 120, 150, GREY, LINE, 2, 14))
            parts.append(line(px + 255, 448, px + 330, 448, BLUE, 5))
        elif i == 1:
            parts.append(rect(px + 112, 398, 210, 210, "#111827", "none", 0, 12))
            parts.append(circle(px + 222, 503, 54, "#DDE5EC", "none", 0))
            parts.append(circle(px + 268, 468, 20, AMBER_SOFT, AMBER, 5))
        else:
            parts.append(circle(px + 220, 492, 86, WHITE, BLUE, 4))
            parts.append(t(px + 220, 514, "?", 92, AMBER, 700, "middle", "Newsreader"))
        parts.append(t(px + 40, 655, h, 28, INK, 700))
        parts.append(t(px + 40, 692, b, 22, MUTED))
    svg(
        "slide02-opening-story.svg",
        "\n".join(parts),
        "A disagreement moment inside breast cancer screening",
        "The question is no longer simply who is right. It becomes how the service supports a safe, explainable and shared decision.",
    )


def context_metrics():
    data = [
        ("[PLACEHOLDER]", "annual mammograms", "High-volume public health pathway"),
        ("[PLACEHOLDER]", "radiologist workforce pressure", "More cases, limited expert capacity"),
        ("[PLACEHOLDER]", "screening demand / backlog", "Efficiency pressure is already present"),
        ("[PLACEHOLDER]", "AI pilot evidence", "AI promises support but changes review"),
    ]
    parts = []
    for i, (num, lab, imp) in enumerate(data):
        x = 120 + i * 430
        parts.append(rect(x, 320, 380, 360))
        parts.append(t(x + 34, 405, num, 42, BLUE, 800))
        parts.append(t(x + 34, 462, lab, 25, INK, 700))
        for j, ln in enumerate(wrap(imp, 26)):
            parts.append(t(x + 34, 530 + j * 30, ln, 22, MUTED))
    parts.append(t(120, 780, "When AI enters this pathway, it does not only support detection. It changes how responsibility, disagreement and review are handled.", 29, INK, 600))
    parts.append(t(1510, 935, "[PLACEHOLDER: source]", 18, MUTED))
    svg("slide03-context-metrics.svg", "\n".join(parts), "Breast cancer screening is high-volume, high-responsibility work")


def ai_inflection():
    left = [("Efficiency", "faster routine reading"), ("Detection support", "additional evidence signal"), ("Workload reduction", "potential pressure relief")]
    right = [("Judgement", "how to interpret AI output"), ("Responsibility", "who remains accountable"), ("Disagreement", "what happens when outputs conflict"), ("Arbitration", "how review is triggered")]
    parts = [rect(130, 290, 700, 500), rect(1090, 290, 700, 500)]
    parts.append(t(480, 345, "Why AI is attractive", 34, BLUE, 700, "middle"))
    parts.append(t(1440, 345, "What AI disrupts", 34, AMBER, 700, "middle"))
    for i, (h, b) in enumerate(left):
        parts.append(card(190, 395 + i * 115, 580, 84, h, b, BLUE))
    for i, (h, b) in enumerate(right):
        parts.append(card(1150, 390 + i * 90, 580, 70, h, b, AMBER))
    parts.append(arrow(845, 540, 1075, 540, BLUE, 5))
    parts.append(node(865, 480, 190, 120, "AI integration", BLUE_SOFT, BLUE, BLUE))
    svg("slide04-ai-inflection.svg", "\n".join(parts), "AI is entering screening because the system is under pressure")


def traditional_workflow():
    labels = ["Mammogram acquired", "First reading", "Second reading / comparison", "Consensus or arbitration", "Recall or no recall", "Audit and learning"]
    parts = []
    x0, y, w, gap = 100, 460, 250, 115
    for i, lab in enumerate(labels):
        x = x0 + i * (w + gap)
        fill = BLUE_SOFT if i in (2, 3) else WHITE
        stroke = BLUE if i in (2, 3) else LINE
        parts.append(node(x, y, w, 115, lab, fill, stroke, BLUE if i in (2, 3) else INK))
        if i < len(labels) - 1:
            parts.append(arrow(x + w + 8, y + 58, x + w + gap - 8, y + 58))
    parts.append(t(960, 700, "The existing pathway is human-led, but already contains moments of uncertainty and disagreement.", 30, INK, 600, "middle"))
    svg("slide05-traditional-workflow.svg", "\n".join(parts), "Before AI, screening already depends on comparison and review")


def simple_ai_workflow():
    parts = []
    parts.append(node(270, 350, 440, 120, "Human judgement lane", BLUE_SOFT, BLUE, BLUE))
    parts.append(node(270, 560, 440, 120, "AI output lane", WHITE, LINE))
    parts.append(arrow(720, 410, 910, 500, BLUE, 4))
    parts.append(arrow(720, 620, 910, 560, AMBER, 4))
    parts.append(node(930, 460, 310, 145, "Comparison gate", AMBER_SOFT, AMBER, INK))
    parts.append(arrow(1255, 532, 1460, 532, LINE, 4))
    parts.append(node(1480, 460, 300, 145, "Human-led decision", WHITE, LINE))
    parts.append(t(960, 760, "AI becomes a new actor inside the reading pathway, but not the final decision-maker.", 30, INK, 600, "middle"))
    svg("slide06-simple-ai-workflow.svg", "\n".join(parts), "AI changes where judgement enters the pathway")


def workflow_comparison():
    patterns = [
        ("1. AI before reading", "influenced independent judgement", 1),
        ("2. AI as second reader", "AI-human mismatch requires arbitration", 3),
        ("3. AI as safety net", "late second-look decisions", 4),
        ("4. AI as triage", "routing boundaries and exceptions", 1),
    ]
    parts = []
    for i, (h, risk, hot) in enumerate(patterns):
        x = 120 + i * 445
        parts.append(rect(x, 305, 385, 460))
        parts.append(t(x + 28, 365, h, 27, INK, 700))
        for j in range(4):
            fill = AMBER_SOFT if j + 1 == hot else GREY
            stroke = AMBER if j + 1 == hot else LINE
            parts.append(rect(x + 38 + j * 76, 455, 58, 58, fill, stroke, 2, 10))
            if j < 3:
                parts.append(arrow(x + 98 + j * 76, 484, x + 112 + j * 76, 484))
        parts.append(circle(x + 38 + (hot - 1) * 76 + 29, 555, 16, AMBER, "none", 0))
        parts.append(t(x + 28, 635, "Risk:", 22, AMBER, 700))
        parts.append(t(x + 88, 635, risk, 19, MUTED))
    parts.append(t(960, 860, "Across these models, disagreement concentrates around two service moments: reading and arbitration.", 30, INK, 600, "middle"))
    svg("slide07-ai-workflow-comparison.svg", "\n".join(parts), "Different AI placements create different disagreement points")


def research_evidence():
    nums = ["[X]", "[X]", "[X]", "[X]", "[X]", "[X]"]
    labs = ["workflow models", "countries / pilots", "expert conversations", "tutorial rounds", "prototype tests", "synthesis maps"]
    methods = ["Literature and pilot review", "Expert interviews", "Workflow comparison", "System mapping", "Prototype testing"]
    parts = []
    for i, (num, lab) in enumerate(zip(nums, labs)):
        x = 100 + i * 290
        parts.append(rect(x, 270, 250, 150))
        parts.append(t(x + 125, 335, num, 46, BLUE, 800, "middle"))
        parts.append(t(x + 125, 380, lab, 18, MUTED, 700, "middle"))
    for i, m in enumerate(methods):
        x = 130 + i * 350
        parts.append(card(x, 515, 300, 160, m, "[PLACEHOLDER: image / source]", BLUE))
    parts.append(arrow(560, 790, 820, 790, BLUE, 4))
    parts.append(t(500, 800, "Evidence", 25, INK, 700, "middle"))
    parts.append(t(960, 800, "Insights", 25, INK, 700, "middle"))
    parts.append(arrow(1100, 790, 1360, 790, BLUE, 4))
    parts.append(t(1450, 800, "Design anchor", 25, INK, 700, "middle"))
    svg("slide08-research-evidence.svg", "\n".join(parts), "We built the project from evidence, not assumption")


def key_insights():
    cards = [
        ("System insight", "AI is inserted into workflows designed for human-human review.", "Existing arbitration logic may not fully support AI-human disagreement.", "Design support around arbitration rules and handover."),
        ("Human insight", "Radiologists remain accountable while AI changes confidence and override pressure.", "Support must protect independent judgement while allowing review.", "Make AI evidence inspectable, not instructional."),
        ("Service insight", "Systems may surface disagreement but not support review, record and learning.", "The gap is not detection. It is what happens next.", "Connect disagreement to review, receipt and learning loop."),
    ]
    parts = []
    for i, (h, obs, cons, imp) in enumerate(cards):
        x = 120 + i * 580
        parts.append(rect(x, 285, 500, 520))
        parts.append(t(x + 35, 350, h, 30, INK, 800))
        parts.append(t(x + 35, 420, "Observation", 19, INK, 700))
        for j, ln in enumerate(wrap(obs, 36)):
            parts.append(t(x + 35, 455 + j * 28, ln, 20, MUTED))
        parts.append(t(x + 35, 555, "Consequence", 19, AMBER, 700))
        for j, ln in enumerate(wrap(cons, 36)):
            parts.append(t(x + 35, 590 + j * 28, ln, 20, MUTED))
        parts.append(t(x + 35, 690, "Design implication", 19, BLUE, 700))
        for j, ln in enumerate(wrap(imp, 36)):
            parts.append(t(x + 35, 725 + j * 28, ln, 20, MUTED))
    svg("slide09-key-insights.svg", "\n".join(parts), "Disagreement is not only a technical mismatch")


def active_system_map():
    layers = [
        ("External policy / regulatory", 210),
        ("NHS organisation / governance", 360),
        ("Clinical / operational", 525),
        ("Public / affected", 720),
    ]
    parts = []
    for label, y in layers:
        parts.append(rect(110, y, 1700, 110, "#FBFCFD", LINE, 2, 14))
        parts.append(t(135, y + 65, label, 23, MUTED, 700))
    actors = [
        ("NHS Trust", 480, 395), ("InfoGov", 700, 395), ("AI product", 430, 560), ("PACS / RIS", 650, 560),
        ("Radiologist", 900, 560), ("Arbitration team", 1180, 560), ("Decision record", 1390, 560),
        ("Learning library", 1260, 395), ("Governance / calibration", 1490, 395),
        ("Radiographer", 500, 755), ("MDT / GP", 900, 755), ("Patient", 1300, 755),
    ]
    for name, x, y in actors:
        fill = BLUE_SOFT if name in ("Radiologist", "Learning library") else WHITE
        stroke = BLUE if name in ("Radiologist", "Learning library") else LINE
        parts.append(node(x - 90, y - 38, 180, 76, name, fill, stroke, BLUE if stroke == BLUE else INK))
    parts.append(arrow(520, 560, 810, 560, BLUE, 4))
    parts.append(arrow(990, 560, 1090, 560, BLUE, 4))
    parts.append(arrow(1275, 560, 1300, 560, BLUE, 4))
    parts.append(arrow(1390, 522, 1260, 433, BLUE, 4))
    parts.append(arrow(1350, 395, 1420, 395, BLUE, 4))
    parts.append(rect(780, 460, 770, 220, "none", BLUE, 4, 18))
    parts.append(t(1165, 705, "Readyology service layer", 28, BLUE, 800, "middle"))
    svg("slide10-active-system-map.svg", "\n".join(parts), "The challenge sits between radiologists, AI systems and governance")


def persona_card():
    chips = ["Every extra step matters", "AI needs clinical context", "Human-led accountability", "Shared arbitration context", "Learning across cases"]
    parts = [rect(160, 290, 520, 520), rect(230, 350, 180, 180, GREY, LINE, 2, 90)]
    parts.append(t(420, 405, "[PLACEHOLDER: portrait]", 20, MUTED, 700))
    parts.append(t(230, 595, "Primary user", 22, BLUE, 700))
    parts.append(t(230, 640, "Radiologist / Breast advanced practitioner / Senior reader", 31, INK, 700))
    parts.append(t(230, 710, '"[PLACEHOLDER: quote]"', 24, MUTED, 400, "start", "Newsreader"))
    for i, chip in enumerate(chips):
        x = 780 + (i % 2) * 450
        y = 320 + (i // 2) * 128
        parts.append(card(x, y, 395, 92, chip, "", BLUE if i % 2 == 0 else AMBER))
    for i, icon in enumerate(["screening", "prior image", "arbitration", "record", "learning"]):
        parts.append(pill(795 + i * 190, 740, icon, BLUE_SOFT, BLUE, 165))
    svg("slide11-persona-card.svg", "\n".join(parts), "Our primary user carries the decision, not just the interface")


def journey_breakdown():
    stages = ["Case queue", "Independent reading", "AI output", "Disagreement", "Arbitration", "Outcome", "Calibration"]
    parts = []
    x0, w, gap = 95, 230, 25
    for i, st in enumerate(stages):
        x = x0 + i * (w + gap)
        hot = i in (3, 4)
        parts.append(node(x, 310, w, 86, st, AMBER_SOFT if hot else WHITE, AMBER if hot else LINE, INK))
        if i < len(stages) - 1:
            parts.append(arrow(x + w + 2, 353, x + w + gap - 5, 353))
    rows = [("Clinical / system action", 465), ("Human concern", 570), ("Pain point", 675), ("Opportunity", 780)]
    for label, y in rows:
        parts.append(t(96, y + 34, label, 20, MUTED, 700))
        parts.append(line(330, y + 24, 1780, y + 24, LINE, 2))
    parts.append(rect(850, 285, 520, 560, "none", AMBER, 4, 20))
    parts.append(t(1110, 885, "Two fragile moments: reading disagreement and arbitration", 28, AMBER, 800, "middle"))
    svg("slide12-journey-breakdown.svg", "\n".join(parts), "The fragile moments are reading disagreement and arbitration")


def problem_gap():
    parts = []
    parts.append(node(250, 430, 340, 120, "AI output", BLUE_SOFT, BLUE, BLUE))
    parts.append(node(250, 610, 340, 120, "Human judgement", WHITE, LINE))
    parts.append(arrow(610, 490, 780, 560, BLUE, 4))
    parts.append(arrow(610, 670, 780, 600, LINE, 4))
    parts.append(node(800, 510, 280, 130, "Disagreement", AMBER_SOFT, AMBER, INK))
    parts.append(arrow(1095, 575, 1270, 575, AMBER, 4))
    parts.append(node(1270, 490, 350, 170, "Missing bridge: review / record / learn", WHITE, RED, INK))
    parts.append(rect(1228, 448, 435, 252, "none", BLUE, 5, 24))
    parts.append(t(1445, 735, "Readyology fills this service gap", 30, BLUE, 800, "middle"))
    svg("slide13-problem-gap.svg", "\n".join(parts), "The gap is not AI detection. It is disagreement handling.")


def design_strategy():
    steps = [
        ("Reading Support", "Make disagreement visible without turning AI into an instruction."),
        ("Arbitration Support", "Carry context into shared review so the team discusses the same evidence."),
        ("Learning Support", "Turn selected disagreement cases into non-blame calibration material."),
    ]
    parts = []
    for i, (h, b) in enumerate(steps):
        x = 210 + i * 520
        parts.append(rect(x, 380 - i * 35, 420, 270, BLUE_SOFT if i != 1 else AMBER_SOFT, BLUE if i != 1 else AMBER, 3, 18))
        parts.append(t(x + 40, 455 - i * 35, h, 32, INK, 800))
        for j, ln in enumerate(wrap(b, 31)):
            parts.append(t(x + 40, 510 - i * 35 + j * 30, ln, 21, MUTED))
        if i < 2:
            parts.append(arrow(x + 430, 505 - i * 35, x + 500, 505 - (i + 1) * 35, BLUE, 4))
    parts.append(t(960, 760, "Detect -> Resolve -> Learn", 38, BLUE, 800, "middle"))
    svg("slide14-design-strategy.svg", "\n".join(parts), "From disagreement detection to a learning loop")


def service_proposition():
    stages = ["Reading", "Comparison", "Arbitration", "Outcome", "Learning"]
    parts = []
    x0, y, w, gap = 160, 510, 250, 90
    for i, st in enumerate(stages):
        x = x0 + i * (w + gap)
        parts.append(node(x, y, w, 95, st, WHITE, LINE))
        if i < len(stages) - 1:
            parts.append(arrow(x + w + 8, y + 48, x + w + gap - 8, y + 48))
    parts.append(rect(145, 430, 1500, 245, "none", BLUE, 5, 28))
    parts.append(t(895, 420, "Readyology service layer", 34, BLUE, 800, "middle"))
    parts.append(pill(260, 685, "Reading Support", BLUE_SOFT, BLUE, 240))
    parts.append(pill(800, 685, "Arbitration Support", BLUE_SOFT, BLUE, 290))
    parts.append(pill(1320, 685, "Learning Support", BLUE_SOFT, BLUE, 250))
    parts.append(circle(680, 557, 18, AMBER, "none", 0))
    parts.append(arrow(1430, 610, 1430, 760, BLUE, 4))
    parts.append(arrow(1430, 760, 670, 760, BLUE, 4))
    svg("slide15-service-proposition.svg", "\n".join(parts), "Introducing Readyology")


def prototype_overview():
    cards = [
        ("Reading Interface", "individual reading station", "Detect and inspect disagreement"),
        ("Arbitration Mode", "human-led review meeting", "Resolve with shared context"),
        ("Learning Platform", "scheduled professional learning", "Learn and calibrate over time"),
    ]
    parts = []
    for i, (h, ctx, fn) in enumerate(cards):
        x = 140 + i * 590
        parts.append(rect(x, 320, 500, 420))
        parts.append(rect(x + 38, 365, 424, 170, GREY, LINE, 2, 14))
        parts.append(t(x + 250, 460, "[PLACEHOLDER: screenshot]", 23, MUTED, 700, "middle"))
        parts.append(t(x + 40, 590, h, 31, INK, 800))
        parts.append(t(x + 40, 634, ctx, 21, BLUE, 700))
        parts.append(t(x + 40, 680, fn, 22, MUTED))
        if i < 2:
            parts.append(arrow(x + 510, 530, x + 575, 530, BLUE, 4))
    parts.append(t(960, 845, "Detect -> Resolve -> Learn", 34, BLUE, 800, "middle"))
    svg("slide16-prototype-overview.svg", "\n".join(parts), "Three connected prototype environments")


def reading_support():
    parts = [rect(210, 295, 1050, 585, "#111827", "none", 0, 18)]
    parts.append(rect(260, 350, 400, 420, "#222B35", "none", 0, 16))
    parts.append(rect(730, 350, 400, 420, "#222B35", "none", 0, 16))
    parts.append(circle(500, 545, 105, "#DDE5EC", "none", 0))
    parts.append(circle(940, 545, 105, "#DDE5EC", "none", 0))
    parts.append(circle(1015, 485, 34, AMBER_SOFT, AMBER, 6))
    parts.append(rect(1285, 330, 430, 510, WHITE, LINE, 2, 16))
    parts.append(t(1320, 390, "Soft disagreement signal", 28, INK, 800))
    parts.append(t(1320, 445, "AI output and human judgement differ.", 22, MUTED))
    parts.append(pill(1320, 495, "Amber = disagreement / caution", AMBER_SOFT, AMBER, 330))
    parts.append(pill(1320, 555, "Blue = neutral support action", BLUE_SOFT, BLUE, 310))
    parts.append(pill(1320, 615, "Red = critical only", "#FCE8E8", RED, 220))
    parts.append(arrow(1265, 520, 1050, 493, AMBER, 4))
    svg("slide17-reading-support-callouts.svg", "\n".join(parts), "Reading Support makes disagreement visible without creating alarm")


def arbitration_support():
    parts = [rect(115, 330, 680, 450, "#F0F4F8", LINE, 2, 20)]
    for i in range(3):
        parts.append(rect(155 + i * 205, 385, 170, 230, "#111827", "none", 0, 12))
        parts.append(t(240 + i * 205, 650, "Image screen", 18, MUTED, 700, "middle"))
    parts.append(rect(885, 330, 430, 450, WHITE, BLUE, 3, 20))
    parts.append(t(1100, 395, "Shared evidence screen", 27, BLUE, 800, "middle"))
    parts.append(t(930, 455, "Participant views", 22, MUTED))
    parts.append(t(930, 505, "Disagreement pattern", 22, MUTED))
    parts.append(t(930, 555, "Meeting keywords", 22, MUTED))
    parts.append(t(930, 605, "Evidence controls", 22, MUTED))
    parts.append(rect(1400, 330, 400, 450, WHITE, LINE, 2, 20))
    parts.append(t(1600, 395, "Decision summary", 27, INK, 800, "middle"))
    parts.append(t(1445, 455, "Final rationale", 22, MUTED))
    parts.append(t(1445, 505, "Unresolved uncertainty", 22, MUTED))
    parts.append(t(1445, 555, "Non-blame receipt", 22, MUTED))
    parts.append(t(960, 860, "Image reading remains clean. Discussion evidence is shared. Rationale is captured.", 28, INK, 700, "middle"))
    svg("slide18-arbitration-support-layout.svg", "\n".join(parts), "Arbitration Support creates shared context for human-led review")


def learning_support():
    tags = ["AI-positive / human-negative", "Focal asymmetry", "Prior comparison", "Low suspicion", "Outcome known", "Learning module available"]
    parts = [rect(130, 300, 330, 560, WHITE, LINE, 2, 18), rect(510, 300, 820, 560, WHITE, LINE, 2, 18), rect(1380, 300, 410, 560, WHITE, LINE, 2, 18)]
    parts.append(t(180, 365, "Filters / tags", 28, INK, 800))
    for i, tag in enumerate(tags):
        parts.append(pill(175, 420 + i * 62, tag, BLUE_SOFT if i % 2 else AMBER_SOFT, BLUE if i % 2 else AMBER, 240))
    parts.append(t(560, 365, "Disagreement case library", 30, INK, 800))
    for i in range(3):
        parts.append(rect(565, 430 + i * 120, 700, 88, "#FBFCFD", LINE, 2, 12))
        parts.append(t(595, 465 + i * 120, f"Case {i+1}: [PLACEHOLDER]", 22, INK, 700))
        parts.append(t(595, 498 + i * 120, "Outcome-linked review available", 18, MUTED))
    parts.append(t(1430, 365, "Progress / calibration", 28, INK, 800))
    parts.append(circle(1585, 520, 90, BLUE_SOFT, BLUE, 8))
    parts.append(t(1585, 535, "[X] credits", 27, BLUE, 800, "middle"))
    parts.append(t(1440, 690, "Calibration record", 22, MUTED))
    parts.append(t(1440, 735, "Non-blame case discussion", 22, MUTED))
    svg("slide19-learning-support-platform.svg", "\n".join(parts), "Learning Support turns disagreement into calibration")


def service_blueprint():
    cols = ["Case queue", "Reading", "AI output", "Disagreement", "Arbitration", "Feedback"]
    rows = ["Radiologist actions", "Arbitration actions", "Backstage actions", "Touchpoints", "Supporting systems", "Record created"]
    parts = []
    x0, y0, cw, rh = 310, 250, 245, 105
    for i, col in enumerate(cols):
        parts.append(t(x0 + i * cw + cw / 2, 220, col, 20, INK, 800, "middle"))
    for r, row in enumerate(rows):
        parts.append(t(90, y0 + r * rh + 58, row, 18, MUTED, 700))
        for c in range(len(cols)):
            hot = (c in (3, 4) and r in (2, 3, 5)) or (c == 5 and r in (3, 5))
            parts.append(rect(x0 + c * cw, y0 + r * rh, cw - 8, rh - 8, BLUE_SOFT if hot else WHITE, BLUE if hot else LINE, 2, 10))
    parts.append(circle(x0 + 3 * cw + 110, y0 + 3 * rh + 45, 18, AMBER, "none", 0))
    parts.append(t(960, 960, "Detect -> Review -> Escalate -> Resolve -> Record -> Learn", 30, BLUE, 800, "middle"))
    svg("slide20-service-blueprint.svg", "\n".join(parts), "How Readyology connects reading, arbitration and learning")


def testing_iteration():
    pairs = [
        ("Dashboard", "Service layer"),
        ("Alarm", "Soft signal"),
        ("Dense side panel", "Shared evidence screen"),
        ("Manual documentation", "Guided capture"),
        ("One-off decision", "Learning loop"),
    ]
    parts = []
    for i, (before, after) in enumerate(pairs):
        y = 275 + i * 125
        parts.append(node(170, y, 520, 76, before, WHITE, LINE))
        parts.append(arrow(720, y + 38, 890, y + 38, BLUE, 4))
        parts.append(node(920, y, 620, 76, after, BLUE_SOFT, BLUE, BLUE))
    parts.append(t(960, 920, "Testing made the service lighter, clearer and closer to clinical practice.", 30, INK, 700, "middle"))
    svg("slide21-testing-iteration.svg", "\n".join(parts), "Testing made the service lighter, clearer and closer to clinical practice")


def value_matrix():
    vals = [
        ("Radiologists", "Supports judgement without heavy steps."),
        ("Arbitration teams", "Creates shared context for difficult cases."),
        ("Organisations", "Builds traceable, non-blame evidence."),
        ("AI adoption", "Places AI inside a responsible service pathway."),
    ]
    parts = [circle(960, 530, 135, BLUE_SOFT, BLUE, 5), t(960, 520, "Readyology", 36, BLUE, 800, "middle", "Newsreader"), t(960, 565, "service layer", 22, BLUE, 700, "middle")]
    coords = [(260, 270), (1220, 270), (260, 690), (1220, 690)]
    for (h, b), (x, y) in zip(vals, coords):
        parts.append(card(x, y, 460, 190, h, b, BLUE))
    parts.append(arrow(735, 440, 840, 500, BLUE, 4))
    parts.append(arrow(1185, 440, 1080, 500, BLUE, 4))
    parts.append(arrow(735, 780, 845, 610, BLUE, 4))
    parts.append(arrow(1185, 780, 1085, 610, BLUE, 4))
    parts.append(t(960, 955, "Readyology does not decide who is right. It designs what happens when AI and human judgement do not agree.", 29, INK, 700, "middle"))
    svg("slide22-value-matrix.svg", "\n".join(parts), "Value: supporting judgement, review and learning")


def mapping():
    files = [
        ("slide01-cover-service-line.svg", "Slide 1 - Cover"),
        ("slide02-opening-story.svg", "Slide 2 - Opening Story"),
        ("slide03-context-metrics.svg", "Slide 3 - Why This Context Matters"),
        ("slide04-ai-inflection.svg", "Slide 4 - Why AI Is Being Introduced"),
        ("slide05-traditional-workflow.svg", "Slide 5 - Traditional Workflow"),
        ("slide06-simple-ai-workflow.svg", "Slide 6 - Simple AI Workflow"),
        ("slide07-ai-workflow-comparison.svg", "Slide 7 - AI Workflow Comparison"),
        ("slide08-research-evidence.svg", "Slide 8 - Research Evidence"),
        ("slide09-key-insights.svg", "Slide 9 - Key Insights"),
        ("slide10-active-system-map.svg", "Slide 10 - System Map"),
        ("slide11-persona-card.svg", "Slide 11 - Primary User"),
        ("slide12-journey-breakdown.svg", "Slide 12 - Journey Breakdown"),
        ("slide13-problem-gap.svg", "Slide 13 - Problem / HMW"),
        ("slide14-design-strategy.svg", "Slide 14 - Design Strategy"),
        ("slide15-service-proposition.svg", "Slide 15 - Service Proposition"),
        ("slide16-prototype-overview.svg", "Slide 16 - Prototype Overview"),
        ("slide17-reading-support-callouts.svg", "Slide 17 - Prototype 1: Reading Support"),
        ("slide18-arbitration-support-layout.svg", "Slide 18 - Prototype 2: Arbitration Support"),
        ("slide19-learning-support-platform.svg", "Slide 19 - Prototype 3: Learning Support"),
        ("slide20-service-blueprint.svg", "Slide 20 - Service Blueprint"),
        ("slide21-testing-iteration.svg", "Slide 21 - Testing and Iteration"),
        ("slide22-value-matrix.svg", "Slide 22 - Value"),
    ]
    rows = ["# Readyology SVG Visual Mapping", "", "| SVG file | Recommended slide/frame |", "|---|---|"]
    rows += [f"| `{f}` | {s} |" for f, s in files]
    rows.append("")
    rows.append("Note: These SVGs use editable text where possible. Numeric evidence and image-specific data remain as placeholders until verified.")
    (OUT / "SVG_MAPPING.md").write_text("\n".join(rows) + "\n", encoding="utf-8")


def main():
    service_line()
    opening_story()
    context_metrics()
    ai_inflection()
    traditional_workflow()
    simple_ai_workflow()
    workflow_comparison()
    research_evidence()
    key_insights()
    active_system_map()
    persona_card()
    journey_breakdown()
    problem_gap()
    design_strategy()
    service_proposition()
    prototype_overview()
    reading_support()
    arbitration_support()
    learning_support()
    service_blueprint()
    testing_iteration()
    value_matrix()
    mapping()


if __name__ == "__main__":
    main()
