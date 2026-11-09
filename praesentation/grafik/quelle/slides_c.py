from lib import *

OUT = "../slide%02d.png"

# (ID, Kurzlabel, Wert) -- Werte aus kapitel/03c (Gewicht in % bzw. Wert W x A)
S_ = [("S1", "Kapitalarmes Modell", 6.7), ("S2", "Klares Zielsegment", 6.7), ("S3", "Gadget-Potenzial", 8.3),
      ("S4", "Rundum-Service", 5.0), ("S5", "Interdisziplinäres Team", 5.0), ("S6", "Quellenbasierte Planung", 3.3),
      ("S7", "Regionale Nähe", 3.3)]
W_ = [("W1", "Kein Entwickler-Know-how", 16.7), ("W2", "Zeitbudget 5–10 h/Woche", 13.3), ("W3", "Finanzierung offen", 16.7),
      ("W4", "Gadget ungeprüft", 16.7), ("W5", "Keine Marke, keine Nutzer", 25.0), ("W6", "Rechtsfragen offen", 13.3),
      ("W7", "Partner nicht gewählt", 5.0), ("W8", "Keine Primärdaten", 13.3), ("W9", "Abstimmungslücken", 3.3)]
O_ = [("O1", "E-Auto-Boom +23 %", 15), ("O2", "Nicht-Heimlader, Mieter", 16), ("O3", "Ungenutzte Kapazität", 12),
      ("O4", "P2P-Anbieter weichen", 9), ("O5", "Ad-hoc-Preisaufschlag", 9), ("O6", "Gründungsförderung", 9),
      ("O7", "Zukaufbare Bausteine", 16), ("O8", "Partner-Kooperationen", 9), ("O9", "PV-Trend", 6)]
T_ = [("T1", "Eichrecht", 25), ("T2", "Pflicht „öffentlich“", 12), ("T3", "Steuer, Haftung", 16),
      ("T4", "Neue Wettbewerber", 16), ("T5", "Substitute", 16), ("T6", "Markt nicht etabliert", 20),
      ("T7", "Preisdruck", 12), ("T8", "Zahlungsrecht", 12), ("T9", "IT-Sicherheit, Vertrauen", 12)]


def quad(ax, x, y, w, h, letter, name, items, color, vmax):
    rrect(ax, x, y, w, h, r=0.1, fc=PANEL, ec=LINE, lw=1.0, z=2)
    T(ax, x + 0.3, y + 0.5, letter, size=40, color=color, font="disp")
    T(ax, x + 0.95, y + 0.4, name, size=10.5, color=color, font="monob")
    n = len(items); half = (n + 1) // 2
    big = max(items, key=lambda t: t[2])[0]
    for i, (idn, lab, v) in enumerate(items):
        col = 0 if i < half else 1
        row = i if i < half else i - half
        cx = x + 0.3 + col * 3.0
        cy = y + 0.9 + row * 0.235
        r = 0.035 + 0.06 * v / vmax
        circ(ax, cx + 0.05, cy, r, fc=color, ec="none", z=5)
        T(ax, cx + 0.28, cy, idn, size=10, color=DIM, font="sans")
        T(ax, cx + 0.62, cy, lab, size=11, color=TXT if idn == big else MUTED, font="sansb" if idn == big else "sans")


def s10():
    fig, ax = new_fig(); base(ax, 10, 2)
    x1, x2, w1, w2 = 1.1, 6.93, 5.7, 5.8
    y1, y2, h = 2.5, 4.72, 2.08
    quad(ax, x1, y1, w1, h, "S", "STÄRKEN · INTERN · HILFREICH", S_, MINT, 8.3)
    quad(ax, x2, y1, w2, h, "W", "SCHWÄCHEN · INTERN · SCHÄDLICH", W_, CORAL, 25.0)
    quad(ax, x1, y2, w1, h, "O", "CHANCEN · EXTERN · HILFREICH", O_, MINT, 16)
    quad(ax, x2, y2, w2, h, "T", "RISIKEN · EXTERN · SCHÄDLICH", T_, CORAL, 25)
    T(ax, 0.78, y1 + h / 2, "INTERN", size=10, color=MUTED, font="monob", ha="center", rot=90)
    T(ax, 0.78, y2 + h / 2, "EXTERN", size=10, color=MUTED, font="monob", ha="center", rot=90)
    save(fig, OUT % 10)


def s11():
    fig, ax = new_fig(); base(ax, 11, 2)
    zero = 8.7; sc = 0.15
    rows = sorted(S_, key=lambda t: -t[2]) + sorted(W_, key=lambda t: -t[2])
    y0 = 2.68; pitch = 0.255
    line(ax, [(zero, 2.5), (zero, 6.78)], color=MUTED, lw=1.0, z=3)
    for i, (idn, lab, v) in enumerate(rows):
        pos = idn.startswith("S")
        y = y0 + i * pitch + (0.15 if not pos and i >= len(S_) else 0)
        col = MINT if pos else CORAL
        T(ax, 0.6, y, idn, size=10.5, color=DIM, font="sans")
        T(ax, 1.05, y, lab, size=11.5, color=TXT)
        if pos:
            rrect(ax, zero, y - 0.085, v * sc, 0.17, r=0.02, fc=col, ec="none", z=5)
            T(ax, zero + v * sc + 0.08, y, f"+{v:.1f}".replace(".", ","), size=10, color=col, font="mono")
        else:
            rrect(ax, zero - v * sc, y - 0.085, v * sc, 0.17, r=0.02, fc=col, ec="none", z=5)
            T(ax, zero - v * sc - 0.08, y, f"−{v:.1f}".replace(".", ","), size=10, color=col, font="mono", ha="right")
    # Summen rechts
    px = 10.55
    rrect(ax, px, 2.5, 2.18, 4.3, r=0.1, fc=PANEL, ec=LINE, lw=1.0)
    T(ax, px + 1.09, 3.15, "−0,85", size=38, color=CORAL, font="disp", ha="center")
    T(ax, px + 1.09, 3.62, "gewichteter Mittelwert", size=10.5, color=MUTED, ha="center")
    T(ax, px + 1.09, 3.85, "Skala −3 bis +3", size=9, color=DIM, font="mono", ha="center")
    line(ax, [(px + 0.25, 4.2), (px + 1.93, 4.2)], color=LINE, lw=0.8)
    T(ax, px + 0.25, 4.6, "Stärken", size=12, color=MUTED)
    T(ax, px + 1.93, 4.6, "+38,3", size=15, color=MINT, font="disp", ha="right")
    T(ax, px + 0.25, 5.1, "Schwächen", size=12, color=MUTED)
    T(ax, px + 1.93, 5.1, "−123,3", size=15, color=CORAL, font="disp", ha="right")
    T(ax, px + 1.09, 5.85, "Punkte = Gewicht % ×\nAusprägung", size=9.5, color=DIM, font="mono", ha="center")
    save(fig, OUT % 11)


def s12():
    fig, ax = new_fig(); base(ax, 12, 2)
    T(ax, 0.6, 2.62, "CHANCEN", size=11, color=MINT, font="monob")
    T(ax, 6.9, 2.62, "RISIKEN", size=11, color=CORAL, font="monob")
    sc = 0.1
    for (items, x0, col, bx) in [(sorted(O_, key=lambda t: -t[2]), 0.6, MINT, 3.6), (sorted(T_, key=lambda t: -t[2]), 6.9, CORAL, 9.9)]:
        for i, (idn, lab, v) in enumerate(items):
            y = 3.0 + i * 0.335
            T(ax, x0, y, idn, size=10.5, color=DIM, font="sans")
            T(ax, x0 + 0.42, y, lab, size=12, color=TXT)
            rrect(ax, bx, y - 0.1, v * sc, 0.2, r=0.025, fc=col, ec="none", z=5)
            T(ax, bx + v * sc + 0.1, y, f"{v}", size=11, color=col, font="monob")
    # Waage
    total = 101 + 141; wtot = 12.13
    wm = wtot * 101 / total
    yb = 6.3
    rrect(ax, 0.6, yb, wm, 0.42, r=0.04, fc=MINT, ec=BG, lw=1.5, z=5)
    rrect(ax, 0.6 + wm, yb, wtot - wm, 0.42, r=0.04, fc=CORAL, ec=BG, lw=1.5, z=5)
    T(ax, 0.8, yb + 0.22, "Chancen 101", size=13.5, color=BG, font="sansb", z=9)
    T(ax, 0.6 + wtot - 0.2, yb + 0.22, "Risiken 141", size=13.5, color=BG, font="sansb", ha="right", z=9)
    T(ax, 0.6 + wtot / 2, yb - 0.28, "Saldo −40", size=16, color=TXT, font="disp", ha="center")
    save(fig, OUT % 12)


def s13():
    fig, ax = new_fig(); base(ax, 13, 2)
    quads = [
        (1.1, 2.5, "SO", "OFFENSIVE", MINT, [("SO1", "Nische Nicht-Heimlader", None), ("SO2", "Lücke nach P2P-Rückzug besetzen", None),
                                              ("SO3", "Planbarkeit statt Aufschlag", None), ("SO4", "Förderung gezielt nutzen", None)]),
        (5.35, 2.5, "ST", "ABSICHERUNG", BLUE, [("ST1", "Compliance by Design", 3), ("ST2", "Vertrauen, Rechtssicherheit", None),
                                                 ("ST3", "Fokus statt Konfrontation", None), ("ST4", "Kosten variabel", None)]),
        (1.1, 4.72, "WO", "AUFHOLEN", AMBER, [("WO1", "Kompetenz zukaufen", None), ("WO2", "Förderung gegen Finanz-Lücke", None),
                                              ("WO3", "Henne-Ei über Partner", None), ("WO4", "Primärdaten erheben", None)]),
        (5.35, 4.72, "WT", "DEFENSIVE", CORAL, [("WT1", "Gate vor Investition", 2), ("WT2", "Kapital schonen, Optionen", 1),
                                                ("WT3", "Sicherheit an Fachpartner", None), ("WT4", "Entscheidungsregister", None)]),
    ]
    for (x, y, code, nm, col, items) in quads:
        rrect(ax, x, y, 4.1, 2.08, r=0.1, fc=PANEL, ec=col if code == "WT" else LINE, lw=1.8 if code == "WT" else 1.0, z=2)
        T(ax, x + 0.3, y + 0.5, code, size=32, color=col, font="disp")
        T(ax, x + 1.25, y + 0.5, nm, size=10.5, color=col, font="monob")
        for i, (idn, lab, rank) in enumerate(items):
            yy = y + 1.0 + i * 0.255
            T(ax, x + 0.3, yy, idn, size=10.5, color=DIM, font="sans")
            T(ax, x + 0.85, yy, lab, size=11.5, color=TXT if rank else MUTED, font="sansb" if rank else "sans")
            if rank:
                circ(ax, x + 3.78, yy, 0.12, fc=col, ec="none", z=6)
                T(ax, x + 3.78, yy + 0.01, str(rank), size=9.5, color=BG, font="monob", ha="center", z=7)
    T(ax, 0.78, 3.54, "STÄRKEN", size=10, color=MUTED, font="monob", ha="center", rot=90)
    T(ax, 0.78, 5.76, "SCHWÄCHEN", size=10, color=MUTED, font="monob", ha="center", rot=90)
    # Kompass
    cx, cy = 11.3, 4.0; half = 1.25
    for (qx, qy, lab, tint) in [(1, -1, "SO", MINT), (-1, -1, "WO", AMBER), (1, 1, "ST", BLUE), (-1, 1, "WT", CORAL)]:
        x0 = cx if qx > 0 else cx - half; y0 = cy if qy > 0 else cy - half
        rrect(ax, x0, y0, half, half, r=0.02, fc=tint, ec="none", alpha=0.18 if lab == "WT" else 0.05, z=2)
        T(ax, x0 + (0.0 if qx < 0 else half), (cy - half - 0.17) if qy < 0 else (cy + half + 0.17), lab, size=11, color=tint, font="monob",
          ha="left" if qx < 0 else "right")
    line(ax, [(cx - half, cy), (cx + half, cy)], color=MUTED, lw=0.8, z=3)
    line(ax, [(cx, cy - half), (cx, cy + half)], color=MUTED, lw=0.8, z=3)
    px = lambda v: cx + v * 0.8
    py = lambda v: cy - v * 0.02
    bx, by = px(-0.85), py(-40)
    ax_, ay_ = px(-0.48), py(-25)
    arrow(ax, (bx, by), (ax_ - 0.05, ay_ + 0.04), color=MINT, lw=1.2, head=7)
    circ(ax, ax_, ay_, 0.07, fc="none", ec=MINT, lw=1.4, z=8)
    circ(ax, bx, by, 0.09, fc=CORAL, ec=BG, lw=1.0, z=8)
    T(ax, bx - 0.12, by + 0.2, "Basis", size=9.5, color=CORAL, font="mono", ha="left")
    T(ax, ax_ - 0.1, ay_ - 0.2, "Gates ok", size=9.5, color=MINT, font="mono", ha="right")
    T(ax, cx, cy - half - 0.2, "STÄRKEN ← INTERN → SCHWÄCHEN", size=8, color=DIM, font="mono", ha="center") if False else None
    T(ax, cx, cy + half + 0.5, "intern −0,85 · extern −40", size=9.5, color=MUTED, font="mono", ha="center")
    T(ax, cx, 6.1, "Position WT", size=22, color=CORAL, font="disp", ha="center")
    T(ax, cx, 6.38, "Schwächen und Risiken überwiegen", size=11, color=MUTED, ha="center", va="top")
    save(fig, OUT % 13)


def s14():
    fig, ax = new_fig(); base(ax, 14, 3, field_alpha=0.4)
    y = 4.05
    T(ax, 0.6, 2.72, "DREI GATES VOR DER INVESTITION (KRITERIEN: VORSCHLAG)", size=9.5, color=DIM, font="mono")
    xs = [1.25, 3.0, 4.75]
    labs = [("Eichrecht", "Eichamt bestätigt\nkWh-Abrechnung"), ("Recht + Zahlung", "Pfand, Auszahlung,\nReservierungsgebühr"), ("Nachfrage", "Umfrage und\nInterviews")]
    line(ax, [(0.9, y), (7.0, y)], color=LINE, lw=1.4, z=3)
    for i, (x, (t1, t2)) in enumerate(zip(xs, labs)):
        glow(ax, x, y, 0.2, alpha=0.06)
        circ(ax, x, y, 0.36, fc=PANEL, ec=MINT, lw=1.8, z=5)
        circ(ax, x, y, 0.46, ec=MINT, lw=0.6, alpha=0.5, z=5)
        T(ax, x, y + 0.02, str(i + 1), size=20, color=MINT, font="disp", ha="center", z=9)
        T(ax, x, y + 0.85, t1, size=13.5, color=TXT, font="sansb", ha="center")
        T(ax, x, y + 1.38, t2, size=11, color=MUTED, ha="center", va="top")
    arrow(ax, (5.35, y), (6.6, y), color=MINT, lw=1.6, head=10)
    glow(ax, 7.3, y, 0.55, alpha=0.1)
    circ(ax, 7.3, y, 0.55, fc=MINT, ec="none", z=5)
    circ(ax, 7.3, y, 0.72, ec=MINT, lw=0.8, alpha=0.6, z=5)
    circ(ax, 7.3, y, 0.9, ec=MINT, lw=0.5, alpha=0.35, z=5)
    T(ax, 7.3, y + 0.02, "2027", size=17, color=BG, font="disp", ha="center", z=9)
    T(ax, 7.3, y + 1.15, "Pilot", size=13.5, color=TXT, font="sansb", ha="center")
    T(ax, 7.3, y + 1.4, "Mannheim–Heidelberg\n+ Odenwald", size=11, color=MUTED, ha="center", va="top")
    T(ax, 0.6, 6.5, "Sprechen Sie uns heute an", size=21, color=MINT, font="disp")
    # Ask-Karte
    x0 = 8.75
    rrect(ax, x0, 2.5, 3.98, 4.3, r=0.12, fc=PANEL, ec=MINT, lw=1.3)
    T(ax, x0 + 0.3, 2.85, "WIR SUCHEN", size=11, color=MINT, font="monob")
    asks = [(ic_house, "Pilot-Anbieter", "Wallbox-Besitzer in der\nRegion Mannheim–Heidelberg\nund im Odenwald"),
            (ic_pin, "Förderer", "Hochschule, Gründerzentren\nund Förderprogramme"),
            (ic_shield, "Fachwissen", "Eichrecht, Zahlungsverkehr\nund Recht")]
    for i, (icon, t1, t2) in enumerate(asks):
        yy = 3.65 + i * 1.12
        circ(ax, x0 + 0.62, yy, 0.34, fc=PANEL2, ec=MINT, lw=1.0, z=4)
        icon(ax, x0 + 0.62, yy, 0.18)
        T(ax, x0 + 1.15, yy - 0.28, t1, size=15, color=TXT, font="sansb")
        T(ax, x0 + 1.15, yy - 0.07, t2, size=11, color=MUTED, va="top")
    save(fig, OUT % 14)
