# Marktgröße (TAM/SAM/SOM) mit Szenarien

Stand: 2026-11-09. Umsetzung des Beschlusses II.2 (`kapitel/00d-geschaeftsmodell-zielmarkt-beschluesse.md`): Angebot und Nachfrage werden beide gerechnet, der kleinere Wert begrenzt den Markt; SOM bottom-up mit Top-down-Check. **Belegt sind nur die Basiszahlen (Abschnitt 1). Alle Szenariowerte sind Annahmen mit ID, von Claude vorgeschlagen, die Gruppe prüft.** Die Ergebnisse sind Größenordnungen, keine Prognose.

## 1 Belegte Basiszahlen
| Größe | Wert | Quelle | Einschränkung |
|---|---|---|---|
| BEV-Bestand Deutschland, 1.1.2026 | 2.034.260 | `kapitel/00-ueberblick-produkt-kunde-markt.md` 3.1 | Sekundärquelle, vor Abgabe an KBA prüfen |
| Anteil, der zu Hause lädt | 82 % | BDEW, Seitenstand 29.07.2026 (`recherche/private-wallboxen-deutschland.md` P-04) | Heimladen ist nicht gleich „Wallbox an der Wohnung“; Näherung |
| Fahrer ohne Heimladen (Näherung 18 %) | **366.167** | eigene Rechnung: 2.034.260 × 18 % | grobe Näherung, nicht belegt als „ohne Wallbox“ |
| Private Ladepunkte | 690.000 (Untergrenze, geförderte 2021/22); 2.359 Tsd. (2023); 4.069 Tsd. (Prognose 2030) | NOW GmbH (P-01); AlixPartners über Statista (P-05) | Methodik von P-05 unbekannt; Zeitbasis der drei Werte verschieden |
| Gewerbliche Ladepunkte | **keine Zahl** | – | bewusst nicht eingerechnet |

## 2 Annahmen für die Szenarien
| ID | Größe | Pessimistisch | Realistisch | Optimistisch |
|---|---|---|---|---|
| A-08 | Teilungsbereitschaft der Wallbox-Besitzer | 1 % | 3 % | 5 % |
| A-12 | freie Stunden je Tag für Fremde | 3 | 6 | 10 |
| A-18 | Anteil der Fahrer ohne Heimladen, die Sharing nutzen | 1 % | 3 % | 5 % |
| A-19 | kWh je Monat und Fahrer über Sharing | 100 | 150 | 200 |
| A-20 | Ladeleistung je Wallbox (kW) | 11 | 11 | 11 |
| A-14 | kWh-Preis brutto | 0,45 € | 0,55 € | 0,59 € |
| A-14 | Provision | 10 % | 15 % | 20 % |
| – | Ladepunkte (Basis Angebot) | 690.000 | 2.359.000 | 4.069.000 |

## 3 Ergebnis Deutschland, pro Jahr (Basisjahr 2026, kein Wachstum extrapoliert)
Definitionen: **TAM** = alle 366.167 Fahrer ohne Heimladen laden ausschließlich per Sharing (Obergrenze der Nachfrage). **SAM** = Nachfrage der Nutzungsbereiten (A-18). **Angebot** = teilungsbereite Wallboxen × 11 kW × freie Stunden × 360 Tage. **Markt** = kleinerer Wert aus SAM und Angebot.

| Größe | Pessimistisch | Realistisch | Optimistisch |
|---|---|---|---|
| TAM, Energie | 439 Mio. kWh | 659 Mio. kWh | 879 Mio. kWh |
| TAM, Umsatz (Fahrer zahlt, brutto) | 198 Mio. € | 363 Mio. € | 519 Mio. € |
| Nutzungsbereite Fahrer (SAM) | 3.662 | 10.985 | 18.308 |
| SAM, Energie | 4,4 Mio. kWh | 19,8 Mio. kWh | 43,9 Mio. kWh |
| Teilungsbereite Wallboxen | 6.900 | 70.770 | 203.450 |
| Angebot, Kapazität | 82 Mio. kWh | 1.682 Mio. kWh | 8.057 Mio. kWh |
| **Begrenzend** | Nachfrage | Nachfrage | Nachfrage |
| **Markt (SAM), Umsatz** | **2,0 Mio. €** | **10,9 Mio. €** | **25,9 Mio. €** |
| Plattformerlös (Provision) | 0,20 Mio. € | 1,63 Mio. € | 5,18 Mio. € |

**Aussage:** In allen Szenarien begrenzt die **Nachfrage**, nicht das Angebot. Die Kapazität der teilungsbereiten Wallboxen ist 19- bis 183-mal so groß wie die Nachfrage. Das Henne-Ei-Problem liegt bundesweit bei den Fahrern; lokal (Pilotregion) kann es anders aussehen, dazu fehlen Regionaldaten. Die Angebotskapazität (11 kW × Stunden) ist eine theoretische Obergrenze und nicht die Auslastung je Wallbox (A-15: 100 bis 340 kWh im Monat).

## 4 SOM, bottom-up für den Pilot (zwei Regionen)
Eingaben: Anbieter je Region zum Pilotstart (A-06, Vorschlag 10 / 30 / 60), zwei Regionen (Mannheim–Heidelberg, Odenwald), kWh je Wallbox A-15 (100 / 200 / 340), Preise und Provision wie in Abschnitt 2, Deckungsbeitrag I aus `finanzen/unit-economics.md`.

| Größe, pro Jahr | Pessimistisch | Realistisch | Optimistisch |
|---|---|---|---|
| Aktive Anbieter (2 Regionen) | 20 | 60 | 120 |
| Energie | 24.000 kWh | 144.000 kWh | 489.600 kWh |
| Umsatz (Fahrer zahlt) | 10.800 € | 79.200 € | 288.864 € |
| Provision | 1.080 € | 11.880 € | 57.773 € |
| Deckungsbeitrag I (nach Zahlungskosten) | 89 € | 7.214 € | 43.718 € |

**Top-down-Check:** SOM-Energie im Verhältnis zur SAM-Energie Deutschland: 24.000 / 4,4 Mio. = 0,5 %; 144.000 / 19,8 Mio. = 0,7 %; 489.600 / 43,9 Mio. = 1,1 %. Das ist plausibel für zwei Regionen im ersten Jahr, **wenn** die Regionen proportional zur Bevölkerung Fahrer und Wallboxen haben; das ist ungeprüft. Der Check sagt nichts darüber, ob die Anbieterzahl (A-06) erreichbar ist.

## 5 Grenzen
- Basisjahr 2026: Das belegte BEV-Wachstum (+382.617 im Jahr 2025) und die Prognose bis 2030 (private Ladepunkte) sind nicht eingerechnet; TAM und SAM sind für 2027–2031 vermutlich höher. Eine Wachstumsannahme steht aus.
- Gewerbliche Ladepunkte und Fahrer-Segment F3 (Reisende, Pendler) sind nicht enthalten.
- **Quellenprüfung 2026-11-09 (`recherche/zielgruppen-pruefung.md`):** BEV-Bestand ist beim KBA primär bestätigt. Die 82 % (BDEW) haben auf der BDEW-Seite keine Quelle; Fraunhofer ISI nennt primär „rund 80 %“, also rund 20 % ohne Heimladen (406.852 Fahrer, +11 % auf alle Nachfragewerte). Die Rechnung oben bleibt mit 18 % stehen, bis die Gruppe entscheidet. Dass diese Fahrer Mieter in der Stadt sind, ist nicht belegt.
- 18 % „ohne Heimladen“ ist eine Näherung: Wer nicht zu Hause lädt, hat nicht zwingend keine Wallbox, und wer zu Hause lädt, kann zusätzlich Sharing nutzen.
- Der Preis ist brutto angesetzt; die MwSt-Behandlung ist ungeklärt.
- Der Ergebnisbereich ist sehr breit (Faktor 13 zwischen pessimistisch und optimistisch); er hängt fast nur an A-18 und A-19. Umfrage und Interviews (Niclas) sollten diese beiden zuerst prüfen.
