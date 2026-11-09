"""Textboxen (Zoll) fuer die nativen Texte; gemeinsame Quelle fuer Vorschau und pptx."""
import json
BG = "0A0F1E"; TXT = "E9EEF9"; MUTED = "8FA0C6"; MINT = "2DF2B6"


def boxes(s):
    n = s["n"]
    out = []
    if n == 1:
        out.append(dict(role="title", x=0.6, y=1.0, w=6.6, h=1.2, text=s["title"], size=62, bold=True, color=TXT))
        out.append(dict(role="sub", x=0.6, y=2.25, w=6.2, h=1.0, text=s["sub"], size=24, bold=False, color=TXT))
        out.append(dict(role="meta", x=0.6, y=3.25, w=6.4, h=0.35, text="Arbeitsname · Investorenpräsentation · Entwurf, Stand 09.11.2026",
                        size=13, bold=True, color=MINT))
    else:
        out.append(dict(role="kicker", x=0.6, y=0.72, w=9.0, h=0.3, text=s["kicker"], size=11, bold=True, color=MINT, spc=2))
        out.append(dict(role="title", x=0.6, y=1.02, w=12.13, h=0.98, text=s["title"], size=28, bold=True, color=TXT))
        out.append(dict(role="sub", x=0.6, y=2.0, w=12.13, h=0.4, text=s["sub"], size=14, bold=False, color=MUTED))
    out.append(dict(role="source", x=0.6, y=6.93, w=9.6, h=0.42, text=s["source"], size=10, bold=False, color=MUTED))
    return out


if __name__ == "__main__":
    S = json.load(open("content.json"))
    for s in S:
        s["boxes"] = boxes(s)
    json.dump(S, open("content_full.json", "w"), ensure_ascii=False, indent=1)
    print("ok")
