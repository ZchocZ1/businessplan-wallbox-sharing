# Recherche: Branchenrendite und Marktattraktivität (II.3, Option 2)

Stand der Recherche: 2026-11-09. Drei Websuchen und fünf direkte Abrufe. Beschluss: `kapitel/00d-geschaeftsmodell-zielmarkt-beschluesse.md`. Folgeschritt (Unit Economics): `finanzen/unit-economics.md`.

## Ergebnis
**Es wurde keine belegte Branchenrendite (Marge, EBITDA, Kapitalrendite) für Ladeinfrastruktur-Betreiber oder Wallbox-Sharing-Plattformen in Deutschland gefunden.** Belegt sind nur Auslastung, Konsolidierungserwartung und eine Take Rate bei einer Vergleichsplattform. Renditeaussagen dürfen im Plan nur als „nicht belegt“ stehen; die Rendite kommt aus unserem eigenen Modell (`finanzen/unit-economics.md`).

## A Belegt (Seite direkt abgerufen am 2026-11-09)
| ID | Aussage | Quelle | Einschränkung |
|---|---|---|---|
| R-01 | „Öffentliche Ladepunkte waren im Jahr 2025 im Durchschnitt nur zu rund zwölf Prozent zeitgleich belegt“ (BDEW-Elektromobilitätsmonitor, zitiert). Bei Schnellladern „teilweise“ im einstelligen Prozentbereich (Automobilwoche mit Elvah, ohne Zahl). | https://www.auto-motor-und-sport.de/verkehr/ladeinfrastruktur-in-deutschland-die-auslastung-liegt-bei-nur-12-prozent/ | Sekundärquelle (Fachmedium); BDEW-Primärquelle nicht gelesen. |
| R-02 | „Die Einnahmen bei geringer Auslastung entsprechend begrenzt bleiben“; „Branchenbeobachter rechnen mit einer Konsolidierung des Marktes“. Keine Renditezahlen. | derselbe Artikel | Qualitativ, Quelle „frühere Analysen“ nicht genannt. |
| R-03 | Bei Wallbox-Sharing-Plattformen bestehen „erhebliche Kosten für Kundengewinnung, Zahlungsabwicklung, Support und Versicherungen“; Gastgeber könnten „nur mit begrenzten Zusatzerlösen rechnen“. Abschnitt „Die Wirtschaftlichkeit bleibt eine offene Frage“. Keine Beträge. | pv magazine, 19.06.2026 (Paul Fabianek): https://www.pv-magazine.de/2026/06/19/wallbox-sharing-warum-sich-die-guenstigste-ladesaeule-deutschlands-noch-nicht-durchgesetzt-hat/ | Qualitativ, eine Quelle. Der Artikel nennt zudem „mehr als eine Million private Wallboxen“ und „unter 10 % Auslastung“ ohne Primärquelle; bleibt unbelegt (vgl. `private-wallboxen-deutschland.md`, U-01/U-03). |
| R-04 | Cocharge: Verkaufspreis „0,59 €/kWh (brutto)“, einmalige Anschlussgebühr 75 €, keine Monatsgebühr, keine Mindestlaufzeit; der Rechner der Seite zeigt im Schnitt **340 kWh pro Monat** je Ladepunkt (Beispiele: Einfamilienhaus mit PV 250–350 kWh, Wohnimmobilie 850–1.200 kWh, Autohaus 1.000–2.000 kWh). **Ein Prozentsatz der Auszahlung wird auf der Seite nicht genannt.** | https://cocharge.de (Abruf 2026-11-09) | Herstellerrechner, keine gemessene Nutzung. Er ist eine Beispielrechnung des Anbieters. |
| R-05 | Take Rate Airbnb (Umsatz / Gross Booking Value): 2023 13,5 % (9,92 Mrd. $ / 73,25 Mrd. $), 2025 13,4 % (12,2 Mrd. $ / 91,3 Mrd. $). | https://fourweekmba.com/airbnb-take-rate/ (Analyse FourWeekMBA, 27.05.2026) | **Sekundärquelle**, ohne Primärbeleg (Geschäftsbericht); die Seite widerspricht sich bei einzelnen Jahren (z. B. 2023: Diagramm 14,2 %, Text 13,5 %). Nur als grobe Größenordnung für eine Sharing-Plattform nutzbar, nicht als Vorgabe für unsere Provision. |

## B Nicht belegt, nicht verwenden
| ID | Aussage | Herkunft | Problem |
|---|---|---|---|
| U-12 | Cocharge behält „rund 15 %“ Provision; Wallbox-Besitzer erhalten „85 %“, Ø 200 € je Ladepunkt und Monat | Suchzusammenfassung nach energiefluss24 und evcc-Blog | Die Cocharge-Seite nennt **keinen** Prozentsatz (R-04, am 2026-11-09 erneut geprüft). Die Suchzusammenfassung, die „85 % auf der Website“ behauptete, ließ sich nicht bestätigen. Der Wert „ca. 200 €“ ist die Rechnung 340 kWh × 0,59 € und keine Angabe der Seite. |
| U-13 | Marktplatz-Take-Rate im Durchschnitt „etwa 5 %“ | Blog greenmoov.app | Ohne Beleg, widerspricht R-05. |
| U-14 | Vrbo 8 %, Booking.com ca. 15 % (10–25 %) | Hostaway-Blog | Drittanbieter-Blog, keine Primärquelle. |
| U-15 | Margenaussagen aus „Aurora Energy Research 2018“ zu Autobahn- und Parkplatz-Ladepunkten | Suchzusammenfassung | Studie nicht abgerufen, 2018 veraltet. |
| – | Deloitte, „Ladeinfrastruktur als Geschäftsmodell“ | PDF abgerufen | Der Abruf lieferte nur Metadaten, keinen Studientext. Inhalt **nicht ausgewertet**. |

## C Was daraus folgt (Einschätzung, kein Beleg)
- **Attraktivität (II.3):** Wachstum ist belegt (`kapitel/03a-markt-entscheidungen.md`, Datengrundlage: BEV-Bestand, Ladepunkte). Gegen eine hohe Branchenrendite sprechen die belegte niedrige Auslastung (R-01) und die erwartete Konsolidierung (R-02). Für Plattformen nennt die einzige Quelle die Wirtschaftlichkeit „offen“ (R-03).
- **Take-Rate-Vergleich:** Nur R-05 liefert eine Größenordnung (rund 13 %, Airbnb, Sekundärquelle). Unsere Provision (A-14) bleibt eine Annahme mit Spanne.
- **Nächste Schritte** (nicht von Claude lösbar oder offen): Deloitte-Studie als Text beschaffen; BDEW-Primärquelle lesen; Geschäftsberichte von Airbnb (Primärquelle für R-05) und von Ladeplattformen (Handelsregister, Bundesanzeiger) prüfen; Cocharge nach der Provision fragen.
