# Auswertung der Statista-PDFs (Ordner `recherche/statista/`)

**Diese Datei ist der Ersatz für die PDFs im Repository.** Die PDFs selbst (Statista-Lizenz) liegen nur lokal in `recherche/statista/` und sind per `.gitignore` von Git ausgeschlossen. Alle verwertbaren Daten stehen hier; Ergänzungen und Korrekturen der Gegenprüfung vom 2026-11-02 stehen im Abschnitt „Gegenprüfung 2026-11-02“ am Ende.

Ausgewertet am 2026-10-19. Alle sechs PDFs wurden vollständig gelesen. Die Werte stehen exakt so, wie sie im jeweiligen Diagramm gedruckt sind. **Berechnete Werte** sind als solche gekennzeichnet (Rechenweg angegeben). Statista ist ein Aggregator; die Primärerheber stehen in der Spalte „Erheber laut PDF“. Methodik, Definitionen und Fußnotentexte sind in den PDFs nicht enthalten.

## S-1 Private und öffentliche Ladepunkte 2023 und Prognose 2030
- Datei: `Anzahl-der-privaten-und-öffentlichen-Ladepunkte-für-Elektroautos-in-Deutschland-im-Jahr-2023-und-Prognose-für-2030-(in-1.000)-2026-Statista.pdf`
- Titel: „Anzahl der privaten und öffentlichen Ladepunkte für Elektroautos in Deutschland im Jahr 2023 und Prognose für 2030 (in 1.000)“
- Erheber laut PDF: **AlixPartners**, © Statista 2026. Zusatzinfo: Deutschland; 2023 und 2030. Einheit: Tsd. Ladepunkte.

| | 2023 | 2030 (Prognose) |
|---|---|---|
| Öffentlich | 62 Tsd. | 279 Tsd. |
| Privat | **2.359 Tsd.** | **4.069 Tsd.** |

Berechnet (aus obigen Werten):
- Privat 2023 → 2030: +1.710 Tsd. (+72,5 %), durchschnittlich ca. +8,1 % pro Jahr (7 Jahre).
- Öffentlich 2023 → 2030: +217 Tsd., Faktor 4,5.
- Privatanteil an allen Ladepunkten: 2023 ca. 97,4 %, 2030 ca. 93,6 %.

Einschränkungen:
- Das PDF nennt nicht, ob der 2023-Wert eine Zählung oder Schätzung ist, und nicht, was „privat“ umfasst (Einfamilienhaus, Mehrparteienhaus, Firmen). Nicht geklärt.
- Der öffentliche Wert 2023 (62 Tsd.) weicht deutlich von den Bundesnetzagentur-Werten ab (siehe S-6, 88.313 im Jan. 2023 und S-4, 89.823 im Jahr 2023). Die Definition von AlixPartners ist offenbar eine andere. Das schwächt die Vergleichbarkeit der Zahlen von S-1 mit amtlichen Daten.
- Vereinbar mit der Förderzahl P-01 (ca. 690.000 geförderte private Ladepunkte, 2021–2022) in dem Sinn, dass der Gesamtwert höher liegt; ein Abgleich der Definition ist nicht möglich.

## S-2 Öffentliche und halböffentliche Ladepunkte 2016–2019 und Prognose bis 2025
- Datei: `Anzahl-öffentlicher-und-halb-öffentlicher-Ladepunkte-für-Elektrofahrzeuge-in-Deutschland-von-2016-bis-2019-und-Prognose-bis-2025-2026-Statista.pdf`
- Erheber laut PDF: **Horváth & Partners**, © Statista 2026. Zusatzinfo: „Deutschland; 2016 bis 2019“.

| Jahr | Anzahl |
|---|---|
| 2016 | 6.895 |
| 2017 | 10.878 |
| 2018 | 16.100 |
| 2019 | 24.000 |
| 2020¹ | 35.649 |
| 2021¹ | 52.951 |
| 2022¹ | 78.651 |
| 2025¹ | 257.749 |

- Die Werte 2020–2022 und 2025 tragen die Fußnote ¹; der Fußnotentext steht nicht im PDF. Laut Titel sind Werte nach 2019 Prognosen („Prognose bis 2025“).
- Vergleich mit Ist-Werten der Bundesnetzagentur (S-4): 2020 31.006, 2021 44.317, 2022 61.972 liegen unter den damaligen Prognosewerten. Die Prognose 2025 (257.749) liegt über dem Bundesnetzagentur-Wert 2025 (164.784, S-4). Prognose wurde nicht erreicht.
- Zählt öffentliche **und halb-öffentliche** Ladepunkte, ist also mit den Bundesnetzagentur-Zahlen nicht deckungsgleich.

## S-3 Ladesäulen nach Anzahl Ladepunkte (Stand 25. März 2026)
- Datei: `Anzahl-der-Ladesäulen-nach-Ladepunkten-in-Deutschland-im-Jahr-2026-2026-Statista.pdf`
- Erheber laut PDF: **Bundesnetzagentur**, © Statista 2026. Zusatzinfo: Deutschland; Stand 25. März 2026.

| Ladesäule mit … Ladepunkt(en) | Anzahl Ladesäulen |
|---|---|
| 1 | 30.074 |
| 2 | 73.161 |
| 3 | 2.378 |
| 4 | 2.826 |
| 5 | 25 |
| 6 | 113 |

Berechnet:
- Ladesäulen insgesamt: 30.074 + 73.161 + 2.378 + 2.826 + 25 + 113 = **108.577**.
- Daraus abgeleitete Ladepunkte: 30.074×1 + 73.161×2 + 2.378×3 + 2.826×4 + 25×5 + 113×6 = **195.637** (Stichtag 25.03.2026; plausibel zu den 195.051 in S-4, aber anderer Stichtag).

## S-4 Öffentlich zugängliche Ladepunkte nach Leistungsklassen 2017–2026
- Datei: `Anzahl-der-öffentlich-zugänglichen-Ladepunkte-für-Elektrofahrzeuge-in-Deutschland-nach-Leistungsklassen-in-den-Jahren-2017-bis-2026-2026-Statista.pdf`
- Erheber laut PDF: **Bundesnetzagentur**, © Statista 2026. Zusatzinfo: Deutschland; 2017 bis 2026.

| Jahr | Ladepunkte gesamt |
|---|---|
| 2017 | 6.757 |
| 2018 | 11.191 |
| 2019 | 19.862 |
| 2020 | 31.006 |
| 2021 | 44.317 |
| 2022 | 61.972 |
| 2023 | 89.823 |
| 2024 | 130.670 |
| 2025 | 164.784 |
| 2026 | 195.051 |

- Das Diagramm ist nach acht Leistungsklassen gestapelt (0–3,7 kW; >3,7–15; >15–22; >22–49; >49–59; >59–149; >149–299; >299 kW). **Die Werte je Klasse sind im PDF nicht beschriftet** und werden hier nicht angegeben.
- Der Stichtag je Jahr steht nicht im PDF. Die Werte weichen von den Monatswerten in S-6 ab (z. B. 2023: 89.823 hier, Jan. 2023: 88.313 in S-6); der Stichtag ist vermutlich unterschiedlich, nicht geklärt.

## S-5 Öffentliche Ladepunkte nach Bundesland
- Datei: `Anzahl-der-öffentlichen-Ladepunkte-in-Deutschland-nach-Bundesland-im-Jahr-2026-2026-Statista.pdf`
- Erheber laut PDF: **Bundesnetzagentur**, © Statista 2025. Zusatzinfo: „Deutschland; 1. Jan ’25“.
- **Widerspruch im PDF:** Der Titel nennt „im Jahr 2026“, die Fußzeile nennt „1. Jan ’25“. Die Summe der Werte (160.809) entspricht dem Wert in S-6 für Januar 2025. **Stichtag daher 1. Januar 2025 (berechnet, nicht ausdrücklich bestätigt).** Die Achse heißt „Anzahl Ladesäulen“, der Titel „Ladepunkte“; die Summenübereinstimmung mit den Ladepunkten aus S-6 spricht für Ladepunkte.

| Bundesland | Anzahl |
|---|---|
| Bayern | 31.309 |
| Nordrhein-Westfalen | 30.853 |
| Baden-Württemberg | 27.611 |
| Niedersachsen | 15.905 |
| Hessen | 12.898 |
| Schleswig-Holstein | 6.516 |
| Rheinland-Pfalz | 6.298 |
| Sachsen | 5.797 |
| Berlin | 5.647 |
| Brandenburg | 3.963 |
| Hamburg | 3.357 |
| Thüringen | 3.311 |
| Sachsen-Anhalt | 2.750 |
| Mecklenburg-Vorpommern | 2.141 |
| Saarland | 1.228 |
| Bremen | 1.225 |

- Berechnet: Summe aller Bundesländer = **160.809**.
- Aufteilung in Normal- und Schnellladen ist im Diagramm farblich gestapelt, aber nicht beschriftet; nicht angegeben.

## S-6 Öffentliche Ladepunkte Januar 2017 bis August 2026
- Datei: `Anzahl-der-öffentlichen-Ladepunkte-in-Deutschland-von-Januar-2017-bis-August-2026-2026-Statista.pdf`
- Erheber laut PDF: **Bundesnetzagentur**, © Statista 2026. Zusatzinfo: Deutschland; Januar 2017 bis August 2026¹ (Fußnotentext nicht im PDF; Achse nennt „Jan '23¹“).
- Gestapelt nach Normalladepunkt (bis 22 kW) und Schnellladepunkt (>22 kW); die Teilwerte sind nicht beschriftet.
- Gedruckte Gesamtwerte, in Reihenfolge der Balken: 6.496; 7.038; 7.766; 9.108; 10.780; 11.800; 13.464; 15.695; 19.234; 21.154; 23.857; 26.746; 30.165; 32.735; 35.203; 38.058; 42.806; 45.918; 49.720; 53.447; 59.828; 65.387; 69.950; 77.602; 88.313; 95.974; 105.683; 113.567; 123.449; 135.241; 142.793; 150.867; 151.718; 154.037; 160.809; 166.110; 166.867; 169.082; 172.150; 175.141; 177.374; 179.938; 196.846; 198.384; 202.118; 203.951; 206.207; 209.605; 212.064.
- Die Zuordnung der Werte zu Monaten ist im PDF-Text nicht angegeben. Sicher zuordenbar (Wert im Diagramm direkt unter einer Monatsbeschriftung bzw. durch den Titel): **Januar 2017: 6.496** (erster Wert), **August 2026: 212.064** (letzter Wert, Titelende). Weitere Zuordnungen nur aus den im Diagramm beschrifteten Balken lesbar und hier nicht übernommen, um keine Fehlzuordnung zu riskieren.
- Der Wert für Januar 2025 (160.809) ist über die Summe in S-5 abgesichert (Berechnung oben).

## Was daraus für das Projekt folgt
1. **Erstmals eine Zahl für privaten Ladepunkte-Bestand:** 2.359 Tsd. (2023) und Prognose 4.069 Tsd. (2030), Erheber AlixPartners, über Statista. Sie ist eine **Sekundärquelle ohne bekannte Methodik** und weicht bei der öffentlichen Zahl von der Bundesnetzagentur ab. Sie ist verwendbar mit dem Hinweis „laut AlixPartners (Statista 2026)“, nicht als amtliche Zahl.
2. **Öffentliche Infrastruktur (Bundesnetzagentur, über Statista)** ist durch S-3 bis S-6 belegt: 212.064 öffentliche Ladepunkte im August 2026.
3. **Verhältnis privat zu öffentlich 2023** ca. 38 zu 1 (2.359 / 62, berechnet) nach AlixPartners-Zahlen; wegen der abweichenden Definition nur eingeschränkt belastbar.
4. Prognosen (S-1: 2030; S-2: 2025) sind Prognosen, keine Ist-Werte. S-2 zeigt, dass die Prognose für 2025 deutlich über dem tatsächlichen Wert lag; Prognosen daher vorsichtig behandeln.

## Gegenprüfung 2026-11-02 (alle sechs PDFs erneut als Bild gelesen)
Alle Zahlen in S-1 bis S-5 stimmen mit den gedruckten Diagrammwerten überein. Ergänzungen:

### Lesehilfe zu den Diagrammen (Metadaten aus den PDFs)
| Nr. | Titel laut PDF | Quelle/Urheber laut PDF | Zusatzinfo laut PDF | Diagrammart |
|---|---|---|---|---|
| S-1 | Anzahl der privaten und öffentlichen Ladepunkte … 2023 und Prognose für 2030 (in 1.000) | AlixPartners, © Statista 2026 | Deutschland; 2023 und 2030 | gruppierte Balken (2023 / 2030) |
| S-2 | Anzahl öffentlicher und halb-öffentlicher Ladepunkte … von 2016 bis 2019 und Prognose bis 2025 | Horváth & Partners, © Statista 2026 | Deutschland; 2016 bis 2019 | Balken |
| S-3 | Anzahl der Ladesäulen nach Ladepunkten … im Jahr 2026 | Bundesnetzagentur, © Statista 2026 | Deutschland; Stand: 25. März 2026 | Balken |
| S-4 | Anzahl der öffentlich zugänglichen Ladepunkte … nach Leistungsklassen … 2017 bis 2026 | Bundesnetzagentur, © Statista 2026 | Deutschland; 2017 bis 2026 | gestapelte Balken, 8 Leistungsklassen |
| S-5 | Anzahl der öffentlichen Ladepunkte … nach Bundesland im Jahr 2026 | Bundesnetzagentur, © Statista 2025 | Deutschland; 1. Jan ’25 | gestapelte Balken (Normal / Schnell), Bundesländer in englischer Schreibweise |
| S-6 | Anzahl der öffentlichen Ladepunkte … von Januar 2017 bis August 2026 | Bundesnetzagentur, © Statista 2026 | Deutschland; Januar 2017 bis August 2026¹ | gestapelte Balken (Normal bis 22 kW / Schnell >22 kW) |

### S-2: Lücke in den Jahren
Das Diagramm zeigt nur die Jahre 2016, 2017, 2018, 2019, 2020¹, 2021¹, 2022¹ und 2025¹. Die Jahre 2023 und 2024 fehlen im PDF (nicht ergänzen). Der Fußnotentext zu ¹ steht nicht im PDF.

### S-3: kleine Werte
Die Balken für 5 Ladepunkte (25) und 6 Ladepunkte (113) sind im Diagramm kaum sichtbar; die Zahlen sind gedruckt.

### S-4: Leistungsklassen
Legende (acht Klassen, Farben): 0–3,7 kW (blau), >3,7–15 kW (dunkelblau), >15–22 kW (grau), >22–49 kW (dunkelrot), >49–59 kW (grün), >59–149 kW (gelb), >149–299 kW (violett), >299 kW (hellviolett). Gedruckt sind nur die Jahressummen (siehe S-4). Qualitativ lesbar, **nicht beschriftet, keine Zahlen**: Die Klasse >15–22 kW ist in allen Jahren die größte; ab 2023 wächst der Anteil der Klassen ab 149 kW sichtbar. Für Zahlen je Klasse müsste die Originalquelle der Bundesnetzagentur herangezogen werden.

### S-5: Stichtag und Beschriftung
Titel „im Jahr 2026“, Zusatzinfo „1. Jan ’25“, Copyright „© Statista 2025“: Der Stichtag ist laut PDF **1. Januar 2025**. Die Achse heißt „Anzahl Ladesäulen“, der Titel „Ladepunkte“ (Widerspruch im PDF; siehe Summenabgleich in S-5). Legende englisch: „Normal charging speed“ und „Quick charge“. Je Bundesland ist der Anteil Schnellladen nur als Balkenanteil sichtbar, nicht beschriftet.

### S-6: was sich zuordnen lässt und was nicht
- Das Diagramm hat **49 Balken** für 116 Monate (Januar 2017 bis August 2026). Die Balken liegen also nicht in gleichmäßigen Monatsabständen; die Zeitachse ist nicht durchgehend monatlich. 25 Achsenbeschriftungen: Jan ’17, Jul ’17, Jan ’18, Jul ’18, Jan ’19, Jul ’19, Jan ’20, Jul ’20, Jan ’21, Jul ’21, Jan ’22, Jul ’22, Jan ’23¹, Jul ’23, Jan ’24, Jul ’24, Okt ’24, Jan ’25, Mai ’25, Jul ’25, Sep ’25, Jan ’26, Apr ’26, Jun ’26, Aug ’26.
- Im Diagramm sind nur **22 Werte sichtbar beschriftet** (jeder zweite Balken, in Leserichtung): 6.496; 7.766; 10.780; 13.464; 19.234; 23.857; 30.165; 35.203; 42.806; 49.720; 59.828; 69.950; 88.313; 105.683; 123.449; 142.793; 154.037; 166.867; 175.141; 196.846; 203.951; 212.064. Die übrigen Werte der Liste in S-6 stehen nur im Textlayer des PDFs.
- **Zuordnung zu Monaten, soweit aus dem Diagramm lesbar** (Beschriftung steht über dem Balken, der zum Achsenlabel gehört; ein Versatz um einen Balken ist nicht ausgeschlossen): Jan ’17: 6.496 · Jan ’23: 88.313 · Aug ’26: 212.064. Die anderen sind **nicht belastbar** zuordenbar.
- **Widerspruch, offen:** Das Wertlabel 154.037 steht im Diagramm am Achsenlabel „Jan ’25“; aus der Summe der Bundesländer (S-5, Stichtag 1. Jan ’25) ergibt sich dagegen 160.809, was in der Wertliste der benachbarte Balken ist. Entweder sind die Balken gegenüber den Beschriftungen um einen Balken versetzt, oder die Stichtage in S-5 und S-6 unterscheiden sich. Für den Januar-2025-Bestand gilt deshalb weiterhin „160.809 (S-5-Summe, berechnet)“, mit diesem Vorbehalt. Zur Klärung die Bundesnetzagentur-Primärquelle prüfen.
- Die Fußnote ¹ (an „Jan ’23¹“ und in der Zusatzinfo) hat im PDF keinen Text. Der Sprung im Verlauf zwischen den Balken 179.938 und 196.846 (+16.908) ist auffällig; Ursache nicht im PDF erklärt (denkbar: Neuerfassung oder Zählweise). Nicht geklärt, nicht interpretieren.
