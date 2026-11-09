# 2 Produkt und Dienstleistung

Status: Entwurf, Entscheidungen der Gruppe vom 2026-10-19. Offene Punkte sind markiert.

Neuester Stand zum Geschäftsmodell (Jannik, 2026-11-02): `kapitel/00c-geschaeftsmodell.md`. Abweichungen zu den Beschlüssen unten (Gerät, Versicherung, Solar, Erlöse) stehen dort in Abschnitt 13; die Gruppe klärt sie.

## 2.1 Produkt
Digitale App für Wallbox-Sharing. Private Wallbox-Besitzer („Anbieter“) stellen ihre Wallbox zeitweise E-Auto-Fahrern („Kunden“) zur Verfügung. Ein Anbieter kann sich in derselben App auch als Kunde registrieren.

## 2.2 Dienstleistungen
| Nr. | Dienstleistung | Inhalt | Status |
|---|---|---|---|
| D-1 | Vermittlung | Zusammenbringen von Kunde und Anbieter über die App | beschlossen |
| D-2 | Abrechnung und Zahlungsabwicklung | Abrechnung zwischen Anbieter und Kunde, Zahlungsabwicklung | beschlossen |
| D-3 | Versicherung und Support | Absicherung über einen Partnerversicherer (Provision, kein Eigenrisiko) und Kundensupport. **Umfang (2026-10-26):** Police für **Anbieter und Fahrer, geteilt** (Schäden an Wallbox und Grundstück, Haftung beim Laden); Support im Pilot über **In-App-Hilfe und E-Mail, kein Telefon**; Schäden über den Partnerversicherer | beschlossen, Partner und Policen-Details offen |
| D-4 | Energie-Services | **Umfang (2026-10-26):** PV-Überschuss einbinden und Ladezeit-Steuerung nach Strompreis; **erst nach dem Pilot** (braucht Gadget-Daten und Energiepartner) | beschlossen, Phase nach Pilot, Details offen |
| D-5 | Installationsservice | Kleines Gerät („Gadget“), das der Anbieter in seine bestehende Wallbox einsteckt und das sie an das Sharing-System anschließt; wird nach Registrierung kostenlos zugeschickt | beschlossen |
| D-6 | Wallbox-Radar | Kartenfunktion in der App zum Finden verfügbarer Wallboxen | beschlossen |
| D-7 | Weitere Dienstleistungen | Können später dazukommen | offen |

Abgrenzung: Das Unternehmen vermittelt keine Wallbox selbst, sondern nur das Gerät zum Anschluss einer bestehenden Wallbox.

## 2.3 Offene Punkte
- Technische Machbarkeit des Gadgets (Kompatibilität mit vorhandenen Wallboxen, Messung/Eichrecht) – zu recherchieren
- Gadget: kostenlos für den Anbieter, aber mit **Pfand mit Rückerstattung bei Rückgabe** (bestätigt 2026-10-26; Abwicklung über den Zahlungsdienstleister). **Pfandhöhe wird im Pilot getestet**, nicht vorab festgelegt (zwei Höhen vergleichen); Rückgabebedingungen offen
- Kosten des Gadgets pro Anbieter noch unbekannt (Annahme nötig, siehe `ANNAHMEN-GLOSSAR.md`)
- Details zu D-3 (Partnerversicherer, Policen, Deckungssummen, Selbstbehalt, Schadensprozess) und D-4 (Energiepartner, Technik, Datenzugriff)
- Erlös- und Preismodell

## 2.4 Erlösquellen (Entwurf, Preise offen)
| Nr. | Quelle | Anmerkung |
|---|---|---|
| E-1 | Provision pro Ladevorgang | Haupteinnahme |
| E-2 | Premium-Abo für Kunden | Umfang offen |
| E-3 | Energie-Marge und Partnerprovisionen | Z. B. Energie- oder Versicherungspartner |
| E-4 | Werbung in der App | Kleine Werbeanzeigen |
| E-5 | Reservierungsgebühr | Wallbox reservierbar; wird die Reservierung nicht genutzt, wird der Betrag automatisch vom Kunden abgebucht |
| E-6 | Staatliche Förderung/Provision | Nur Hoffnung, keine gesicherte Einnahme – Existenz geeigneter Programme zu recherchieren, im Finanzplan nicht fest einplanen |

## 2.5 Entscheidungen zum Erlösmodell (Grill-me, 2026-10-26)
Preise und Prozentsätze sind **nicht festgelegt** und stehen erst mit Quelle oder als Annahme (A-nn) im Finanzplan.

| Nr. | Quelle | Entscheidung | Offen |
|---|---|---|---|
| E-1 | Provision je Ladevorgang | Der **Anbieter zahlt einen Anteil vom Erlös** (Fahrer zahlt den Ladepreis, wir behalten einen Prozentanteil) | Prozentsatz (Annahme) |
| – | Preis pro kWh | **Anbieter legt den Preis innerhalb einer Preisspanne fest**; wir geben Orientierung oder Obergrenze | Spanne, Obergrenze, kartell- und preisrechtliche Prüfung nicht gemacht |
| E-2 | Premium-Abo für Fahrer | **Kein Abo im Pilot.** Später: niedrigere Servicegebühr oder Rabatt für Vielnutzer | Preis, Umfang, Zeitpunkt |
| E-3 | Partnerprovisionen | **Im Pilot keine.** Danach: Versicherungs-Provision (D-3) und Hardware-Zubehör; Energie (D-4) offen | Partner, Verträge, Höhe |
| E-4 | Werbung | **Nicht im Pilot**, später prüfen | Ob überhaupt |
| E-5 | Reservierungsgebühr | **Nur bei Nichtnutzung**; Reservierungsdauer **30 Minuten**; Reservierung selbst kostenlos | Gebührenhöhe, Anteil für den Anbieter, verbraucherrechtliche Zulässigkeit (Z-11 in `05a-ressourcen.md`), technische Abwicklung über den Zahlungsdienstleister |
| E-6 | Staatliche Förderung | nur Hoffnung, nicht fest einplanen | – |

Folge für den Pilot: Einnahmen entstehen aus **Provision je Ladevorgang (E-1) und Reservierungsgebühr (E-5)**. Abo, Partnerprovisionen und Werbung laufen im Finanzplan des Piloten mit null.
