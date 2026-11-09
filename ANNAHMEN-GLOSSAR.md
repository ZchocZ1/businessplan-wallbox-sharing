# Annahmen und Glossar

## Glossar
| Begriff | Definition |
|---|---|
| Wallbox | Private Ladestation für Elektroautos |
| Wallbox-Sharing | Privatpersonen stellen ihre Wallbox zeitweise anderen E-Auto-Fahrern zur Verfügung |
| DACH | Deutschland, Österreich, Schweiz |

## Annahmen
| ID | Annahme | Wert | Begründung/Quelle | Status |
|---|---|---|---|---|
| A-01 | _offen_ | | | offen |
| A-02 | Gadget-Herstellkosten pro Anbieter | _offen_ | Kosten stehen noch nicht fest; Recherche nötig | offen |
| A-03 | Gadget-Pfand | _offen_ | Pfand mit Rückerstattung bei Rückgabe (bestätigt 2026-10-26); Höhe wird im Pilot mit zwei Varianten getestet; für den Finanzplan eine Planannahme mit Spanne nötig, orientiert an den Herstellkosten (A-02) | offen |
| A-04 | Gesamtbestand privater Wallboxen in Deutschland | 2.359 Tsd. (2023); Prognose 4.069 Tsd. (2030) | AlixPartners über Statista (P-05, `recherche/statista-auswertung.md` S-1), Methodik unbekannt; Untergrenze ca. 690.000 geförderte (P-01) | Quelle belegt, Definition offen |
| A-05 | Zeitbudget je Teammitglied für das Projekt | 5 bis 10 Stunden pro Woche | Angabe der Gruppe im Ressourcen-Grill-me vom 2026-10-26 (Schätzung, nicht belegt); gilt neben dem dualen Studium | Annahme der Gruppe |
| A-06 | Mindestzahl aktiver Anbieter je Pilotregion zum Pilotstart | Vorschlag 2026-11-09: 10 / 30 / 60 (`finanzen/marktgroesse-szenarien.md`) | Wert nach Kapazität und Umfrage festlegen (Beschluss 2026-10-26: Zielwert als Annahme) | offen |
| A-07 | Eigenmittel der Gründer (Betrag je Person) | _offen_ | Freiwillig und unterschiedlich (Beschluss 2026-10-26); Betrag vor Gründung abstimmen | offen |
| A-08 | Teilungsbereitschaft der Wallbox-Besitzer (Spanne) | Vorschlag 2026-11-09: 1 % / 3 % / 5 % (`finanzen/marktgroesse-szenarien.md`) | Nicht belegbar (`recherche/teilungs-und-zahlungsbereitschaft.md`); Spanne pessimistisch/realistisch/optimistisch festlegen | offen |
| A-09 | Zahlungsbereitschaft der Fahrer für geteiltes Laden | _offen_ | Orientierung: 6,84 € je 100 km für Laden insgesamt (Fraunhofer ISI, Befragte aus Mehrparteienhäusern, hypothetisch); keine Studie zu Wallbox-Sharing | offen |
| A-10 | Milieu der Fahrer | Alle E-Auto-Fahrer ohne direkten Zugriff auf eine Wallbox an ihrer Wohnung; Kern F1 Mieter | Definition von Ben (2026-11-09), nicht erhoben und nicht belegt; Prüfung durch Umfrage/Interviews. Beschluss: `kapitel/00d-geschaeftsmodell-zielmarkt-beschluesse.md` | Annahme der Gruppe |
| A-11 | Milieu der Anbieter | Alle Wallbox-Besitzer (privat, gewerblich); Akquise-Schwerpunkt auf Wallboxen mit PV-Anlage | Definition von Ben (2026-11-09), nicht erhoben und nicht belegt. Angebot bleibt für jede Wallbox offen | Annahme der Gruppe |
| A-12 | Freie Stunden je Wallbox und Tag (teilbare Zeit) | Vorschlag: 3 / 6 / 10 h | Szenarien pessimistisch/realistisch/optimistisch; Claude schlägt vor, Gruppe prüft (Beschluss 2026-11-09). Orientierung: pv magazine, Juni 2026 („über 90 % ungenutzt“, eine Quelle) | offen |
| A-13 | Anteil der Wallboxen mit PV-Kopplung | _offen_ | Keine belegte Zahl; für den PV-Schwerpunkt der Akquise nötig (Beschluss 2026-11-09). Recherche oder Spanne festlegen | offen |
| A-14 | kWh-Preisspanne PV-Strom und Normal-Strom, Provisionssatz (in den Preis eingerechnet) | _offen_ | Zwei Preisspannen (Beschluss 2026-11-09); Orientierung: Cocharge 0,59 €/kWh brutto (Herstellerseite, 2026-10-26); Provisionssatz nur als Annahme | offen |
| A-15 | kWh je Anbieter-Wallbox und Monat | pessimistisch 100 / realistisch 200 / optimistisch 340 | Annahme (2026-11-09); 340 = Cocharge-Rechner (Herstellerangabe, `recherche/branchenrendite.md` R-04), nicht gemessen. Verwendung: `finanzen/unit-economics.md` | Annahme der Gruppe, zu prüfen |
| A-16 | kWh je Ladevorgang | 20 | Frei gesetzt, nicht belegt (Unit Economics) | Annahme, zu prüfen |
| A-17 | Zahlart-Mix | 100 % Karte EWR (vorsichtig) | Frei gesetzt; Stripe-Listenpreise als Beispiel, kein Anbieterbeschluss | Annahme, zu prüfen |
| A-18 | Anteil der Fahrer ohne Heimladen, die Sharing nutzen | Vorschlag: 1 % / 3 % / 5 % | Frei gesetzt, nicht belegt; größter Hebel der Marktgröße (`finanzen/marktgroesse-szenarien.md`) | Annahme, zu prüfen |
| A-19 | kWh je Monat und Fahrer über Sharing | Vorschlag: 100 / 150 / 200 | Frei gesetzt, nicht belegt | Annahme, zu prüfen |
| A-20 | Ladeleistung je Wallbox | 11 kW | Typischer Wert, frei gesetzt, nicht belegt | Annahme, zu prüfen |
