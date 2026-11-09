from lib import *


def s01():
    fig, ax = new_fig(); base(ax, 1, 0, field_alpha=0.5)
    hubs = {"MANNHEIM": (7.87, 3.86, "49.49°N 8.47°E"), "HEIDELBERG": (9.34, 4.49, "49.40°N 8.67°E"),
            "ODENWALD": (11.65, 2.65, "49.66°N 9.00°E")}
    rng = np.random.RandomState(11)
    dots = []
    zones = [(7.3, 3.1, 9.0, 3.65), (8.9, 4.65, 10.8, 5.2), (7.0, 5.4, 8.6, 5.75), (10.3, 3.65, 12.1, 3.95), (10.3, 1.3, 13.0, 1.75),
             (11.2, 3.2, 13.0, 3.7), (9.0, 2.3, 11.1, 3.1)]
    while len(dots) < 90:
        x, y = rng.uniform(7.1, 12.6), rng.uniform(2.1, 5.75)
        if all((x - hx) ** 2 + (y - hy) ** 2 > 0.3 for hx, hy, _ in hubs.values()) and not any(a < x < c and b < y < d for a, b, c, d in zones):
            dots.append((x, y))
    for (x, y) in dots:
        circ(ax, x, y, 0.03, fc=DIM, ec="none", z=3, alpha=0.8)
    lit = rng.choice(len(dots), 14, replace=False)
    for i in lit:
        x, y = dots[i]
        circ(ax, x, y, 0.055, fc=MINT, ec="none", z=4)
        circ(ax, x, y, 0.13, ec=MINT, lw=0.6, alpha=0.5, z=4)
    # Verbindungen
    names = list(hubs)
    arrow(ax, hubs["MANNHEIM"][:2], hubs["HEIDELBERG"][:2], color=MINT, lw=1.2, rad=-0.25, head=1)
    arrow(ax, hubs["HEIDELBERG"][:2], hubs["ODENWALD"][:2], color=MINT, lw=1.0, rad=0.22, head=1, ls=(0, (3, 3)))
    for nm, (x, y, co) in hubs.items():
        glow(ax, x, y, 0.28)
        circ(ax, x, y, 0.09, fc=MINT, ec="none", z=7)
        circ(ax, x, y, 0.22, ec=MINT, lw=1.0, z=6)
        circ(ax, x, y, 0.42, ec=MINT, lw=0.5, alpha=0.5, z=6)
        if nm == "MANNHEIM":
            T(ax, x - 0.5, y - 0.62, nm, size=10, color=TXT, font="monob")
            T(ax, x - 0.5, y - 0.4, co, size=8.5, color=MUTED, font="mono")
        elif nm == "HEIDELBERG":
            T(ax, x + 0.3, y + 0.5, nm, size=10, color=TXT, font="monob")
            T(ax, x + 0.3, y + 0.72, co, size=8.5, color=MUTED, font="mono")
        else:
            T(ax, x - 1.08, y - 0.1, nm, size=10, color=TXT, font="monob", ha="right")
            T(ax, x - 1.08, y + 0.12, co, size=8.5, color=MUTED, font="mono", ha="right")
    # Pilot-Ringe
    circ(ax, 8.6, 4.18, 1.25, ec=MINT, lw=0.8, alpha=0.5, ls=(0, (2, 4)))
    T(ax, 7.2, 5.55, "STADT-PILOT", size=9, color=MINT, font="mono")
    circ(ax, 11.65, 2.65, 0.95, ec=AMBER, lw=0.8, alpha=0.6, ls=(0, (2, 4)))
    T(ax, 11.65, 1.55, "LAND-PILOT", size=9, color=AMBER, font="mono", ha="center")
    # Hook: Zahl + 1 von 5
    T(ax, 0.6, 4.25, "2.034.260", size=70, color=TXT, font="disp")
    T(ax, 0.62, 4.95, "reine E-Autos in Deutschland (1. Januar 2026)", size=14, color=MUTED, font="sans")
    for i in range(5):
        on = (i == 4)
        ic_car(ax, 0.95 + i * 1.0, 5.82, 0.3, c=MINT if on else DIM, lw=1.5, fill=on)
    T(ax, 0.62, 6.38, "Rund jedes fünfte lädt nicht zu Hause", size=14, color=MINT, font="sansb")
    save(fig, OUT % 1)


def s02():
    fig, ax = new_fig(); base(ax, 2, 1)
    cy = 4.35
    nodes = [(1.5, 0.7, ic_house, "Wallbox-Besitzer", "privat und gewerblich"),
             (3.6, 0.9, ic_bolt, "WallShare", "reservieren · abrechnen"),
             (5.7, 0.7, ic_car, "E-Auto-Fahrer", "ohne Heimladen")]
    for i, (x, r, icon, t1, t2) in enumerate(nodes):
        main = (i == 1)
        if main:
            glow(ax, x, cy, 0.45)
        circ(ax, x, cy, r, fc=PANEL, ec=MINT if main else LINE, lw=2.0 if main else 1.2, z=4)
        if main:
            circ(ax, x, cy, r + 0.14, ec=MINT, lw=0.6, alpha=0.5, z=4)
            ic_bolt(ax, x, cy, 0.42, c=MINT, lw=2.0)
        elif icon is ic_house:
            ic_house(ax, x, cy, 0.34, c=TXT)
        else:
            ic_car(ax, x, cy - 0.05, 0.36, c=TXT)
        T(ax, x, cy + r + 0.38, t1, size=14, color=TXT, font="sansb", ha="center")
        T(ax, x, cy + r + 0.66, t2, size=11, color=MUTED, font="sans", ha="center")
    arrow(ax, (2.25, cy), (2.7, cy), color=MINT, lw=1.6, both=True, head=9)
    arrow(ax, (4.5 + 0.14, cy), (5.0, cy), color=MINT, lw=1.6, both=True, head=9)
    chip(ax, 2.3, 6.2, 2.6, 0.46, "0 eigene Ladesäulen", color=MINT, size=14)
    # Roadmap
    by = 5.0
    line(ax, [(6.9, by), (12.5, by)], color=LINE, lw=1.2)
    st = [(7.5, "2027", "Pilot in Mannheim–\nHeidelberg + Odenwald", 0.45, 4),
          (9.6, "2028–29", "weitere Regionen,\nBreak-even je Region", 0.72, 12),
          (11.7, "2030–31", "bundesweit,\nDACH nur Option", 0.92, 30)]
    rng = np.random.RandomState(4)
    for i, (x, yr, lab, rad, cnt) in enumerate(st):
        on = (i == 0)
        circ(ax, x, by, 0.12, fc=MINT if on else BG, ec=MINT, lw=1.6, z=6)
        cx, cy2 = x, by - 0.35 - rad
        placed = []
        tries = 0
        while len(placed) < cnt and tries < 4000:
            tries += 1
            a = rng.uniform(0, 6.283); rr = rad * np.sqrt(rng.uniform(0, 1))
            px, py = cx + rr * np.cos(a), cy2 + rr * np.sin(a)
            if all((px - qx) ** 2 + (py - qy) ** 2 > 0.04 for qx, qy in placed):
                placed.append((px, py))
        for (px, py) in placed:
            circ(ax, px, py, 0.045, fc=MINT if on else MUTED, ec="none", z=5, alpha=1 if on else 0.75)
        if len(placed) > 2:
            for k in range(min(len(placed) - 1, 9)):
                line(ax, [placed[k], placed[(k * 3 + 1) % len(placed)]], color=MINT, lw=0.4, alpha=0.35, z=4)
        T(ax, x, by + 0.38, yr, size=22, color=MINT if on else TXT, font="disp", ha="center")
        T(ax, x, by + 0.9, lab, size=11.5, color=MUTED, font="sans", ha="center", va="top")
    save(fig, OUT % 2)


def s03():
    fig, ax = new_fig(); base(ax, 3, 1)
    cards = [(0.6, "FAHRER", [
        (ic_cal, "Reservieren statt suchen", "festes Zeitfenster, auch über Nacht"),
        (ic_pin, "Laden, wo Säulen fehlen", "Wohngebiet und ländlicher Raum")],
        [("F1 Mieter · Kern", 1.9), ("F2 Land", 1.1), ("F3 unterwegs", 1.5)], "Preis: kein Versprechen", AMBER),
        (6.78, "ANBIETER", [
        (ic_shield, "Rundum sorglos", "Abrechnung · Versicherung · Support"),
        (ic_euro, "Einnahmen als Möglichkeit", "keine Euro-Zahl ohne Beleg")],
        [("A1 Einkommen", 1.5), ("A2 Service", 1.3), ("A3 Nachhaltig", 1.55)], "Akquise-Schwerpunkt: PV-Anlagen", AMBER)]
    for (x, head, rows, chips, note, ncol) in cards:
        rrect(ax, x, 2.5, 5.95, 4.3, r=0.12, fc=PANEL, ec=LINE, lw=1.0)
        T(ax, x + 0.35, 2.85, head, size=12, color=MINT, font="monob")
        for i, (icon, t1, t2) in enumerate(rows):
            yy = 3.65 + i * 0.95
            circ(ax, x + 0.62, yy, 0.38, fc=PANEL2, ec=MINT, lw=1.0, z=4)
            if icon is ic_euro:
                T(ax, x + 0.62, yy + 0.02, "€", size=21, color=MINT, font="disp", ha="center", z=9)
            else:
                icon(ax, x + 0.62, yy, 0.2)
            T(ax, x + 1.25, yy - 0.14, t1, size=16, color=TXT, font="sansb")
            T(ax, x + 1.25, yy + 0.19, t2, size=12, color=MUTED, font="sans")
        line(ax, [(x + 0.35, 5.35), (x + 5.6, 5.35)], color=LINE, lw=0.8)
        T(ax, x + 0.35, 5.62, "KUNDENSEGMENTE (ANNAHME)", size=9, color=DIM, font="mono")
        cx = x + 0.35
        for (lab, w) in chips:
            chip(ax, cx, 5.82, w, 0.4, lab, color=MINT if "Kern" in lab or lab.startswith("A1") else MUTED, size=11.5)
            cx += w + 0.15
        if "PV" in note:
            ic_sun(ax, x + 0.55, 6.5, 0.17, c=AMBER, lw=1.3)
            T(ax, x + 0.9, 6.5, note, size=12.5, color=AMBER, font="sansb")
        else:
            line(ax, [(x + 0.42, 6.4), (x + 0.62, 6.6)], color=AMBER, lw=1.8)
            line(ax, [(x + 0.42, 6.6), (x + 0.62, 6.4)], color=AMBER, lw=1.8)
            T(ax, x + 0.9, 6.5, note, size=12.5, color=AMBER, font="sansb")
    save(fig, OUT % 3)


def s04():
    fig, ax = new_fig(); base(ax, 4, 1)
    # Legende
    rrect(ax, 0.6, 2.58, 0.32, 0.2, r=0.04, fc="none", ec=MINT, lw=1.4)
    T(ax, 1.05, 2.68, "eigener Kern", size=11.5, color=TXT)
    rrect(ax, 2.45, 2.58, 0.32, 0.2, r=0.04, fc="none", ec=MUTED, lw=1.0, ls=(0, (3, 2)))
    T(ax, 2.9, 2.68, "Partner (Kandidaten, nicht geprüft)", size=11.5, color=TXT)
    rrect(ax, 6.1, 2.58, 0.32, 0.2, r=0.04, fc="none", ec=AMBER, lw=1.4)
    T(ax, 6.55, 2.68, "unter Vorbehalt (Gate)", size=11.5, color=TXT)
    ys, hh = 3.3, 1.1
    nodes = [(0.6, "Wallbox-\nBesitzer", ic_house, TXT, LINE, "-"), (3.84, "Gadget", ic_plug, AMBER, AMBER, "-"),
             (7.08, "WallShare\nPlattform", ic_bolt, MINT, MINT, "-"), (10.32, "E-Auto-\nFahrer", ic_car, TXT, LINE, "-")]
    cx = []
    for i, (x, lab, icon, ic_c, ec, ls) in enumerate(nodes):
        main = (i == 2)
        y0, h0 = (ys - 0.2, 1.5) if main else (ys, hh)
        if main:
            glow(ax, x + 1.2, y0 + h0 / 2, 0.8, alpha=0.08)
        rrect(ax, x, y0, 2.4, h0, r=0.1, fc=PANEL, ec=ec, lw=1.8 if main or i == 1 else 1.0, z=4)
        icon(ax, x + 0.5, y0 + h0 / 2, 0.28, c=ic_c, lw=1.7)
        T(ax, x + 0.95, y0 + h0 / 2, lab, size=14, color=TXT, font="sansb", va="center")
        cx.append(x + 1.2)
    # Pfeile
    for i in range(3):
        x0 = nodes[i][0] + 2.4; x1 = nodes[i + 1][0]
        arrow(ax, (x0 + 0.06, ys + 0.55), (x1 - 0.06, ys + 0.55), color=MINT, lw=1.5, head=9)
    T(ax, 7.08 + 1.2, ys + 1.02, "App · Radar · Reservierung", size=9.5, color=MINT, font="mono", ha="center")
    # Partner-Chips
    chips = [("Auftragsfertigung", 1, 1), ("Fulfillment-Dienst", 2, 1), ("Zahlungsdienst", 3, 2),
             ("Backend + EU-Hosting", 4, 2), ("Versicherer", 5, 2)]
    for (lab, idx, target) in chips:
        ccx = 0.6 + idx * 2.05 + 0.925
        tx = cx[target]
        y_node_bottom = 4.6 if target == 2 else ys + hh
        line(ax, [(ccx, 5.78), (ccx, 5.3), (tx, 5.3), (tx, y_node_bottom)], color=MUTED, lw=0.9, alpha=0.8, z=3)
        rrect(ax, ccx - 0.925, 5.78, 1.85, 0.5, r=0.08, fc=PANEL, ec=MUTED, lw=1.0, ls=(0, (3, 2)), z=4)
        T(ax, ccx, 6.03, lab, size=11, color=TXT, font="sans", ha="center")
    T(ax, 0.6, 6.03, "ZUGEKAUFT", size=10, color=MUTED, font="mono")
    save(fig, OUT % 4)


def s05():
    fig, ax = new_fig(); base(ax, 5, 1)
    tiles = [(ic_pin, "D-1", "Vermittlung", "Anbieter finden Fahrer", MINT, "-"),
             (ic_euro, "D-2", "Abrechnung", "kWh, Auszahlung, Pfand", MINT, "-"),
             (ic_shield, "D-3", "Absicherung", "Versicherung, Support", MINT, "-"),
             (ic_radar, "D-6", "Radar", "Karte, Verfügbarkeit", MINT, "-"),
             (ic_plug, "D-5", "Gadget", "kostenlos gegen Pfand", AMBER, "-"),
             (ic_sun, "D-4", "Energie", "PV-Strom, nach Pilot", AMBER, (0, (3, 2)))]
    for i, (icon, idn, t1, t2, col, ls) in enumerate(tiles):
        x = 0.6 + (i % 3) * 2.27; y = 2.55 + (i // 3) * 1.75
        rrect(ax, x, y, 2.07, 1.55, r=0.1, fc=PANEL, ec=col if ls != "-" or col == AMBER else LINE, lw=1.0, z=3, ls=ls)
        if icon is ic_euro:
            circ(ax, x + 0.45, y + 0.5, 0.26, ec=col, lw=1.5, z=8)
            T(ax, x + 0.45, y + 0.51, "€", size=17, color=col, font="disp", ha="center", z=9)
        elif icon is ic_sun:
            ic_sun(ax, x + 0.45, y + 0.5, 0.26, c=col, lw=1.3)
        else:
            icon(ax, x + 0.45, y + 0.5, 0.24, c=col, lw=1.5)
        T(ax, x + 1.9, y + 0.25, idn, size=9, color=DIM, font="mono", ha="right")
        T(ax, x + 0.2, y + 1.02, t1, size=14, color=TXT, font="sansb")
        T(ax, x + 0.2, y + 1.3, t2, size=10.5, color=MUTED, font="sans")
    chip(ax, 0.6, 6.0, 6.61, 0.5, "Pilot: kein Abo · keine Werbung · Partnerprovisionen später", color=MUTED, size=12.5, font="sans", tc=TXT)
    # Erlös
    px = 7.75; pw = 4.98
    T(ax, px, 2.7, "Fahrer zahlt 110 € je Wallbox und Monat", size=15, color=TXT, font="sansb")
    T(ax, px, 3.02, "Szenario realistisch, brutto, Annahmen", size=11, color=MUTED, font="sans")
    sc = pw / 110.0
    segs = [(93.5, "#1F7A63"), (6.48, CORAL), (10.02, MINT)]
    x = px
    for v, col in segs:
        rrect(ax, x, 3.4, v * sc, 0.6, r=0.02, fc=col, ec=BG, lw=1.0, z=5)
        x += v * sc
    T(ax, px + 0.2, 3.7, "Anbieter 93,50 €", size=14, color=TXT, font="sansb", z=9)
    xz = px + 93.5 * sc + 6.48 * sc / 2; xd = px + (93.5 + 6.48) * sc + 10.02 * sc / 2
    line(ax, [(xz, 4.0), (xz, 4.3)], color=CORAL, lw=1.0)
    T(ax, xz + 0.12, 4.3, "Zahlungskosten 6,48 €", size=12.5, color=CORAL, font="sansb", ha="right")
    line(ax, [(xd, 4.0), (xd, 4.68)], color=MINT, lw=1.0)
    T(ax, xd + 0.12, 4.68, "Deckungsbeitrag 10,02 €", size=12.5, color=MINT, font="sansb", ha="right")
    T(ax, px + pw, 5.0, "zusammen 16,50 € Provision im Preis", size=10.5, color=MUTED, font="sans", ha="right")
    lines = ["Provision im kWh-Preis enthalten", "Zwei Preise: PV-Strom · Normalstrom", "Reservierungsgebühr nur bei Nichtnutzung"]
    for i, s in enumerate(lines):
        chip(ax, px, 5.28 + i * 0.54, pw, 0.44, s, color=LINE, size=12.5, font="sans", tc=TXT)
    save(fig, OUT % 5)


OUT = "../slide%02d.png"
