# Prüfung der Zielgruppe und der Belege in 03b und der Marktrechnung

Stand: 2026-11-09. Auftrag von Ben: prüfen, ob die Zielgruppe wirklich stimmt, und die Aussagen in `kapitel/03b-porter-five-forces.md` und `finanzen/marktgroesse-szenarien.md` so weit wie möglich mit **Primärquellen** belegen. Jede Quelle wurde am 2026-11-09 direkt abgerufen, sofern nicht anders vermerkt. „Primär“ heißt: Herausgeber der Zahl (Behörde, Forschungsinstitut, Anbieter selbst).

## 1 Urteil zur Zielgruppe
**Die Zielgruppe „Fahrer ohne Wallbox an der Wohnung“ ist als Größenordnung belegt, aber nicht als Zielgruppe „Mieter in der Stadt“ (F1).** Genauer:

| Annahme in 03b / Marktrechnung | Befund | Urteil |
|---|---|---|
| Rund 18 % der E-Auto-Fahrer laden nicht zu Hause (aus BDEW 82 %) | Die BDEW-Seite nennt für die 82 % **keine Quelle, kein Erhebungsjahr, keine Stichprobe**. Primär belegt ist stattdessen Fraunhofer ISI (Pressemitteilung 20.11.2025): „Approximately 80 percent of the electric cars registered in Germany are charged at home“. Das sind **rund 20 %**, nicht 18 %. | Größenordnung **bestätigt**, Wert 18 % **ersetzen** durch rund 20 % mit Primärquelle |
| Diese 18 % sind „Mieter ohne Ladeplatz“ (F1) | Es gibt **keine Aufschlüsselung** der Nicht-Heimlader nach Mieter oder Eigentümer. Die ISI-Studie nennt Heimladen „vor allem in Einfamilienhäusern“. In der Fraunhofer-Befragung haben „nahezu alle Elektroautobesitzenden“ einen eigenen Stellplatz (F-06). | **Nicht belegt** |
| Es gibt viele Mieter | Destatis, Mikrozensus-Zusatzprogramm Wohnen 2022: 58,2 % der 39,3 Mio. Haushalte wohnen zur Miete (22,9 Mio.), 41,8 % im Eigentum (16,4 Mio.). | **Belegt** (Haushalte, nicht E-Auto-Fahrer) |
| Mieter sind die Kernzielgruppe der E-Autos | Heutige E-Auto-Halter laden überwiegend zu Hause, „vor allem in Einfamilienhäusern“ (Fraunhofer ISI). Mieter sind also eher **künftige** Käufer. Ein Teil der Nachfrage ist **latent**: Mieter, die kein E-Auto kaufen, weil sie nicht laden können. Dazu gibt es keine Primärzahl (DAT 72 % und Verivox 4 % sind ungeprüft, `teilungs-und-zahlungsbereitschaft.md` U-08/U-09). | **Plausibel, nicht belegt**; die Marktrechnung zählt nur heutige Fahrer und unterschätzt wahrscheinlich das Potenzial |
| Ladeinfrastruktur in Mehrfamilienhäusern ist knapp | ADAC (08.02.2024), Umfrage 2022 unter 250 Wohnungsunternehmen in elf Städten: 7 % der Mehrfamilienhäuser hatten Wallboxen oder Ladesäulen (2019: 2 %). Umfrage 2023 unter 716 Mietern und Eigentümern: 57 % berichten Probleme in der Hausgemeinschaft. | **Belegt**, aber nicht repräsentativ (Teilnehmerauswahl, elf Städte) |
| Stadt ist der Kern (F1) | Gegenläufig: Wallboxen stehen meist an Einfamilienhäusern (ISI), Mietwohnungen in Mehrfamilienhäusern haben selten Ladepunkte (ADAC). **Mieter sitzen in der Stadt, die Anbieter eher am Stadtrand und auf dem Land.** Nähe ist die Kernbotschaft (I.3), aber die akzeptierte Distanz zur Lademöglichkeit beträgt im Median **101 m**, bei 25 % höchstens 41,75 m; nur „etwas mehr als 30 %“ gehen 250 m oder mehr (ISI-Studie, S. 45–46; Befragte aus Mehrparteienhäusern, hypothetisch, in Städten größere Distanzen). | **Spannung, nicht gelöst.** Das Matching Fahrer und Anbieter auf kurze Distanz ist die offene Kernfrage |
| Land (F2) braucht Sharing | Es gibt **keine Primärdaten** zu Fahrern ohne Lademöglichkeit auf dem Land. Auf dem Land dominiert nach allgemeiner Annahme das Eigenheim; das ist für Wallboxen belegt (siehe oben), für den Bedarf nicht. | **Nicht belegt** |

**Empfehlung zur Schärfung (die Gruppe entscheidet):** Die Zielgruppe nicht als „alle ohne Wallbox“ führen, sondern als zwei Teile: (1) **heutige** E-Auto-Fahrer, die nicht zu Hause laden (rund 20 %, nach Fraunhofer), (2) **latente** Fahrer in Mietwohnungen (nicht quantifiziert). Die Frage „wie weit gehen sie zur nächsten privaten Wallbox“ gehört als Erstes in die Umfrage von Niclas, weil sie über die Machbarkeit des Matchings entscheidet.

## 2 Belegprüfung der Aussagen in 03b
| Aussage in 03b | Primärquelle (Abruf 2026-11-09) | Ergebnis |
|---|---|---|
| BEV-Bestand 2.034.260 am 1.1.2026, +23,2 % | KBA, Pressemitteilung Nr. 09/2026 vom 03.03.2026, „Der Fahrzeugbestand am 1. Januar 2026“: https://www.kba.de/DE/Presse/Pressemitteilungen/Fahrzeugbestand/2026/pm09_fz_bestand_pm_komplett.html : 2.034.260 BEV, Anteil 4,1 %, +23,2 %; Pkw gesamt 49.486.487. | **Primär bestätigt.** Der Wert 1.651.643 für 1.1.2025 steht in der Pressemitteilung nicht; er ist mit +23,2 % rechnerisch stimmig, bleibt aber sekundär |
| Öffentliche Ladepunkte 212.064 (1.8.2026), +15,6 % | Bundesnetzagentur, https://www.bundesnetzagentur.de/ladeinfrastruktur : **157.762 Normalladepunkte und 56.572 Schnellladepunkte (zusammen 214.334) am 1. September 2026**, „enthalten auch Meldungen aus noch nicht abgeschlossenen Anzeigeverfahren“. Die 212.064 (1.8.2026) und die +15,6 % stehen in der Presse (electrive, 07.09.2026), die Seite nannte sie nicht. | **Primär bestätigt mit neuerem Stand (214.334).** Die +15,6 % bleiben sekundär |
| Auslastung öffentlicher Ladepunkte rund 12 % (BDEW) | BDEW-Seite https://www.bdew.de/energie/elektromobilitaet-dossier/ladesaeulen-ladeinfrastruktur/ nennt „durchschnittlich nur zwölf Prozent zeitgleich belegt“, **ohne Quelle, Methode oder Zeitraum**; BDEW-Primärbericht nicht gefunden. | **Nur auf Verbandsseite, ohne Primärbeleg.** Als „BDEW-Angabe“ kennzeichnen |
| 82 % laden zu Hause | siehe Abschnitt 1 | durch Fraunhofer ISI (rund 80 %) ersetzen |
| Konsolidierung erwartet | auto motor und sport: „Branchenbeobachter rechnen mit einer Konsolidierung“, Quelle „frühere Analysen“ ungenannt | **Sekundär, nicht primär belegbar** |
| Cocharge: 0,59 €/kWh brutto, 75 € Anschlussgebühr, keine Monatsgebühr, kein Prozentsatz | https://cocharge.de : alle Angaben bestätigt; **kein Provisionssatz** auf der Seite | **Primär bestätigt** |
| AirElectric: kostenlos, ohne Werbung, Destination Charger, API/White-Label, Zielgruppe auch Hotels und Ferienhausvermieter; **keine Reservierung, keine Preise, keine Provision** auf der Seite | https://airelectric.de | **Primär bestätigt.** Neu: Der „Destination Charger“ (Hotels, Ferienhäuser, private Anbieter, Laden über Nacht) konkurriert direkt mit unserem Segment A2 (Hotels, Gastronomie, Parkplätze) |
| Zahlungsdienstleister: Stripe, Mollie Preise | Herstellerseiten, abgerufen 2026-10-26 (`zahlungsdienstleister.md`) | **Primär**, älter als eine Woche, vor Verwendung neu prüfen |
| Zahlungsbereitschaft 6,84 € je 100 km, Median 101 m, F-05 geteiltes Laden | Fraunhofer-ISI-Studie, Primärquelle gelesen am 2026-10-26 (`teilungs-und-zahlungsbereitschaft.md` Abschnitt D) | **Primär**, aber hypothetisch, Befragte aus Mehrparteienhäusern mit eigenem Auto; F-05 meint Teilen **im gleichen Wohnhaus**, nicht mit fremden Nachbarn. In 03b als Beleg für „Teilen mit Fremden“ **zu stark** formuliert |
| Wallbox-Sharing ist kein Massenmarkt, Wirtschaftlichkeit offen | pv magazine, 19.06.2026, Fachbeitrag (Sekundär, ohne Zahlen) | **Sekundär, qualitativ** |
| Take Rate Airbnb rund 13 % | FourWeekMBA (Sekundär); Geschäftsbericht nicht abgerufen | **Nur Sekundär** |
| Teilungsbereitschaft begrenzt | pv magazine, Interviews mit Plattformbetreibern, qualitativ | **Sekundär**; Primärstudie fehlt (A-08 bleibt Annahme) |

## 3 Was an 03b und der Marktrechnung zu ändern ist
1. **Heimladen-Anteil:** 20 % (Fraunhofer ISI, Primärquelle) statt 18 % (BDEW, ohne Quelle). Wirkung auf die Marktrechnung: Nicht-Heimlader 406.852 statt 366.167 (+11,1 %); alle Nachfragewerte steigen um denselben Faktor (Markt im realistischen Szenario rund 12,1 statt 10,9 Mio. €). Die Gruppe entscheidet, ob die Rechnung angepasst wird; bis dahin gilt die Rechnung mit 18 % als vorsichtig.
2. **Aussage „Unser Segment ist genau der Teil, den die Substitute nicht abdecken“** in 03b ist zu stark: Wer nicht zu Hause lädt, nutzt Arbeitgeber, öffentliche Säulen oder Schnelllader; wie viele davon Sharing wollen, ist ungeprüft.
3. **F-05 (Teilen im Wohnhaus)** ist kein Beleg für die Bereitschaft, mit Fremden aus der Nachbarschaft zu teilen.
4. **Konkurrenz um A2:** AirElectric Destination Charger ergänzen.
5. **Quellen kennzeichnen:** BDEW-Angaben als „Verbandsangabe ohne Primärquelle“, +15,6 % als „Presse“.

## 4 Weiterhin nicht belegbar (Primärquelle fehlt)
- Anteil der Mieter unter den E-Auto-Fahrern ohne Heimladen; Anteil der latenten Käufer in Mietwohnungen.
- Bedarf auf dem Land (F2); Zahl privater und gewerblicher Wallboxen (nur AlixPartners über Statista, Methodik unbekannt).
- Teilungsbereitschaft von Wallbox-Besitzern; Zahlungsbereitschaft für **Sharing** (nicht für Laden insgesamt).
- Rendite der Branche (`branchenrendite.md`).

## 5 Noch zu beschaffen (nächste Schritte)
- Fraunhofer ISE/ISI (2024), „Potenziale von Stellplätzen an Wohn- und Nichtwohngebäuden“: https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/studies/Studie_Ladeinfrastruktur_MFH_und_Nichtwohngebäude.pdf . Eine Suchzusammenfassung nennt dort „ca. 80 % der heutigen BEV-Halter haben eine einfache private Lademöglichkeit“; das PDF ließ sich hier nicht auslesen (komprimiert, kein Textwerkzeug installiert), die Stelle ist **ungeprüft**.
- Mobilität in Deutschland (MiD 2023, BMV): Aufschlüsselung der E-Auto-Haushalte nach Wohnform und Stellplatz.
- NOW GmbH / Nationale Leitstelle, „Einfach zu Hause laden“ (Befragung von KfW-440-Wallbox-Besitzern, laut Leitstelle-Folien 51.893 Fragebögen, September/Oktober 2022): beste Quelle zum **Anbieterprofil**; bisher nur aus Suchtreffern bekannt.
- BDEW-Primärbericht (Elektromobilitätsmonitor) für Heimladen und Auslastung.
- Eigene Erhebung durch Niclas: Distanzbereitschaft, Heimladen, Teilungsbereitschaft, Zahlungsbereitschaft für Sharing.
