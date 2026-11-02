# Schlüsselressourcen

Status: **Entwurf, E-1 bis E-7 mit der Gruppe entschieden**, Stand 2026-10-26. Grundlage: Grill-me-Entscheidungen der Gruppe vom 2026-10-26 sowie `kapitel/02-produkt-dienstleistung.md`, `recherche/`. Offene Entscheidungen sind mit **[E-n]** markiert und werden mit der Gruppe geklärt. Zahlen (Kosten, Beträge) stehen nur mit Quelle oder als Annahme (A-nn); bisher sind keine Beträge eingetragen (`finanzen/kapitalbedarf-kostenpositionen.xlsx`).

Aufgabe: „Geben Sie die physischen, intellektuellen, personellen und finanziellen Ressourcen an, auf die Ihr Geschäftsmodell angewiesen ist.“ Bezug: Kapitel 2 (Produkt), 5 (Organisation und Team), 6 (Rechtsform), 7 (Finanzplan), 8 (Risiken).

## 1 Kernaussage
Das Geschäftsmodell ist eine Zwei-Seiten-Plattform (Wallbox-Anbieter und E-Auto-Fahrer). Ihr Wert entsteht durch **Software und Daten**, die wir selbst besitzen. Die **kritischste Ressource sind deshalb die intellektuellen Ressourcen** (App, Radar/Reservierung, Gadget-Firmware, Nutzerdaten). Hardware (Gadget) ist der Hebel zur Abgrenzung, aber zugleich das größte Vorfinanzierungs- und Zulassungsrisiko. Zahlung, Versicherung und Fertigung werden über Partner eingekauft. Zulassungen und Berechtigungen (Eichrecht, CE, Zahlungserlaubnis, Registereintrag, Marke) sind Voraussetzung für Betrieb und Schutz; ihre Prüfung steht weitgehend aus (Abschnitt 3a).

| Rang | Ressourcenart | Warum |
|---|---|---|
| 1 | Intellektuell | Plattform, Netzwerkeffekt, Alleinstellung durch Gadget-Anbindung und Radar |
| 2 | Personell und Partner | 6 Studierende ohne Hardware-Entwickler, vier zwingende Partnergruppen |
| 3 | Finanziell | Vorfinanzierung von Entwicklung und Gadgets vor ersten Umsätzen |
| 4 | Physisch | Gadget in Auftragsfertigung; sonst wenig eigene Hardware |

## 2 Intellektuelle Ressourcen
| Baustein | Bedarf | Beschaffung | Eigenbesitz | Status |
|---|---|---|---|---|
| App-MVP: Vermittlung (D-1) und Abrechnung (D-2) | Anbieter listen, Fahrer finden, bezahlen | Mischform: extern oder White-Label (Beschluss) | Teilweise | Anbieterwahl offen |
| Wallbox-Radar und Reservierung (D-6) | Suche, Verfügbarkeit, Reservierung | später Eigenentwicklung | ja | nach dem MVP |
| Gadget-Anbindung und Firmware (D-5) | Steuerung und Messung der bestehenden Wallbox | Eigenentwicklung, Fertigungspartner baut Hardware | ja | abhängig von Machbarkeit/Eichrecht |
| Nutzerdaten und Bewertungssystem | Vertrauen, Auslastung, Matching | eigene Erhebung in der App; **Hosting in der EU** bei Anbietern mit EU-Rechenzentrum (Beschluss [E-4]) | ja | DSGVO-Konzept offen |
| Abrechnung und Zahlung | Einzug, Auszahlung, Pfand, Reservierungsgebühr | **Zukauf** über Zahlungsdienstleister (kein Eigenbau); Pfand ebenfalls darüber | nein | Rechtslage ungeprüft |
| Marke, Domain | Wiedererkennung | Anmeldung DPMA, Domainsicherung | ja | Klassen offen |
| Patent/Gebrauchsmuster Gadget | Schutz der technischen Lösung | Prüfung durch Patentanwalt | ja, falls anmeldbar | Ergebnis offen |
| Geheimhaltung, Quellcode-Rechte | Schutz gegenüber Agentur und Fertiger | NDAs, Nutzungsrechte im Vertrag, Quellcode im eigenen Besitz | ja | Vertragsvorlagen offen |

Abhängigkeit und Risiko: Bei White-Label-Start bleibt die Plattform zunächst fremd; die Gruppe will die Kernfunktionen später selbst besitzen. Der Wettbewerbsvorteil beruht auf dem Gadget und dem Radar (`recherche/wettbewerber.md`); „Reservierung“ allein ist nicht neu.

## 3 Physische Ressourcen
| Ressource | Bedarf | Beschaffung | Status |
|---|---|---|---|
| Gadget (Einsteckgerät) | Anschluss bestehender Wallboxen ans System, kostenlos gegen Pfand | Auftragsfertigung nach eigenem Design (Beschluss) | Machbarkeit, Eichrecht, CE, Herstellkosten, Mindestabnahme offen |
| Pfand | Sicherheit für Gadget | Abwicklung über Zahlungsdienstleister (Beschluss) | Pfandhöhe und rechtliche Machbarkeit offen |
| Lager, Versand, Rücknahme | Gadgets bevorraten und verschicken, Rückgabe | **Fulfillment-Dienstleister** (Beschluss [E-1]) | Anbieter und Kosten offen |
| Testausstattung für den Pilot | Wallboxen, E-Auto zum Testen, Messtechnik | **Wallboxen der Pilot-Anbieter, E-Auto und Messgeräte geliehen** (Beschluss [E-2]) | Leihpartner offen |
| Büro, IT | Arbeitsplätze, Kommunikation | Hochschule/Privat, später Co-Working | nicht besprochen |

Abhängigkeit und Risiko: Vorfinanzierung der Gadgets bindet Kapital, bis Anbieter aktiv sind oder Geräte zurückkommen. Ohne Zertifizierung kein Verkauf des Gadgets.

## 3a Genehmigungen, Zertifikate und Lizenzen
Das Geschäftsmodell hängt von Zulassungen und Berechtigungen ab, die Dritte erteilen oder die wir erwerben müssen. Sie sind keine eigene Ressourcenart in der Aufgabenstellung, gehören aber zu den intellektuellen und rechtlichen Voraussetzungen. **Keine Rechtsberatung;** Stand der Prüfung je Zeile angegeben. Verantwortlich nach `kapitel/05b-rollen-kompetenzbereiche.md`.

| Nr. | Genehmigung, Zertifikat, Lizenz | Wofür (Ressource) | Stand der Prüfung | Verantwortlich |
|---|---|---|---|---|
| Z-1 | **Eichrechtskonforme Messung und Abrechnung** | Gadget (D-5) und Abrechnung pro kWh | Nicht geprüft. Belegt ist nur: Cocharge verlangt von Anbietern eine „eichrechtskonforme Abrechnung“ (https://cocharge.de, `recherche/wettbewerber.md`). Ob das Gadget das erfüllen kann, ist offen. | Jannik (R2) |
| Z-2 | **CE-Kennzeichnung** und weitere Produktprüfungen des Gadgets | Gadget (Verkauf/Abgabe in der EU) | Nicht geprüft. Bedarf und Umfang unbekannt (Annahme, nicht belegt). | Jannik (R2) |
| Z-3 | **Zahlungsdienst-Erlaubnis** bzw. Nutzung des Zahlungsdienstleisters als Lizenzträger | Abrechnung, Auszahlung an Anbieter, Pfand (D-2) | Nicht geprüft. Nur Herstellerangabe: Mollie schreibt, eine eigene Zahlungsinstitutslizenz sei bei Mollie Connect nicht erforderlich (`recherche/zahlungsdienstleister.md`). Ob unser Modell damit zulässig ist, ist ungeklärt. | Ben (R6) |
| Z-4 | **Meldung/Registrierung von Ladepunkten bei Behörden** (z. B. Bundesnetzagentur), falls nötig | Vermittlung öffentlich zugänglicher Wallboxen | Nicht geprüft. Belegt ist nur: Cocharge übernimmt für Anbieter „die Anmeldung bei der Bundesnetzagentur“ (cocharge.de). Ob das für uns gilt, offen. | Ben (R6) |
| Z-5 | **Eintragung im Handelsregister** (bei UG/GmbH) | Rechtsform, Haftungsbeschränkung | Belegt: Eine GmbH besteht vor der Eintragung nicht; wer vorher handelt, haftet persönlich (§ 11 GmbHG); Registergebühr 225 € (`recherche/rechtsform.md`, `recherche/kosten-belegte-preise.md`). Rechtsform nicht entschieden. | Ben (R6) |
| Z-6 | **Gewerbeanmeldung** | Aufnahme der Geschäftstätigkeit | Nicht an Primärquelle geprüft (Ratgeber nennt ca. 35 €, nicht verwenden). | Ben (R6) |
| Z-7 | **Markeneintragung** (DPMA, ggf. EUIPO) | Marke (intellektuell) | Belegt: DPMA 290 € elektronisch bzw. 300 € Papier bis drei Klassen (`recherche/kosten-belegte-preise.md`). Klassen offen; EUIPO-Gebühren nicht an Primärquelle belegt. | Gregor (R4) |
| Z-8 | **Patent oder Gebrauchsmuster** für das Gadget | Schutz der technischen Lösung | Prüfung beschlossen, Ergebnis offen; Anmeldbarkeit unbekannt. | Jannik (R2) |
| Z-9 | **App-Store-Konten** (Apple Developer Program, Google Play Console) | Veröffentlichung der App | Belegt: Apple 99 USD je Jahr, Google 25 USD einmalig (`recherche/kosten-belegte-preise.md`). | Damian (R1) |
| Z-10 | **DSGVO-Nachweise** (Datenschutzkonzept, Einwilligungen, Verträge mit Auftragsverarbeitern, EU-Hosting) | Nutzerdaten (intellektuell) | Hosting in der EU beschlossen; Konzept noch nicht erstellt, Anforderungen nicht recherchiert. | Damian (R1), Ben (R6) |
| Z-11 | **AGB und Verträge** (Nutzer, Anbieter, Pfand, Haftung, Reservierungsgebühr) | Plattformbetrieb, Pfand, Gebühren | Nicht erstellt, rechtlich nicht geprüft. Verbraucherrechtliche Zulässigkeit der automatischen Abbuchung bei nicht genutzter Reservierung ungeprüft. | Ben (R6) |
| Z-12 | **Versicherung des Unternehmens** (z. B. Betriebshaftpflicht) sowie Partnerversicherung für Anbieter und Fahrer (D-3) | Absicherung der Plattform und der Nutzer | Bedarf und Anbieter nicht geprüft; Partnerversicherer noch nicht gewählt. | Ben (R6) |
| Z-13 | **Steuerliche Einordnung der Stromweitergabe** (privat/gewerblich) und Steuerfragen der Anbieter | Anbieter-Akquise, Preismodell | Nicht belegt. Ratgeber unterscheiden „ohne Gewinnabsicht = privat“ und „regelmäßig mit Gewinn = gewerblich“ sowie eine Freigrenze (EnBW, energiefluss24, Sekundärquellen, nicht geprüft). | Ben (R6), Tim (R5) |
| Z-14 | **Förderbedingungen bei Gebrauch geförderter Ladepunkte** | Gewerbliche Anbieter, Mehrparteienhäuser | Das KfW-Programm für Unternehmen und Kommunen förderte „nicht öffentlich zugängliche“ Ladestationen (Sekundärquelle). Ob geförderte Anlagen für Sharing mit Fremden zulässig sind, ist offen. | Ben (R6), Niclas (R3) |
| Z-15 | **Lizenzen von Dritten** (White-Label-Plattform, Software-Bibliotheken), **Eignungsbescheinigung INVEST** (nur falls Investor mit INVEST) | Software, Finanzierung | Nicht beschafft; Plattformanbieter nicht gewählt; INVEST-Eignung nicht geprüft (`recherche/foerderprogramme.md`). | Damian (R1), Tim (R5) |

Reihenfolge nach Wirkung: Zuerst Z-1 bis Z-3 (Gadget und Zahlung), weil sie Pilot und Abgrenzung blockieren können; Z-5 bis Z-7 hängen an der Rechtsform; Z-9 bis Z-12 vor dem Pilotstart.

## 4 Personelle Ressourcen
- **Team:** 6 Personen, alle DHBW Mannheim, Wirtschaftsingenieurwesen, Fachbereich „Digital Transformation“.
- **Kompetenzbereiche:** (1) Produkt/Softwareentwicklung, (2) Hardware/Technik (Gadget, Eichrecht), (3) Marketing, Vertrieb, Anbieter-Akquise, (4) Finanzen, Recht, Organisation. Zuweisung **individuell nach Interesse und Vorkenntnis**, je Bereich eine verantwortliche Person und eine Vertretung. Zuweisung am 2026-10-26 beschlossen: Damian (R1 Produkt und Software), Jannik (R2 Hardware, Zertifizierung, Logistik), Niclas (R3 Anbieter-Akquise und Pilot), Gregor (R4 Marketing und Marke), Tim (R5 Finanzen und Förderung), Ben (R6 Recht, Partner, Organisation); Details in `kapitel/05b-rollen-kompetenzbereiche.md`.
- **Lücken:** werden extern ausgeglichen (Berater, Partner, spätere Einstellungen). Die Studiengänge sind wirtschaftlich-technisch gemischt; Hardware- und Softwareentwicklung sind aus dem Studiengang allein nicht belegt, deshalb externe Entwicklung (App) und Fertigungspartner (Gadget).
- **Zeitbudget:** 5 bis 10 Stunden pro Person und Woche neben dem dualen Studium (Annahme A-05, Beschluss [E-3]). Das ist Schätzung der Gruppe; daraus folgt, dass Entwicklung und Fertigung extern erfolgen müssen.
- **Externe Partner (zwingend):** Zahlungsdienstleister (zuerst), Fertigungspartner und Zertifizierer, Versicherer (D-3), Energieversorger oder Strompartner (D-4, Umfang offen).
- **Netzwerk als Ressource:** Anbieter-Basis (zuerst gewinnen, Pilot in zwei Regionen) ist ein eigener Engpass. Der Pilot startet erst, wenn je Region eine **Mindestzahl aktiver Anbieter** erreicht ist; die Zahl ist Annahme A-06 und noch offen (Beschluss [E-7]).

Offen/Risiko: Praxispartner und DHBW-Regeln zu Gründung und Nebentätigkeit sind nicht geklärt (`recherche/rechtsform.md`, Abschnitt C).

## 5 Finanzielle Ressourcen
- **Finanzierungsmix:** Eigenmittel, Förderung und Investor. **Reihenfolge in Phasen** (Beschluss [E-6]): Konzept und MVP aus Eigenmitteln und Förderung, Investor erst mit Pilotergebnissen für Gadget und Skalierung. **Eigenmittel** der Gründer freiwillig und unterschiedlich (Beschluss [E-5]; Betrag Annahme A-07, offen). Anteile nicht festgelegt. Bankdarlehen und reines VC wurden nicht gewählt.
- **Förderung (Stand der Recherche, nicht zugesagt):** EXIST (nur über die Hochschule, Team bis 3 Personen), Start-up BW Pre-Seed (Co-Investor und Unternehmen nötig, Stand 2023 belegt), KfW StartGeld (Kredit), INVEST (Zuschuss an Investor) (`recherche/foerderprogramme.md`).
- **Kapitalbedarf:** noch nicht berechnet; bottom-up aus 31 Kostenpositionen (`finanzen/kapitalbedarf-kostenpositionen.xlsx`), jede Zahl mit Quelle oder Annahme A-nn. Belegte Listenpreise: Marke DPMA, Handelsregister, App-Store-Konten, Zahlungsgebühren (`recherche/kosten-belegte-preise.md`, `recherche/zahlungsdienstleister.md`).
- **Rechtsform:** nicht entschieden; beeinflusst Haftung, Stammkapital, Förderfähigkeit (`recherche/rechtsform.md`).
- **Einnahmen als Finanzquelle:** Erlöse E-1 bis E-6 (Kapitel 2.4), Preise offen; staatliche Förderung nicht fest einplanen.

## 6 Abhängigkeiten zwischen den Ressourcen
1. Gadget → Eichrecht/CE-Prüfung (Z-1, Z-2) → Fertigung → Vorfinanzierung → Pfandmodell → Zahlungsdienstleister (Z-3).
2. MVP (Vermittlung + Abrechnung) → Zahlungsdienstleister (Rechtslage) → Pilotstart → Anbieter-Basis.
3. Förderung/Investor → Rechtsform/Gründung → Kapital für Entwicklung und Gadget.
4. Team-Zeit → Geschwindigkeit des Piloten und externer Zukauf.

## 7 Offene Entscheidungen und Aufgaben
| Nr. | Frage | Stand |
|---|---|---|
| E-1 | Lager, Versand, Rücknahme der Gadgets | entschieden: Fulfillment-Dienstleister |
| E-2 | Testausstattung für den Pilot | entschieden: Pilot-Anbieter und Leihgeräte |
| E-3 | Zeitbudget je Teammitglied | entschieden: 5 bis 10 Stunden pro Woche (A-05) |
| E-4 | Datenhaltung und Hosting (DSGVO) | entschieden: EU-Hosting |
| E-5 | Eigenmittel der Gründer | entschieden: freiwillig, unterschiedlich (Betrag A-07 offen) |
| E-6 | Reihenfolge Förderung und Investor | entschieden: Eigenmittel/Förderung, dann Investor |
| E-7 | Ziel der Anbieter-Basis zum Pilotstart | entschieden: Zielwert pro Region als Annahme (A-06 offen) |
| A-1 | Aufteilung MVP extern/White-Label und späterer Eigenbau; Plattformanbieter auswählen | offen |
| A-2 | Kompetenzzuweisung an die 6 Personen | erledigt am 2026-10-26: R1 Damian, R2 Jannik, R3 Niclas, R4 Gregor, R5 Tim, R6 Ben (`kapitel/05b-rollen-kompetenzbereiche.md`); Vertretungen und Kapitelverantwortung bestätigt |
| A-3 | Gadget: Machbarkeit, Eichrecht, Herstellkosten, Pfandhöhe, Mindestabnahme | offen, zu recherchieren |
| A-4 | Rechtliche Vorfrage Zahlung (Pfand, Auszahlung an Privatpersonen) | offen, Anwalt/Beratung |
| A-5 | Hochschule: EXIST-Träger, Ansprechpartner DHpreneur; Regeln Pre-Seed BW | offen, Anfragen der Gruppe |
| A-6 | Partnergespräche (Zahlungsdienstleister zuerst, dann Fertiger/Zertifizierer, Versicherer, Energieversorger) | offen |
| A-7 | Rechtsform | offen |
| A-8 | Beträge in die Kostenpositionen eintragen und Finanzplan rechnen | offen |
| A-9 | Genehmigungen und Zertifikate Z-1 bis Z-15 prüfen, Zuständigkeiten klären (Abschnitt 3a) | offen, Prüfung durch Jannik (Gadget), Ben (Recht), Damian (Software) |
