# Kundensegmente (vorläufige Fassung)

Aufgabe: „Segmentieren Sie Ihre Kundschaft nach ihren Bedürfnissen, Verhaltensweisen und anderen Merkmalen, die sich darauf auswirken, wie sie Ihre Produkte oder Services wertschätzen.“

Stand: vorläufig, 2026-10-26. Die Segmente sind **Hypothesen der Gruppe**, nicht durch Daten belegt, bis Interviews und Umfrage vorliegen. Segmentgrößen sind nicht angegeben (keine belegten Zahlen). Grundlage: Grill-me vom 2026-10-26, `kapitel/01a-kunden.md`, `kapitel/01b-personas.md`.

Unser Geschäftsmodell ist ein Zwei-Seiten-Markt. Wir segmentieren **beide Seiten getrennt**, weil sie unterschiedlich zum Wert beitragen: Fahrer nach Ladesituation und Bedarf, Anbieter nach Motivation.

## 1 Fahrer (Kundenseite), Basis: Ladesituation und Bedarf
Für alle Fahrer-Segmente gilt: Wichtig sind Verfügbarkeit und Planbarkeit, Preis, Nähe zum Wohnort oder zur Strecke sowie Einfachheit und Vertrauen. Beim Pilot-Segment F1 ist **Verfügbarkeit und Planbarkeit** das wichtigste Merkmal (Entscheidung der Gruppe).

| Segment | Merkmale und Situation | Bedürfnis | Verhalten (Hypothese) | Wertschätzt besonders | Pilot |
|---|---|---|---|---|---|
| **F1 Mieter ohne Ladeplatz** (eher Stadt) | Wohnt zur Miete, E-Auto vorhanden oder geplant, kein eigener Ladepunkt | Planbar und günstig im Wohnumfeld laden | Lädt regelmäßig, abhängig von öffentlichen Säulen (belegt oder weit weg, schwankende Preise) | Wallbox-Radar, Reservierung, verlässliche Preise, Stammplatz | **ja, Hauptzielgruppe** |
| **F2 Land ohne Wallbox** | Wohnt auf dem Land, kein eigener Ladepunkt, lange Fahrten | Laden in der Nähe von Wohnort oder Strecke, Planungssicherheit | Weite Wege, wenig öffentliche Infrastruktur | Verlässliche Anbieter im Umkreis, Sichtbarkeit im Radar | **ja, Hauptzielgruppe** |
| **F3 Akuter Bedarf unterwegs** | Reise oder Pendeln, braucht kurzfristig Laden (Stadt oder Land) | Schnell eine freie, verlässliche Wallbox | Unregelmäßig, zeitkritisch, vermutlich höhere Zahlungsbereitschaft (Annahme) | Echtzeit-Verfügbarkeit, Reservierung (E-5) | später, aus F1/F2 ableitbar |

Hinweis: Die frühere Persona K-3 („E-Auto, aber kein Ladeort“) wird als **Oberbegriff** für F1 und F2 geführt, nicht als eigenes Segment. Weitere Gruppen aus `01a-kunden.md` (Pendler und Alltagslader, preisbewusste Fahrer, Reisende) sind Merkmale innerhalb dieser Segmente, keine eigenen Segmente.

## 2 Anbieter (Wallbox-Besitzer), Basis: Motivation
Zusatzmerkmal für alle Anbietersegmente: **privat oder gewerblich** (Kleingewerbe, Firmen mit freien Ladepunkten). Gewerbliche Anbieter zählen laut Beschluss von Anfang an dazu; rechtliche und steuerliche Folgen sind ungeklärt.

| Segment | Merkmale (Hypothese) | Bedürfnis | Sorgen/Barrieren | Wertschätzt besonders | Pilot |
|---|---|---|---|---|---|
| **A1 Einkommensorientiert** | Möchte die Wallbox besser auslasten und Geld verdienen | Zusatzeinkommen | Haftung, Schäden, Steuern und Gewerbe-Status, Fremde auf dem Grundstück | Abrechnung (D-2), Versicherung (D-3), klare Einnahmen | **ja, Fokus des Piloteinstiegs** (Entscheidung der Gruppe) |
| **A2 Service- und Komfortorientiert** | Will wenig Aufwand, offen für Teilen, wenn alles geregelt ist | Rundum-Service ohne Technikaufwand | Technik und Einrichtung, Aufwand, Privatsphäre | Gadget zum Einstecken (D-5), Support, Zeitfenster-Regeln | ja, mitgedacht |
| **A3 Nachhaltigkeit und Gemeinschaft** | Will vorhandene Infrastruktur sinnvoll nutzen und der Region helfen; eher auf dem Land | Beitrag zu Nachhaltigkeit, Gemeinschaft | Wenig Nachfrage vor Ort, Fremde, Aufwand | Sichtbarkeit im Radar, einfacher Betrieb | ja, mitgedacht |

## 3 Wie sich die Segmente auf den Wert auswirken (Hypothesen)
- Fahrer F1 und F2 entscheiden vor allem nach Verfügbarkeit und Planbarkeit; ohne Anbieterdichte in ihrer Nähe entsteht kein Nutzen (Zwei-Seiten-Effekt).
- Anbieter A1 treten bei klarem Verdienst und geklärter Haftung bei; A2 bei geringem Aufwand; A3 bei Sinn und Sichtbarkeit.
- Erlösrelevanz: Provision je Ladevorgang trifft alle Segmente; Reservierungsgebühr und Premium-Abo sprechen vor allem F3 und F1 an (Annahme).

## 4 Was belegt ist und was nicht
- **Nicht belegt:** Größe der Segmente, Anteil teilungsbereiter Besitzer, Zahlungsbereitschaft, Häufigkeit des Ladens (siehe `recherche/teilungs-und-zahlungsbereitschaft.md`).
- **Teilweise belegt, Orientierung:** Laut BDEW laden rund 82 % der E-Auto-Fahrer zu Hause (Seitenstand 29.07.2026, `recherche/private-wallboxen-deutschland.md`), also rechnerisch rund 18 % nicht; das ist eine Näherung, kein Segment F1/F2. Fraunhofer ISI (Befragte aus Mehrparteienhäusern, hypothetisches Szenario, Stand 2025): Hälfte akzeptiert höchstens ca. 100 m zur Lademöglichkeit; geteilte Lösungen werden mit Kostenvorteil deutlich attraktiver (`recherche/teilungs-und-zahlungsbereitschaft.md`, Abschnitt D). Das stützt Nähe und Preis als Wertmerkmale, belegt aber keine Sharing-Nachfrage.
- Stichproben im Bekanntenkreis sind nicht repräsentativ und werden so gekennzeichnet.

## 5 Vorläufig, noch zu klären
1. Segmentgrößen (Marktrechnung: kleinerer Wert aus Angebot und Nachfrage, `kapitel/03a-markt-entscheidungen.md`).
2. Zahlungsbereitschaft je Segment (A-09) und Teilungsbereitschaft der Anbieter (A-08).
3. Gewerbliche Anbieter: eigener Vertrag oder wie private behandeln; Steuer- und Rechtsfolgen.
4. Überschneidung F1/F2 und Reihenfolge in der Stadt/Land-Pilotierung (Spannung: Mieter in der Stadt, Wallboxen eher auf dem Land).
5. Interviewleitfaden und Umfrage aus den offenen Punkten ableiten (Rolle R3, Niclas).
6. Personas (`kapitel/01b-personas.md`) an die neue Segmentierung anpassen.
