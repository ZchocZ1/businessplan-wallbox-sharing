from lib import *

OUT = "../slide%02d.png"


def mark(ax, x, y, kind, color=TXT):
    if kind == "yes":
        circ(ax, x, y, 0.13, fc=color, ec="none", z=8)
    elif kind == "no":
        circ(ax, x, y, 0.13, fc="none", ec=MUTED, lw=1.3, z=8)
    elif kind == "alt":
        line(ax, [(x - 0.12, y), (x + 0.12, y)], color=MUTED, lw=1.6, z=8)
    elif kind == "plan":
        circ(ax, x, y, 0.13, fc="none", ec=MINT, lw=1.5, z=8)
        ax.add_patch(Wedge((x, y), 0.13, 90, 270, fc=MINT, ec="none", zorder=9))


def s06():
    fig, ax = new_fig(); base(ax, 6, 1)
    cols = [3.75, 5.1, 6.45, 7.8]
    heads = ["Abrechnung +\nAuszahlung", "Reservierung", "Gadget für\nBestandsbox", "Versicherung"]
    for cx, h in zip(cols, heads):
        T(ax, cx, 3.05, h, size=11, color=MUTED, font="sans", ha="center")
    rows = [("WallShare", ["plan"] * 4, True), ("Cocharge", ["yes", "no", "no", "no"], False),
            ("AirElectric", ["no", "no", "no", "no"], False), ("VoltExchange", ["alt", "no", "alt", "no"], False)]
    for i, (nm, marks, ours) in enumerate(rows):
        yc = 3.85 + i * 0.7
        rrect(ax, 0.6, yc - 0.28, 7.85, 0.56, r=0.08, fc=PANEL2 if ours else PANEL, ec=MINT if ours else LINE, lw=1.3 if ours else 0.8, z=2)
        T(ax, 0.85, yc, nm, size=14.5, color=MINT if ours else TXT, font="sansb")
        for cx, m in zip(cols, marks):
            mark(ax, cx, yc, m)
    # Legende
    ly = 6.55
    items = [(0.65, "yes", "belegt"), (1.9, "no", "auf Seite nicht erwähnt"), (4.75, "alt", "anderes Modell"), (6.75, "plan", "geplant")]
    for lx, kind, lab in items:
        mark(ax, lx + 0.13, ly, kind)
        T(ax, lx + 0.35, ly, lab, size=10.5, color=MUTED)
    # Kernkompetenz
    x0 = 8.85
    rrect(ax, x0, 2.5, 3.88, 4.3, r=0.12, fc=PANEL, ec=MINT, lw=1.3)
    glow(ax, x0 + 3.2, 2.9, 0.5, alpha=0.06)
    T(ax, x0 + 0.3, 2.85, "KERNKOMPETENZ", size=11, color=MINT, font="monob")
    T(ax, x0 + 0.3, 3.4, "Zweiseitigen\nLade-Marktplatz\naufbauen", size=17, color=TXT, font="sansb", va="center")
    T(ax, x0 + 0.3, 4.2, "Plattform + Anbieter und Fahrer\nregional gleichzeitig gewinnen", size=11.5, color=MUTED, va="center")
    for k, lab in enumerate(["Kundennutzen", "Differenzierung", "Imitationsschutz", "Übertragbarkeit"]):
        yy = 4.75 + k * 0.32
        ic_check(ax, x0 + 0.42, yy, 0.18, c=MINT, lw=1.6)
        T(ax, x0 + 0.75, yy, lab, size=12, color=TXT)
    T(ax, x0 + 3.58, 2.85, "KONZEPT", size=9, color=DIM, font="mono", ha="right")
    rrect(ax, x0 + 0.25, 6.12, 3.38, 0.5, r=0.1, fc="none", ec=AMBER, lw=1.3, z=5)
    T(ax, x0 + 1.94, 6.37, "Gate: Eichrecht + Gadget", size=12.5, color=AMBER, font="sansb", ha="center")
    save(fig, OUT % 6)


def trap(ax, cx, y, wt, wb, h, ec=LINE, fc=PANEL, lw=1.1, glow_c=None):
    pts = [(cx - wt / 2, y), (cx + wt / 2, y), (cx + wb / 2, y + h), (cx - wb / 2, y + h)]
    if glow_c:
        glow(ax, cx, y + h / 2, 0.8, color=glow_c, alpha=0.07)
    poly(ax, pts, fc=fc, ec=ec, lw=lw, z=4)


def s07():
    fig, ax = new_fig(); base(ax, 7, 2)
    cx = 3.5; ys = 2.6; h = 0.84; gap = 0.14
    stages = [(5.8, 5.2, "2.034.260", "E-Autos in Deutschland (KBA)", 23), (5.1, 4.5, "ca. 366.000", "ohne Heimladen (Näherung 18 %)", 23),
              (4.4, 3.8, "3.662 · 10.985 · 18.308", "nutzungsbereit (1 · 3 · 5 %)", 17), (3.7, 3.1, "2,0 · 10,9 · 25,9 Mio. €", "Markt pro Jahr (Fahrer zahlen)", 17)]
    for i, (wt, wb, big, small, sz) in enumerate(stages):
        y = ys + i * (h + gap)
        last = (i == 3)
        trap(ax, cx, y, wt, wb, h, ec=MINT if last else LINE, fc=PANEL2 if last else PANEL, lw=1.8 if last else 1.0, glow_c=MINT if last else None)
        T(ax, cx, y + 0.32, big, size=sz, color=MINT if last else TXT, font="disp", ha="center")
        T(ax, cx, y + 0.63, small, size=11, color=MUTED, ha="center")
    # Balken rechts
    T(ax, 7.1, 2.72, "Markt und Plattformerlös pro Jahr, Mio. €", size=14, color=TXT, font="sansb")
    base_y = 5.25; sc = 0.081
    groups = [(8.2, "pessimistisch", "1 % Nutzer", 2.0, 0.2), (10.1, "realistisch", "3 % Nutzer", 10.9, 1.6), (12.0, "optimistisch", "5 % Nutzer", 25.9, 5.2)]
    line(ax, [(7.2, base_y), (12.75, base_y)], color=LINE, lw=1.0)
    for gx, nm, sub, mk, pv in groups:
        hb = mk * sc; hp = pv * sc
        rrect(ax, gx - 0.62, base_y - hb, 0.55, hb, r=0.03, fc=MINT, ec="none", z=5)
        rrect(ax, gx + 0.07, base_y - max(hp, 0.03), 0.55, max(hp, 0.03), r=0.03, fc=AMBER, ec="none", z=5)
        T(ax, gx - 0.345, base_y - hb - 0.2, f"{mk:.1f}".replace(".", ","), size=13, color=MINT, font="sansb", ha="center")
        T(ax, gx + 0.345, base_y - hp - 0.2, f"{pv:.1f}".replace(".", ","), size=13, color=AMBER, font="sansb", ha="center")
        T(ax, gx, base_y + 0.25, nm, size=11.5, color=TXT, ha="center")
        T(ax, gx, base_y + 0.5, sub, size=9.5, color=DIM, font="mono", ha="center")
    rrect(ax, 7.2, 3.02, 0.22, 0.14, r=0.03, fc=MINT, ec="none"); T(ax, 7.5, 3.09, "Markt", size=10.5, color=MUTED)
    rrect(ax, 8.25, 3.02, 0.22, 0.14, r=0.03, fc=AMBER, ec="none"); T(ax, 8.55, 3.09, "Plattformerlös (Provision)", size=10.5, color=MUTED)
    chip(ax, 7.2, 5.95, 5.53, 0.38, "Nachfrage begrenzt: Wallbox-Kapazität ×19 bis ×183", color=MINT, size=11.5, font="sans", tc=TXT)
    chip(ax, 7.2, 6.4, 5.53, 0.38, "Pilot, 2 Regionen: 11 k · 79 k · 289 k € Umsatz", color=LINE, size=11.5, font="sans", tc=TXT)
    save(fig, OUT % 7)


def s08():
    fig, ax = new_fig(); base(ax, 8, 2)
    def rowlabel(y, tag, title):
        T(ax, 0.6, y, tag, size=9, color=DIM, font="mono")
        T(ax, 0.6, y + 0.28, title, size=14, color=TXT, font="sansb")
    def mio(v, d):
        return f"{v:.{d}f}".replace(".", ",") + " Mio."
    rowlabel(2.55, "E-AUTOS (BEV)", "Bestand Deutschland")
    for k, (lab, v) in enumerate([("1.1.2025", 1.65), ("1.1.2026", 2.03)]):
        yy = 3.4 + k * 0.38
        T(ax, 1.55, yy, lab, size=10, color=MUTED, font="mono", ha="right")
        rrect(ax, 1.7, yy - 0.13, v * 1.25, 0.26, r=0.03, fc=MUTED if k == 0 else MINT, ec="none")
        T(ax, 1.7 + v * 1.25 + 0.1, yy, mio(v, 2), size=11.5, color=TXT)
    T(ax, 6.0, 3.6, "+23,2 %", size=24, color=MINT, font="disp", ha="center")
    line(ax, [(0.6, 3.93), (6.4, 3.93)], color=LINE, lw=0.7)
    rowlabel(4.15, "ÖFFENTLICHE LADEPUNKTE", "Bundesnetzagentur, 1.9.2026")
    T(ax, 0.6, 4.95, "214.334", size=32, color=TXT, font="disp")
    T(ax, 3.1, 4.95, "+15,6 % zum Vorjahr (Presse)", size=11.5, color=MUTED)
    line(ax, [(0.6, 5.32), (6.4, 5.32)], color=LINE, lw=0.7)
    rowlabel(5.55, "PRIVATE LADEPUNKTE", "AlixPartners über Statista")
    for k, (lab, v, dash) in enumerate([("2023", 2.359, False), ("2030", 4.069, True)]):
        yy = 6.28 + k * 0.38 - 0.0
        T(ax, 1.55, yy, lab, size=10, color=MUTED, font="mono", ha="right")
        rrect(ax, 1.7, yy - 0.13, v * 0.55, 0.26, r=0.03, fc="none" if dash else MUTED, ec=MINT if dash else "none", lw=1.2, ls=(0, (3, 2)) if dash else "-")
        T(ax, 1.7 + v * 0.55 + 0.1, yy, (mio(v, 2) if not dash else mio(v, 2) + " (Prognose)"), size=11, color=TXT)
    rrect(ax, 6.9, 2.5, 5.83, 4.3, r=0.12, fc=PANEL, ec=LINE, lw=1.0)
    circ(ax, 7.3, 2.95, 0.2, ec=AMBER, lw=1.4)
    T(ax, 7.3, 2.97, "?", size=14, color=AMBER, font="disp", ha="center", z=9)
    T(ax, 7.65, 2.95, "Keine belegte Branchenrendite", size=15, color=TXT, font="sansb")
    T(ax, 7.1, 3.5, "Eigene Rechnung: Deckungsbeitrag je Anbieter und Monat", size=11.5, color=MUTED)
    cols = [(7.95, "pessimistisch", "0,37 €", 91.7, CORAL), (9.8, "realistisch", "10,02 €", 39.3, AMBER), (11.65, "optimistisch", "30,36 €", 24.3, MINT)]
    for cx2, nm, val, pc, col in cols:
        T(ax, cx2, 4.05, val, size=26, color=col, font="disp", ha="center")
        T(ax, cx2, 4.45, nm, size=11, color=MUTED, ha="center")
        rrect(ax, cx2 - 0.8, 5.0, 1.6, 0.16, r=0.04, fc=GRIDC, ec="none")
        rrect(ax, cx2 - 0.8, 5.0, 1.6 * pc / 100, 0.16, r=0.04, fc=col, ec="none")
        T(ax, cx2, 5.33, f"{pc:.0f} %", size=12, color=TXT, font="sansb", ha="center")
    T(ax, 7.1, 4.8, "Zahlungskosten in % der Provision", size=10.5, color=DIM, font="mono")
    chip(ax, 7.15, 6.05, 5.33, 0.46, "Unter ca. 100 kWh je Wallbox und Monat trägt das Modell nicht", color=AMBER, size=11.5, font="sans", tc=TXT)
    save(fig, OUT % 8)


def radar(ax, cx, cy, R, labels, vals, color, words, dashed_idx=None):
    n = 5
    ang = [np.deg2rad(90 - 72 * k) for k in range(n)]
    for lvl in range(1, 6):
        pts = [(cx + R * lvl / 5 * np.cos(a), cy - R * lvl / 5 * np.sin(a)) for a in ang]
        poly(ax, pts, fc="none", ec=LINE, lw=0.8 if lvl < 5 else 1.1, alpha=0.9, z=2)
    for a in ang:
        line(ax, [(cx, cy), (cx + R * np.cos(a), cy - R * np.sin(a))], color=LINE, lw=0.6, z=2)
    pts = [(cx + R * v / 5 * np.cos(a), cy - R * v / 5 * np.sin(a)) for v, a in zip(vals, ang)]
    glow(ax, cx, cy, R * 0.5, color=color, alpha=0.05)
    poly(ax, pts, fc=color, ec=color, lw=2.0, alpha=0.22, z=4)
    poly(ax, pts, fc="none", ec=color, lw=2.0, z=5)
    for i, (px, py) in enumerate(pts):
        if dashed_idx == i:
            circ(ax, px, py, 0.09, fc=BG, ec=AMBER, lw=1.6, z=7)
        else:
            circ(ax, px, py, 0.07, fc=color, ec="none", z=7)
    for i, a in enumerate(ang):
        lx = cx + (R + 0.28) * np.cos(a); ly = cy - (R + 0.28) * np.sin(a)
        ha = "center" if abs(np.cos(a)) < 0.3 else ("left" if np.cos(a) > 0 else "right")
        va = "bottom" if np.sin(a) > 0.9 else "center"
        yoff = -0.05 if va == "bottom" else 0
        T(ax, lx, ly - 0.17 + yoff if va != "bottom" else ly, labels[i], size=12.5, color=TXT, font="sansb", ha=ha, va=va)
        T(ax, lx, (ly + 0.08) if va != "bottom" else ly + 0.2, words[i], size=11, color=AMBER if dashed_idx == i else color, ha=ha, va="center" if va != "bottom" else "top")


def s09():
    fig, ax = new_fig(); base(ax, 9, 2)
    T(ax, 0.6, 2.62, "LADEN VON E-AUTOS", size=10, color=MINT, font="monob")
    T(ax, 6.9, 2.62, "SHARING-PLATTFORMEN", size=10, color=BLUE, font="monob")
    radar(ax, 3.6, 4.55, 1.45, ["Rivalität", "Neue Anbieter", "Substitute", "Käufermacht", "Lieferanten"], [4, 3.5, 4, 4, 3], MINT,
          ["hoch", "mittel–hoch", "hoch", "hoch", "mittel"])
    radar(ax, 9.75, 4.55, 1.45, ["Rivalität", "Neue Anbieter", "Substitute", "Käufermacht", "Anbieter-Macht"], [3, 3, 4, 4, 3], BLUE,
          ["mittel", "mittel", "hoch", "hoch", "offen"], dashed_idx=4)
    T(ax, 3.6, 6.62, "Cocharge · AirElectric · öffentliche Betreiber", size=11.5, color=MUTED, ha="center")
    T(ax, 9.75, 6.62, "VoltExchange · kein Massenmarkt", size=11.5, color=MUTED, ha="center")
    save(fig, OUT % 9)
