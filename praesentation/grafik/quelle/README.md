# Quelle der Grafiken und der Präsentation

Die Folien bestehen aus Grafiken (`../slide01.png` bis `slide14.png`, gestaltet nach `../gestaltungsphilosophie.md`) und nativen, editierbaren Texten (Titel, Untertitel, Quellen, Sprechernotizen). Text und Zahlen in den **Grafiken** ändert man im Python-Code, Titel und Notizen in `content.py`.

## Neu erzeugen (Entwurf, nicht Teil der Abgabe)
1. Python-Umgebung mit `matplotlib`, `numpy`, `pillow` und Node mit `pptxgenjs` bereitstellen.
2. In `lib.py` den Pfad `FD` auf einen Ordner mit den Schriften (Instrument Sans, JetBrains Mono, Outfit) setzen; die Schriften liegen im canvas-design-Skill unter `canvas-fonts/`.
3. In diesem Ordner: `python render_all.py` (Grafiken), `python content.py`, `python layout.py`, `node build.js ../../WallShare-Investorenpraesentation.pptx` (Präsentation; `build.js` braucht die Datei `scripts/apply_theme.js` des pptx-Skills, Pfad `SKILL` oben anpassen).
4. `python preview.py` zeigt Grafik und Text zusammen und meldet Textüberläufe.

## Zahlen und Quellen
Alle Zahlen stammen aus `kapitel/00d`, `03b`, `03c`, `finanzen/marktgroesse-szenarien.md`, `finanzen/unit-economics.md` und `recherche/`. Bei Änderungen dort die Grafik in `slides_*.py` nachziehen.
