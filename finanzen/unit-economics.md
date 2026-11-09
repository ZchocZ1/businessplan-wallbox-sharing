# Unit Economics je Anbieter (II.3, Option 1)

Stand: 2026-11-09. Rechnung der Rendite aus dem eigenen Modell, weil keine Branchenrendite belegt ist (`recherche/branchenrendite.md`). **Alle Eingaben sind Annahmen mit ID oder belegte Listenpreise; die Ergebnisse sind Szenarien, keine Prognose.** Grundlage: `kapitel/00d-geschaeftsmodell-zielmarkt-beschluesse.md` (Provision im kWh-Preis enthalten, Pilot-Erlöse Provision und Reservierungsgebühr).

## 1 Eingaben
| Größe | Pessimistisch | Realistisch | Optimistisch | Status |
|---|---|---|---|---|
| kWh je Anbieter-Wallbox und Monat (A-15) | 100 | 200 | 340 | **Annahme.** 340 ist der Durchschnitt aus dem Cocharge-Rechner (Herstellerangabe, `recherche/branchenrendite.md` R-04), also keine gemessene Nutzung; 100 und 200 sind frei gesetzt |
| kWh je Ladevorgang (A-16) | 20 | 20 | 20 | **Annahme**, nicht belegt |
| kWh-Preis brutto, Fahrer zahlt (A-14) | 0,45 € | 0,55 € | 0,59 € | **Annahme**; 0,59 € = Cocharge-Verkaufspreis (belegt als Wettbewerberpreis); MwSt-Behandlung ungeklärt, alle Beträge brutto gerechnet |
| Provisionssatz, im Preis enthalten (A-14) | 10 % | 15 % | 20 % | **Annahme**; 15 % ist kein Beleg (`recherche/wettbewerber.md`, Abschnitt B) |
| Zahlart-Mix (A-17) | 100 % Karte EWR | 100 % Karte EWR | 100 % Karte EWR | **Annahme** (vorsichtig; SEPA wäre mit 0,35 € je Vorgang meist günstiger) |
| Zahlungskosten | 1,5 % + 0,25 € je Vorgang | dito | dito | belegt: Stripe-Listenpreis (`recherche/zahlungsdienstleister.md`); **kein Anbieterbeschluss** |
| Plattformkosten Connect | 2 € je aktivem Anbieter und Monat; 0,25 % + 0,10 € je Auszahlung (eine Auszahlung pro Monat) | dito | dito | belegt: Stripe Connect, „Sie übernehmen die Preisgestaltung“ (dieselbe Datei) |

Nicht enthalten, weil unbekannt: Reservierungsgebühren (E-5; Höhe und Quote offen, im Szenario null), Support- und Versicherungskosten je Anbieter (D-3; offen), Gadget-Kosten (A-02 offen), Marketing, Hosting, Personal.

## 2 Rechnung je Anbieter und Monat
Formeln: Umsatz = kWh × Preis; Vorgänge = kWh / 20; Provision = Satz × Umsatz; Zahlungskosten = 1,5 % × Umsatz + 0,25 € × Vorgänge + 2 € + 0,25 % × (Umsatz − Provision) + 0,10 €; **Deckungsbeitrag I (DB I) = Provision − Zahlungskosten**.

| Größe | Pessimistisch | Realistisch | Optimistisch |
|---|---|---|---|
| Umsatz (Fahrer zahlt) | 45,00 € | 110,00 € | 200,60 € |
| Ladevorgänge | 5 | 10 | 17 |
| Provision | 4,50 € | 16,50 € | 40,12 € |
| Zahlungskosten | 4,13 € | 6,48 € | 9,76 € |
| **DB I je Anbieter und Monat** | **0,37 €** | **10,02 €** | **30,36 €** |
| Zahlungskosten in % der Provision | 91,7 % | 39,3 % | 24,3 % |
| Anbieter erhält (Umsatz − Provision, vor eigenen Steuern) | 40,50 € | 93,50 € | 160,48 € |
| Provisionssatz, bei dem DB I = 0 | 9,2 % | 5,9 % | 4,9 % |

## 3 Gadget-Rückzahlung (Sensitivität)
Gadget-Kosten sind offen (A-02). Die drei Beträge sind **Rechenbeispiele, keine Schätzung**. Rückzahlung der Kosten in Monaten = Gadget-Kosten / DB I. Das Pfand mit Rückerstattung deckt das Risiko nur teilweise und fließt nicht ein.

| Gadget-Kosten (Beispiel) | Pessimistisch | Realistisch | Optimistisch |
|---|---|---|---|
| 20 € | 53,5 Monate | 2,0 Monate | 0,7 Monate |
| 40 € | 107,0 Monate | 4,0 Monate | 1,3 Monate |
| 60 € | 160,5 Monate | 6,0 Monate | 2,0 Monate |

## 4 Break-even je Region (nur Formel, keine Zahl)
Anbieter, die für den Break-even je Region nötig sind = monatliche Fixkosten der Region / DB I je Anbieter. Fixkosten (App, Hosting, Personal, Marketing, Support) sind **nicht belegt und nicht angenommen**; eine Zahl entsteht erst mit dem Finanzplan (`finanzen/kapitalbedarf-kostenpositionen.xlsx`, bisher ohne Beträge). Beispiel zur Lesart, kein Ergebnis: Bei 1.000 € Fixkosten je Region und Monat (frei gesetzt) wären es im realistischen Szenario 100 aktive Anbieter, im optimistischen 33, im pessimistischen über 2.700.

## 5 Aussagen und Grenzen
- **Rendite hängt fast vollständig an der Nutzung je Wallbox (A-15).** Im pessimistischen Szenario frisst die Zahlungsabwicklung die Provision auf; unter ca. 100 kWh je Monat trägt das Modell ohne Mindestgebühr nicht. Das stützt die Reservierungsgebühr (E-5) und die späteren Abos als Ergänzung, ist aber noch kein Beleg dafür.
- Die Fixkosten je aktivem Anbieter (2 € Stripe Connect) wirken stark bei kleinen Umsätzen (Pilot).
- Offene Kostenblöcke (Versicherung, Support, Gadget, Personal) verschlechtern jedes Ergebnis; DB I ist eine **Obergrenze** des Beitrags.
- Preis- und Provisionsannahmen (A-14) sind Spannen für den Finanzplan und keine Aussage zu zulässigen Preisen (Preisspanne rechtlich ungeprüft).
- Nächste Schritte: A-15 mit Pilotdaten und Interviews prüfen; Zahlungsanbieter wählen und Konditionen anfragen (Zahlart-Mix); Reservierungsgebühr als Szenario ergänzen; Excel-Modell auf diese Formeln aufsetzen (Tim, R5).
