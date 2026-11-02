# Erster Überblick: Produkt, Kunde, Markt

Stand: 2026-10-19, Arbeitsentwurf für das Gruppentreffen. Zahlen mit Quelle stehen in `recherche/quellen.md`. Alles mit **[Annahme]** ist eine Hypothese der Gruppe und noch nicht belegt.

## 1 Produkt
- App für Wallbox-Sharing in Deutschland (später DACH). Details siehe `02-produkt-dienstleistung.md`.
- Kern: Vermittlung, Abrechnung und Zahlung, Versicherung (Partnerversicherer) und Support, Energie-Services, Installationsservice (Gadget gegen Pfand) und Wallbox-Radar.
- Zwei Rollen in einer App: **Anbieter** (stellt Wallbox bereit) und **Kunde** (lädt). Ein Anbieter kann zugleich Kunde sein.
- Wertversprechen **[Annahme]**:
  - Anbieter: zusätzliche Einnahmen aus einer sonst ungenutzten Wallbox, Abrechnung und Absicherung ohne eigenen Aufwand.
  - Kunde: Ladepunkte in Wohnortnähe, oft günstiger oder bequemer als öffentliche Ladesäulen, per Radar auffindbar und reservierbar.

## 2 Kunden (B2C)
Aktueller Stand der Gruppe (Anbieter zuerst, zwei Piloten Stadt/Land, Zielgruppe Mieter und Landbewohner): siehe `01a-kunden.md`. Die folgende Tabelle ist der frühere Entwurf.

| Segment | Beschreibung | Bedürfnis | Status |
|---|---|---|---|
| Anbieter | Privatpersonen mit Wallbox | Nebeneinkommen, Auslastung, Rechtssicherheit | **[Annahme]** |
| Kunde A | E-Auto-Fahrer ohne eigene Lademöglichkeit (z. B. Mieter) | Zuverlässiges Laden in Wohnortnähe | **[Annahme]** |
| Kunde B | Unterwegs-Lader, Pendler, Reisende | Mehr Auswahl als öffentliche Säulen, Preis, Reservierung | **[Annahme]** |
| Später | Firmen als Anbieter von Ladepunkten | Auslastung von Firmen-Ladepunkten | offen, spätere Phase |

Offene Fragen an die Gruppe: Welches Segment ist der Einstieg? Welche Regionen oder Stadttypen zuerst? Gibt es Personas?

## 3 Markt
### 3.1 Nachfrage (E-Autos)
- Bestand BEV in Deutschland am 1.1.2026: 2.034.260, nach 1.651.643 am 1.1.2025 (+382.617 im Jahr 2025).
- Neuzulassungen 2025: 545.142 BEV. August 2026: 68.930 BEV, 32,4 % Marktanteil an den Neuwagen.
- Folgerung: Der Bestand wächst weiter, die potenzielle Kundengruppe nimmt zu.

### 3.2 Angebot (Ladeinfrastruktur)
- Öffentliche Ladepunkte am 1.8.2026: 212.064 (+15,6 % zum Vorjahr), davon 156.399 Normal- und 55.665 Schnellladepunkte.
- Private Ladepunkte: laut AlixPartners (über Statista) 2.359 Tsd. im Jahr 2023, Prognose 4.069 Tsd. für 2030; Methodik unbekannt. Belegte Untergrenze: ca. 690.000 geförderte (NOW GmbH, 2021–2022). Details: `recherche/statista-auswertung.md`, `recherche/private-wallboxen-deutschland.md`.
- Laut BDEW laden rund 82 % der E-Auto-Fahrer zu Hause (Stand 29.07.2026). Die Zahl zu Hause oder am Arbeitsplatz aus 2021 (9 von 10) ist nicht belegt.
- Ein Fachbeitrag (pv magazine, Juni 2026) nennt private Ladepunkte mehr als 90 % der Zeit ungenutzt. Das ist die Kernthese für das Angebot, aber eine einzelne Quelle.

### 3.3 Wettbewerb
- Genannte Anbieter laut Ratgebern: Cocharge, AirElectric, Sharepnp, &Charge, YouCharge.Me, Obelisk; Plugsurfing in einer Liste. Die Listen sind teils undatiert und widersprüchlich.
- ChargeAtFriends soll den Betrieb zum 31.5.2026 eingestellt haben (eine Quelle, ungeprüft).
- Cocharge: Standardpreis 0,59 €/kWh brutto, ca. 15 % Provision (Angabe aus Ratgeber, ungeprüft).
- Wallbox-Sharing ist laut Quellen bisher **kein Massenmarkt**; als Haupthindernis gelten Haftung, Versicherung und Steuer- bzw. Eichrecht, nicht die Technik.
- Indirekte Konkurrenz: öffentliche Ladenetze und Roaming-Anbieter.

### 3.4 Rechtlicher Rahmen (erste Hinweise, unvollständig)
- Teilen ohne Gewinnerzielungsabsicht gilt als private Nutzung; regelmäßige Gewinne über eine Plattform gelten als gewerblich (Angabe EnBW).
- Für öffentliches Sharing ist das Eichrecht relevant (Angabe energiefluss24). Das betrifft direkt das Gadget.

## 4 Erste Einschätzung
- Rückenwind: wachsender E-Auto-Bestand, dichter werdende, aber noch endliche öffentliche Infrastruktur, ungenutzte private Kapazität.
- Risiken: Markt bisher klein, Wettbewerber teils gescheitert, Rechts- und Eichrechtsfragen, Henne-Ei-Problem (ohne Anbieter keine Kunden).
- Unser Differenzierungsansatz **[Annahme]**: Gadget für bestehende Wallboxen, Rundum-Service (Abrechnung, Versicherung, Support) und Radar in einer App.

## 5 Aufgaben für die Gruppe
1. Einstiegssegment und Personas festlegen.
2. Zahl privater Wallboxen und Anteil der E-Auto-Fahrer ohne Heimladen recherchieren (z. B. Bundesnetzagentur, KBA, BDEW, Studien).
3. Wettbewerber einzeln prüfen (Preise, Funktionen, Stand 2026).
4. Eichrecht und Steuern für das Gadget klären.
5. Marktgröße berechnen (TAM/SAM/SOM) und in `ANNAHMEN-GLOSSAR.md` eintragen.
