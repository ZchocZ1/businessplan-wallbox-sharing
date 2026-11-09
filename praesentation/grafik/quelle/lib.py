"""Gemeinsame Bausteine fuer die Folien-Grafiken (Quiet Voltage).
Koordinaten in Zoll, Ursprung oben links, Folie 13.333 x 7.5 (16:9)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon, Wedge, Rectangle, FancyArrowPatch
from matplotlib.font_manager import FontProperties
from matplotlib.path import Path
from matplotlib.patches import PathPatch

W, H = 13.333, 7.5
DPI = 180
FD = "/Users/bengerlach/.claude/skills/canvas-design/canvas-fonts/"
FONTS = {
    "sans": FD + "InstrumentSans-Regular.ttf",
    "sansb": FD + "InstrumentSans-Bold.ttf",
    "mono": FD + "JetBrainsMono-Regular.ttf",
    "monob": FD + "JetBrainsMono-Bold.ttf",
    "disp": FD + "Outfit-Bold.ttf",
    "dispr": FD + "Outfit-Regular.ttf",
    "jura": FD + "Jura-Medium.ttf",
}
BG = "#0A0F1E"; PANEL = "#101830"; PANEL2 = "#16213F"; LINE = "#2A3A66"; GRIDC = "#1B2749"
TXT = "#E9EEF9"; MUTED = "#8FA0C6"; DIM = "#5F6F96"
MINT = "#2DF2B6"; AMBER = "#FFB347"; CORAL = "#FF6B7A"; BLUE = "#5B8CFF"

AIDA = [("A", "ATTENTION"), ("I", "INTEREST"), ("D", "DESIRE"), ("A", "ACTION")]


def fp(name, size):
    return FontProperties(fname=FONTS[name], size=size)


def T(ax, x, y, s, size=12, color=TXT, font="sans", ha="left", va="center", alpha=1.0, z=10, rot=0):
    return ax.text(x, y, s, fontproperties=fp(font, size), color=color, ha=ha, va=va, alpha=alpha, zorder=z, rotation=rot)


def circ(ax, x, y, r, fc="none", ec=MINT, lw=1.2, alpha=1.0, z=5, ls="-"):
    p = Circle((x, y), r, fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z, ls=ls)
    ax.add_patch(p); return p


def rrect(ax, x, y, w, h, r=0.06, fc=PANEL, ec=LINE, lw=1.0, alpha=1.0, z=3, ls="-"):
    p = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}", fc=fc, ec=ec, lw=lw,
                       alpha=alpha, zorder=z, ls=ls)
    ax.add_patch(p); return p


def line(ax, pts, color=LINE, lw=1.0, alpha=1.0, z=4, ls="-", cap="round"):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ax.plot(xs, ys, color=color, lw=lw, alpha=alpha, zorder=z, ls=ls, solid_capstyle=cap)


def poly(ax, pts, fc=MINT, ec="none", lw=1, alpha=1.0, z=5):
    p = Polygon(pts, closed=True, fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z)
    ax.add_patch(p); return p


def glow(ax, x, y, r, color=MINT, n=6, alpha=0.10, z=2):
    for i in range(n, 0, -1):
        ax.add_patch(Circle((x, y), r * i / n * 2.4, fc=color, ec="none", alpha=alpha * (1 - i / (n + 1)) * 1.2, zorder=z))


def arrow(ax, p0, p1, color=MUTED, lw=1.3, rad=0.0, head=8, z=6, both=False, ls="-"):
    st = "<|-|>" if both else "-|>"
    a = FancyArrowPatch(p0, p1, arrowstyle=st, mutation_scale=head, lw=lw, color=color,
                        connectionstyle=f"arc3,rad={rad}", zorder=z, shrinkA=0, shrinkB=0, ls=ls)
    ax.add_patch(a); return a


# ---------- Icons (Umriss, Mitte x,y, Groesse s = Halbbreite) ----------
def ic_bolt(ax, x, y, s, c=MINT, lw=1.6, fill=False):
    pts = [(0.15, -1), (-0.55, 0.12), (-0.05, 0.12), (-0.2, 1), (0.55, -0.15), (0.05, -0.15)]
    pts = [(x + px * s, y + py * s) for px, py in pts]
    poly(ax, pts, fc=c if fill else "none", ec=c, lw=lw, z=8)


def ic_pin(ax, x, y, s, c=MINT, lw=1.6):
    circ(ax, x, y - 0.25 * s, 0.62 * s, ec=c, lw=lw, z=8)
    poly(ax, [(x - 0.5 * s, y + 0.1 * s), (x + 0.5 * s, y + 0.1 * s), (x, y + 1.0 * s)], fc="none", ec=c, lw=lw, z=8)
    circ(ax, x, y - 0.25 * s, 0.2 * s, fc=c, ec=c, lw=0.5, z=9)


def ic_cal(ax, x, y, s, c=MINT, lw=1.6):
    rrect(ax, x - s, y - 0.85 * s, 2 * s, 1.85 * s, r=0.05 * s, fc="none", ec=c, lw=lw, z=8)
    line(ax, [(x - s, y - 0.3 * s), (x + s, y - 0.3 * s)], color=c, lw=lw, z=8)
    for dx in (-0.55, 0.55):
        line(ax, [(x + dx * s, y - 1.1 * s), (x + dx * s, y - 0.65 * s)], color=c, lw=lw, z=8)
    for i in range(3):
        for j in range(2):
            circ(ax, x + (-0.55 + 0.55 * i) * s, y + (0.1 + 0.45 * j) * s, 0.09 * s, fc=c, ec=c, lw=0.3, z=9)


def ic_shield(ax, x, y, s, c=MINT, lw=1.6):
    pts = [(-0.8, -0.8), (0, -1.05), (0.8, -0.8), (0.8, 0.1), (0, 1.05), (-0.8, 0.1)]
    poly(ax, [(x + px * s, y + py * s) for px, py in pts], fc="none", ec=c, lw=lw, z=8)
    line(ax, [(x - 0.35 * s, y - 0.05 * s), (x - 0.05 * s, y + 0.3 * s), (x + 0.42 * s, y - 0.3 * s)], color=c, lw=lw, z=9)


def ic_house(ax, x, y, s, c=MINT, lw=1.6):
    poly(ax, [(x - s, y + 0.9 * s), (x - s, y - 0.1 * s), (x, y - 0.95 * s), (x + s, y - 0.1 * s), (x + s, y + 0.9 * s)],
         fc="none", ec=c, lw=lw, z=8)
    rrect(ax, x - 0.22 * s, y + 0.25 * s, 0.44 * s, 0.65 * s, r=0.03 * s, fc="none", ec=c, lw=lw * 0.8, z=8)


def ic_car(ax, x, y, s, c=MINT, lw=1.6, fill=False):
    rrect(ax, x - 1.1 * s, y - 0.05 * s, 2.2 * s, 0.7 * s, r=0.18 * s, fc=c if fill else "none", ec=c, lw=lw, z=8)
    poly(ax, [(x - 0.7 * s, y - 0.05 * s), (x - 0.4 * s, y - 0.55 * s), (x + 0.4 * s, y - 0.55 * s), (x + 0.75 * s, y - 0.05 * s)],
         fc=c if fill else "none", ec=c, lw=lw, z=8)
    for dx in (-0.62, 0.62):
        circ(ax, x + dx * s, y + 0.68 * s, 0.22 * s, fc=BG, ec=c, lw=lw, z=9)


def ic_plug(ax, x, y, s, c=MINT, lw=1.6):
    rrect(ax, x - 0.55 * s, y - 0.9 * s, 1.1 * s, 1.35 * s, r=0.14 * s, fc="none", ec=c, lw=lw, z=8)
    for dx in (-0.22, 0.22):
        line(ax, [(x + dx * s, y - 0.9 * s), (x + dx * s, y - 1.25 * s)], color=c, lw=lw, z=8)
    line(ax, [(x, y + 0.45 * s), (x, y + 1.0 * s)], color=c, lw=lw, z=8)


def ic_radar(ax, x, y, s, c=MINT, lw=1.6):
    for r in (0.35, 0.7, 1.05):
        circ(ax, x, y, r * s, ec=c, lw=lw * 0.7, alpha=0.8, z=8)
    line(ax, [(x, y), (x + 0.75 * s, y - 0.75 * s)], color=c, lw=lw, z=9)
    circ(ax, x + 0.55 * s, y - 0.3 * s, 0.11 * s, fc=c, ec=c, lw=0.3, z=9)


def ic_sun(ax, x, y, s, c=AMBER, lw=1.6):
    circ(ax, x, y, 0.42 * s, ec=c, lw=lw, z=8)
    for k in range(8):
        a = k * np.pi / 4
        line(ax, [(x + 0.62 * s * np.cos(a), y + 0.62 * s * np.sin(a)), (x + 0.95 * s * np.cos(a), y + 0.95 * s * np.sin(a))],
             color=c, lw=lw, z=8)


def ic_euro(ax, x, y, s, c=MINT, lw=1.6):
    circ(ax, x, y, s, ec=c, lw=lw, z=8)
    T(ax, x, y + 0.02, "€", size=s * 26, color=c, font="disp", ha="center", z=9)


def ic_check(ax, x, y, s, c=MINT, lw=1.8):
    line(ax, [(x - 0.45 * s, y), (x - 0.1 * s, y + 0.38 * s), (x + 0.5 * s, y - 0.4 * s)], color=c, lw=lw, z=9)


# ---------- Basis (Hintergrund, Raster, Rahmen, AIDA) ----------
def new_fig():
    fig = plt.figure(figsize=(W, H), dpi=DPI, facecolor=BG)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W); ax.set_ylim(H, 0); ax.axis("off")
    return fig, ax


def contour_field(ax, alpha=0.30, levels=16, seed=3, strength=1.0):
    xs = np.linspace(0, W, 260); ys = np.linspace(0, H, 150)
    X, Y = np.meshgrid(xs, ys)
    rng = np.random.RandomState(seed)
    Z = np.zeros_like(X)
    for _ in range(5):
        kx, ky = rng.uniform(0.25, 0.7, 2); ph = rng.uniform(0, 6.28, 2); a = rng.uniform(0.5, 1.0)
        Z += a * np.sin(kx * X * 2.0 + ph[0]) * np.cos(ky * Y * 2.0 + ph[1])
    Z += 0.55 * np.exp(-(((X - 10.4) / 2.6) ** 2 + ((Y - 3.7) / 1.9) ** 2)) * 3.0 * strength
    ax.contour(X, Y, Z, levels=levels, colors=[LINE], linewidths=0.5, alpha=alpha, zorder=0)


def base(ax, n, aida, title_slide=False, field_alpha=0.28):
    # Glow (weiche Tiefe)
    g = np.zeros((90, 160, 4))
    yy, xx = np.mgrid[0:90, 0:160]
    d = np.sqrt(((xx - 125) / 90.0) ** 2 + ((yy - 18) / 55.0) ** 2)
    g[..., 0] = 0.10; g[..., 1] = 0.35; g[..., 2] = 0.55
    g[..., 3] = np.clip(0.16 * np.exp(-d * d * 2.2), 0, 0.16)
    ax.imshow(g, extent=[0, W, H, 0], zorder=0.2, aspect="auto", interpolation="bilinear")
    contour_field(ax, alpha=field_alpha)
    # feine Kreuzmarken auf 1-Zoll-Raster
    for gx in np.arange(0.6, W - 0.2, 1.0):
        for gy in np.arange(0.5, H - 0.2, 1.0):
            line(ax, [(gx - 0.04, gy), (gx + 0.04, gy)], color=GRIDC, lw=0.6, alpha=0.9, z=0.5)
            line(ax, [(gx, gy - 0.04), (gx, gy + 0.04)], color=GRIDC, lw=0.6, alpha=0.9, z=0.5)
    # Passermarken an den Ecken
    m, L = 0.26, 0.2
    for (cx, cy, sx, sy) in [(m, m, 1, 1), (W - m, m, -1, 1), (m, H - m, 1, -1), (W - m, H - m, -1, -1)]:
        line(ax, [(cx, cy + sy * L), (cx, cy), (cx + sx * L, cy)], color=DIM, lw=0.8, alpha=0.8, z=1)
    # Folien-Kennung unten rechts
    T(ax, W - 0.6, H - 0.27, f"WALLSHARE · QV-{n:02d}/14", size=8, color=DIM, font="mono", ha="right")
    # AIDA-Leiste oben rechts
    x0 = W - 0.6 - 4 * 0.46 + 0.1
    for i, (ch, lab) in enumerate(AIDA):
        bx = x0 + i * 0.46
        on = (i == aida)
        rrect(ax, bx, 0.42, 0.34, 0.34, r=0.05, fc=MINT if on else "none", ec=MINT if on else LINE, lw=1.0, z=6)
        T(ax, bx + 0.17, 0.595, ch, size=11, color=BG if on else MUTED, font="monob", ha="center", z=7)
    T(ax, W - 0.6, 0.93, AIDA[aida][1], size=8.5, color=MINT, font="mono", ha="right")


def chip(ax, x, y, w, h, label, color=MINT, fc=None, size=12, font="sansb", tc=None, ls="-"):
    rrect(ax, x, y, w, h, r=h / 2, fc=fc if fc else "none", ec=color, lw=1.1, z=6, ls=ls)
    T(ax, x + w / 2, y + h / 2 + 0.01, label, size=size, color=tc if tc else color, font=font, ha="center", z=7)


def save(fig, path):
    fig.savefig(path, dpi=DPI, facecolor=BG)
    plt.close(fig)
