# Elevator Pitch (Entwurf 2)

Status: **Entwurf 2 von Ben und Claude, 2026-11-02**, noch nicht mit der Gruppe abgestimmt. Grundlage: der neueste Stand des Geschäftsmodells (`Geschäftsmodell – Wallbox-Sharing-Plattform.docx`, Jannik, 2026-11-02) plus die Beschlüsse in `kapitel/`. Aufbau nach **AIDA** (Attention, Interest, Desire, Action). Alles in `[eckigen Klammern]` ist offen oder muss die Gruppe festlegen.

## 1 Pitch-Text, 60 Sekunden (ca. 190 Wörter)

**A – Attention**
Wann haben Sie zuletzt eine Ladesäule gesucht, und sie war belegt? Über zwei Millionen E-Autos fahren in Deutschland. Viele Fahrer, vor allem Mieter ohne eigenen Stellplatz, können zu Hause nicht laden. Gleichzeitig steht in Garagen und Einfahrten eine Wallbox, die den größten Teil des Tages still steht.

**I – Interest**
**WallShare** macht diese Wallboxen buchbar. Wir sind ein Marktplatz, auf dem private und gewerbliche Besitzer ihre Wallbox an Fahrer aus der Nachbarschaft vermieten. Fahrer finden im Radar eine freie Wallbox, reservieren ein festes Zeitfenster und bezahlen in der App, auch über Nacht und ohne Blockiergebühr. Jede bestehende Wallbox machen wir mit einem kleinen Gadget fit, das der Anbieter kostenlos gegen Pfand bekommt. Abrechnung, Absicherung und Support übernehmen wir. Wir bauen dafür keine einzige Ladesäule.

**D – Desire**
Fahrer laden planbar und nah am Wohnort. Anbieter registrieren sich kostenlos und machen aus Leerlauf Zusatzeinnahmen, ohne Aufwand. Unsere Stärke ist der Aufbau eines zweiseitigen Marktplatzes: Wir gewinnen Anbieter und Fahrer in einer Region gleichzeitig. Ein dichtes regionales Netz mit eigenen Daten und Partnern lässt sich nicht einfach kopieren.

**A – Action**
Wir starten den Pilot in Mannheim–Heidelberg und im Odenwald. Dafür suchen wir Wallbox-Besitzer, die ihre Wallbox mit uns teilen. Melden Sie sich bei uns.

### 30-Sekunden-Kurzfassung
Über zwei Millionen E-Autos, aber viele Fahrer können zu Hause nicht laden, während Wallboxen den Tag über still stehen. **WallShare** macht diese Wallboxen buchbar: reservieren, laden, in der App bezahlen, ohne neue Ladesäulen. Anbieter verdienen an ihrer Wallbox, Fahrer laden planbar in der Nachbarschaft. Wir suchen Wallbox-Besitzer für unseren Pilot in Mannheim–Heidelberg. Melden Sie sich bei uns.

## 2 Was sich gegenüber Entwurf 1 geändert hat
| Änderung | Grund aus dem Geschäftsmodell-Dokument |
|---|---|
| Einstieg als Frage („Ladesäule belegt?“) | Kernnutzen ist Planbarkeit durch Reservierung |
| „Marktplatz“, „private und gewerbliche Besitzer“ | Modelltyp Marketplace mit Pay per Use; gewerbliche Anbieter von Anfang an (Beschluss 2026-10-26, A2) |
| „Ohne Blockiergebühr, auch über Nacht“ | Über-Nacht-Pauschalen als neues Merkmal für Mieter (F1) |
| „Keine einzige Ladesäule“ | Kapitalarmes Modell ohne eigene Infrastruktur |
| „Anbieter registrieren sich kostenlos“ | Freemium auf Anbieterseite |
| Kernkompetenz im Desire-Teil | Das Dokument definiert sie jetzt ausdrücklich (Abschnitt 3) |
| Versicherung nur noch als „Absicherung“ | Im Dokument ist sie nur Kostenposition, im Repo Leistung D-3 (Abschnitt 4) |
| Solarstrom **nicht** im Pitch | Im Dokument Teil der Neuheit, im Repo „erst nach dem Pilot“ (D-4); sonst verspricht der Pitch mehr als der Pilot liefert |

## 3 Kernkompetenz, Stärken, Alleinstellung
### 3.1 Kernkompetenz (laut Geschäftsmodell-Dokument)
Aufbau und Betrieb eines **zweiseitigen Lade-Marktplatzes**: die Plattform (App, Radar, Firmware) plus die Fähigkeit, Anbieter und Fahrer in einer Region gleichzeitig zu gewinnen. Geprüft nach Prahalad/Hamel:

| Merkmal | Erfüllung |
|---|---|
| Kundennutzen | Reservierbares, günstiges Laden bzw. Zusatzeinnahmen |
| Differenzierung | Reservierung ohne Blockiergebühr, Smart-Relais, (später) Solar-Tarife |
| Imitationsschutz | Netzwerkeffekt, eigene Daten, Marke, Partnernetz, Gebrauchsmuster/Design, EU-Hosting |
| Übertragbarkeit | Weitere Regionen, Flotten, Parkplätze, Energie-Sharing |

### 3.2 Worin wir gut sind (Vorschlag, von der Gruppe zu bestätigen)
Persönliche Vorkenntnisse sind im Repo weiter nicht erfasst (`kapitel/05b-rollen-kompetenzbereiche.md`). Dokumentiert sind: Studiengang Wirtschaftsingenieurwesen mit Digital Transformation, strukturierte Marktanalyse mit Quellen und Annahmenliste, Partnerstrategie (Zahlung, Versicherung, Fertigung) und Pilotnähe zu Mannheim/Heidelberg. **Lücke:** Hardware-Entwicklung, Eichrecht und Softwareentwicklung (extern bzw. White-Label). Im Pitch nicht als Stärke nennen; bei Rückfragen: „Das holen wir uns über Partner.“

### 3.3 Was uns einzigartig macht, und was nicht
| Merkmal | Befund (`recherche/wettbewerber.md`) | Im Pitch? |
|---|---|---|
| Smart-Relais/Gadget für ältere Wallboxen | Kein Wettbewerber mit Gadget gefunden; &Charge unterstützte 2021 aber schon „jede handelsübliche Wallbox“ ohne Hardware. **Eichrecht und Machbarkeit ungeprüft** | Ja, aber ohne „einzigartig“ |
| Reservierung ohne Blockiergebühr, Über-Nacht-Pauschale | Reservierung selbst nicht neu (&Charge 2021). Die Pauschale ist als Kombination neu, im Wettbewerb nicht geprüft | Ja, als Nutzen für Mieter |
| Dichtes regionales Netz (Netzwerkeffekt) | Strategie, noch kein Beleg; wirkt erst nach dem Pilot | Ja, als Schutz, nicht als Ist-Zustand |
| Solar-Tarife | Idee, im Repo erst nach dem Pilot | Nein, erst später |
| „Günstiger als öffentliche Säulen“ | **Unbelegt**, Preis und Gebühr stehen nicht fest (A-09 offen) | Nur als Annahme |

**Empfehlung:** „Erste“ oder „einzige“ Lösung nicht behaupten. Cocharge bietet Abrechnung, Auszahlung und Support schon; Sharepnp, &Charge und YouCharge.Me sind ungeklärt.

## 4 Abweichungen zwischen Geschäftsmodell-Dokument und Repo (Gruppe klärt)
| Thema | Repo (Beschluss) | Geschäftsmodell-Dokument |
|---|---|---|
| Gerät | „Gadget“, kostenlos gegen Pfand | „Smart-Relais“, Verkauf oder Vermietung, Pfand |
| Versicherung | Leistung D-3 mit Partnerversicherer | Nur Kostenposition |
| Solar/Energie | D-4 erst nach dem Pilot | Teil der Neuheit |
| Erlöse | Provision (E-1) und Reservierungsgebühr (E-5) im Pilot | Plattformgebühr, Über-Nacht-Pauschalen, Zeit-/Solar-Tarife; Reservierungsgebühr fehlt |
| Pilot | Stadt und Land parallel | F1 Mieter in der Stadt als Kern |

## 5 Belege
| Aussage im Pitch | Beleg | Stand |
|---|---|---|
| „Über zwei Millionen E-Autos“ | 2.034.260 BEV am 1.1.2026 (`kapitel/00-ueberblick-produkt-kunde-markt.md`, 3.1) | belegt |
| „Wallbox steht den größten Teil des Tages still“ | pv magazine, Juni 2026 (über 90 %); Geschäftsmodell-Dokument sagt dasselbe ohne Quelle | **eine Quelle**, im Pitch ohne Prozentzahl |
| „Vor allem Mieter können zu Hause nicht laden“ | Zielgruppenbeschluss (`01a-kunden.md`); BDEW: rund 82 % laden zu Hause | Zielgruppe ist Annahme, BDEW belegt |
| Radar, Reservierung, Abrechnung, Support | D-1, D-2, D-6 beschlossen | Partner, Machbarkeit offen |

## 6 Entscheidungen (Ben, 2026-11-02) und offene Punkte
Von Ben für diesen Entwurf entschieden, **noch nicht von der Gruppe bestätigt**:
1. **Aufruf:** Pilot-Anbieter suchen.
2. **Gerät:** „Gadget“, kostenlos gegen Pfand (Repo-Stand). Der Begriff „Smart-Relais“ und Verkauf/Vermietung aus dem Dokument sind nicht übernommen; Abweichung bleibt in Abschnitt 4 für die Gruppe offen.
3. **Preis:** „günstiger als öffentlich“ steht nicht im Pitch, bis Preis und Gebühr feststehen.
4. **Länge und Publikum:** 60 Sekunden, Dozenten/Kurs.

5. **Land-Pilotregion:** Odenwald, laut Ben von der Gruppe bestätigt (2026-11-02). Im Repo (`kapitel/01a-kunden.md`) steht noch „Odenwald oder Kraichgau, offen“; dort nachtragen, am besten mit der Begründung (Kontakte, Anbieterdichte).
6. **App-Name:** Ben wollte Vorschläge von Claude, siehe Abschnitt 7. Ben hat **WallShare** (N-2) vorläufig gewählt; der Pitch trägt den Namen als Arbeitsname. Websuche am 2026-11-02 (2 Suchen) fand **keine** Treffer zu „WallShare“ als Produkt oder Marke; das ist **keine Markenrecherche** (DPMAregister, EUIPO, WIPO und Domains wallshare.de/.com nicht abgefragt). Gruppenentscheid und Prüfung von Marke, Domain und Namensgleichheit durch R4 Gregor stehen aus.

## 7 Namensvorschläge (alle ungeprüft)
Weder Markenrecht (DPMA) noch Domain noch Namensgleichheit mit bestehenden Apps sind geprüft. Kriterien: leicht sprechbar im Pitch, Deutsch oder neutral, später DACH-tauglich, zeigt „teilen“ oder „Nachbarschaft“.

| Nr. | Name | Idee | Hinweis |
|---|---|---|---|
| N-1 | **Ladenachbar** | Laden bei den Nachbarn | Sehr klar für Fahrer, nur Deutsch (DACH ok, international schwach) |
| N-2 | **WallShare** | Wallbox plus Teilen | Selbsterklärend. Websuche 2026-11-02 ohne Treffer (kein Clearing); Anklang an „Wallbox“ (Hersteller Wallbox Chargers, Begriff auch beschreibend) prüfen |
| N-3 | **Steckplatz** | Steckdose plus Parkplatz | Kurz und merkbar, weniger klar ohne Erklärung |
| N-4 | **Stromnachbar** | Strom von nebenan | Passt zur späteren Solar-Idee; ähnelt Energieversorgern |
| N-5 | **Wallnachbar** | Wallbox plus Nachbar | Nennt Produkt und Idee, etwas sperrig |
| N-6 | **Lade-Dock** | Ort, an dem man „andockt“ | Kurz, wenig Bezug zum Teilen |
| N-7 | **Nebenan Laden** | Nähe als Kernnutzen | Beschreibend, als Marke schwer schützbar |

Empfehlung: **N-1 Ladenachbar** (klarstes Bild für Fahrer und Anbieter) und **N-3 Steckplatz** (kürzer, besser als Marke) in die engere Wahl nehmen. Beschreibende Namen (N-7) sind schwer als Marke schützbar. Prüfschritte für R4: DPMA-Register, Domain, App-Stores, Google-Suche.
