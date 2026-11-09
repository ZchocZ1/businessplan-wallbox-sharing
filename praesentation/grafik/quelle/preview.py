"""Vorschau: Grafik + native Texte (Arial-Metrik) und Ueberlauf-Pruefung."""
import json, sys
from PIL import Image, ImageDraw, ImageFont
sys.path.insert(0, ".")
import layout
DPI = 180
F = {True: "/System/Library/Fonts/Supplemental/Arial Bold.ttf", False: "/System/Library/Fonts/Supplemental/Arial.ttf"}
LH = 1.2
S = json.load(open("content.json"))
problems = []
for s in S:
    n = s["n"]
    im = Image.open(f"art/slide{n:02d}.png").convert("RGB")
    d = ImageDraw.Draw(im)
    for b in layout.boxes(s):
        pt = b["size"]; px = pt * DPI / 72
        font = ImageFont.truetype(F[b["bold"]], int(round(px)))
        maxw = b["w"] * DPI
        lines = []
        for para in b["text"].split("\n"):
            cur = ""
            for word in para.split(" "):
                t = (cur + " " + word).strip()
                if font.getlength(t) + (len(t) * b.get("spc", 0) * DPI / 72) <= maxw:
                    cur = t
                else:
                    lines.append(cur); cur = word
            lines.append(cur)
        need = len(lines) * pt * LH / 72
        if need > b["h"] + 0.001:
            problems.append(f"Folie {n} {b['role']}: {len(lines)} Zeilen, braucht {need:.2f} in, Box {b['h']:.2f} in")
        y = b["y"] * DPI
        col = "#" + b["color"]
        for ln in lines:
            d.text((b["x"] * DPI, y), ln, font=font, fill=col)
            y += px * LH
    im.save(f"preview/p{n:02d}.png")
print("\n".join(problems) if problems else "keine Ueberlaeufe")
