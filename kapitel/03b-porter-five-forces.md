# Branchenanalyse nach Porter (5 Forces), zwei Analysen

Stand: 2026-11-09. Umsetzung des Beschlusses II.4 (`kapitel/00d-geschaeftsmodell-zielmarkt-beschluesse.md`): zwei getrennte Analysen. **Spalte „Beleg“ nennt nur Aussagen mit Quelle; die Spalte „Einstufung“ ist die Einschätzung von Claude und der Gruppe und kein Befund.** Wo kein Beleg vorliegt, steht „nicht belegt“. Quellen: `recherche/wettbewerber.md`, `recherche/branchenrendite.md`, `recherche/zahlungsdienstleister.md`, `kapitel/03a-markt-entscheidungen.md`, `recherche/teilungs-und-zahlungsbereitschaft.md`.

## A Branche „Laden von E-Autos“ (Mitbewerber: Säulenbetreiber, Stadtwerke, P2P-Apps)

| Kraft | Beleg | Einstufung | Folge für uns |
|---|---|---|---|
| **Rivalität unter Bestandsanbietern** | 214.334 öffentliche Ladepunkte am 1.9.2026 (157.762 normal, 56.572 schnell; Bundesnetzagentur, Primärquelle); Vorjahreswachstum +15,6 % nur aus der Presse (electrive). Durchschnittliche Auslastung öffentlicher Ladepunkte „rund 12 %“ steht auf der BDEW-Seite **ohne Quelle, Methode und Zeitraum**; Konsolidierung erwartet (Fachpresse, Quelle ungenannt; `branchenrendite.md` R-01, R-02). P2P: Cocharge (0,59 €/kWh brutto, 75 € Anschlussgebühr) und AirElectric (kostenlos, ohne Werbung, **Destination Charger für Hotels, Ferienhäuser und private Anbieter, also auch unser Segment A2**) auf den Herstellerseiten belegt (Abruf 2026-11-09). &Charge (Stand 2021), Sharepnp, YouCharge.Me unklar; ChargeAtFriends angeblich eingestellt (eine Quelle, ungeprüft). | **hoch** bei öffentlichem Laden (Preisdruck, viel Kapazität), **mittel** bei P2P-Apps | Preisvorteil nicht versprechen (A-09); Abgrenzung nur über Gadget und Reservierung für Fahrer ohne Wallbox |
| **Bedrohung durch neue Anbieter** | Technik ist zukaufbar: AirElectric bietet API und White-Label; Cocharge übernimmt Abrechnung, Auszahlung, Support und die Anmeldung bei der Bundesnetzagentur. B2B-Backends wie Monta und chargecloud sind Kandidaten (`00c`), nicht geprüft. Hürden: eichrechtskonforme Abrechnung (Cocharge verlangt sie), Anbieter- und Fahrerakquise. | **mittel bis hoch** | Kein technischer Schutz; Schutz nur über Netzdichte, Marke, Gadget (Schutzrechte noch zu prüfen) |
| **Bedrohung durch Substitute** | Rund 80 % der Elektroautos werden zu Hause geladen, vor allem in Einfamilienhäusern (Fraunhofer ISI, Pressemitteilung 20.11.2025, Primärquelle); die BDEW-Angabe 82 % hat keine Quelle. Alternativen: eigene Wallbox, Laden beim Arbeitgeber oder am Supermarkt, öffentliche Säulen (`03a`). Für Mieter sind laut Fraunhofer ISI öffentliches Laden und Quartierslösungen „eher unattraktiv“; attraktiv ist geteiltes Laden **mit Personen im gleichen Wohnhaus** mit Kostenvorteil (F-05, hypothetisch). Das sagt nichts über Teilen mit fremden Nachbarn. | **hoch** | Die Fahrer ohne Heimladen (rund 20 %) nutzen teils Arbeitgeber, öffentliche Säulen und Schnelllader; wie viele davon Sharing wollen, ist ungeprüft (`recherche/zielgruppen-pruefung.md`) |
| **Verhandlungsmacht der Käufer** | Fahrer: Wechsel kostet nichts; AirElectric zeigt Ladetarife und Karten zum Vergleich (Preistransparenz). Anbieter: kann bei AirElectric kostenlos listen, bei Cocharge 75 € einmalig; Multi-Homing möglich. Zahlungsbereitschaft Fahrer: 6,84 € je 100 km für Laden insgesamt (F-03), keine Zahl für Sharing. | **hoch** (beide Seiten) | Provision und Reservierungsgebühr dürfen die Wechselhürde nicht erhöhen; Anbieter brauchen Mehrwert (Versicherung, Abrechnung) |
| **Verhandlungsmacht der Lieferanten** | Zahlungsdienstleister: Karten bei Stripe 1,5 % + 0,25 €, bei Mollie 1,80 % + 0,25 €, Connect-Gebühren nur bei Stripe öffentlich; Marktplatz-Konditionen bei anderen nur per Angebot. Gadget: Fertiger, Mindestabnahme und Kosten offen (A-02). Wallbox-Hersteller (ABL, KEBA, go-e) als Partner genannt, nicht geprüft. Strom bringt der Anbieter mit. | **mittel** (Zahlung austauschbar, Gadget-Fertigung offen) | Zwei bis drei Zahlungsangebote einholen; Gadget-Fertiger vergleichen, Abhängigkeit vermeiden |

**Fazit A (Einschätzung):** Die Branche ist wettbewerbsintensiv und margenschwach (niedrige Auslastung, Konsolidierung). Chancen hat nur ein klar abgegrenztes Segment mit geringem Kapitalbedarf. Das deckt sich mit der Unit-Economics-Rechnung (`finanzen/unit-economics.md`): kleine Margen je Anbieter.

## B Branche „Sharing-Economy-Plattformen“ (Vergleich: Airbnb, Parkplatz-Sharing)

Hier fehlen für Wallbox-Sharing fast alle belegten Zahlen. Die Analyse stützt sich auf die Plattformlogik und die wenigen Quellen zu Wallbox-Sharing.

| Kraft | Beleg | Einstufung | Folge für uns |
|---|---|---|---|
| **Rivalität** | Wallbox-Sharing ist laut Fachartikel (pv magazine, 19.06.2026) und Ratgebern bisher **kein Massenmarkt**; der Artikel nennt die Wirtschaftlichkeit eine „offene Frage“ (R-03). Einzelne Anbieter sind eingestellt oder unklar. Take Rate Airbnb rund 13 % (Sekundärquelle, R-05). | **mittel** (wenige, kleine Wettbewerber, aber kaum Teilnehmer) | Wettbewerb um knappe Teilnehmer in jeder Region |
| **Neue Anbieter** | Netzwerkeffekt wirkt als Schutz, ist aber erst mit Netzdichte vorhanden („Strategie, noch kein Beleg“, `00b`). White-Label-Software senkt die Eintrittskosten (siehe A). | **mittel** | Region für Region Dichte aufbauen; frühe Partner (Hausverwaltungen, Installateure) |
| **Substitute** | Vermietung der Wallbox an einzelne Nachbarn ohne Plattform; Quartierslösungen und Hausverwaltungen mit eigenen Ladepunkten; Laden öffentlich. Belegt nur indirekt (Fraunhofer ISI F-05). | **hoch** | Nutzen von Versicherung, Abrechnung und Reservierung gegenüber „privat unter Nachbarn“ betonen |
| **Verhandlungsmacht der Käufer (Fahrer)** | Siehe A; zusätzlich Vertrauen: Die Bereitschaft, private Infrastruktur mit Unbekannten zu teilen, sei „begrenzt“ (T-02, nur qualitativ). | **hoch** | Bewertungen, Pfand und klare Preise (`00c` Megatrend Distrust Society) |
| **Verhandlungsmacht der Anbieter (Teilnehmer der Angebotsseite)** | Rechnerisch übersteigt die Kapazität teilungsbereiter Wallboxen die Nachfrage bundesweit deutlich (`finanzen/marktgroesse-szenarien.md`, Faktor 19 bis 183, Annahmen). Die Teilungsbereitschaft selbst ist nicht belegt (A-08), Haftung und Steuer gelten als Hürde. | **offen** (angebotsseitig knapp wegen Bereitschaft, rechnerisch reichlich) | Anbieterakquise nicht unterschätzen; Interviews mit Wallbox-Besitzern (Niclas) klären das |

**Fazit B (Einschätzung):** Die Plattformlogik schützt nur mit Netzdichte, die im Pilot noch fehlt. Der größte Unsicherheitsfaktor ist die Teilungsbereitschaft (A-08), für die keine Studie gefunden wurde.

## Quellenprüfung (2026-11-09)
Die Belege dieser Datei wurden gegen Primärquellen geprüft: `recherche/zielgruppen-pruefung.md`. Kernergebnis: KBA- und Bundesnetzagentur-Zahlen sind primär bestätigt, die Zielgruppe „Mieter in der Stadt“ ist **nicht** belegt, und die BDEW-Zahlen (82 %, 12 %) haben auf der BDEW-Seite keine Quelle.

## C Offen
1. Einstufungen sind Einschätzungen; die Gruppe bestätigt oder ändert sie.
2. Nicht geprüft: Marktanteile der Wettbewerber, Preise öffentlicher Säulen (Preisvergleich fehlt), Status von &Charge, Sharepnp, YouCharge.Me, regulatorische Eintrittsbarrieren (Eichrecht, Zahlungsdienste).
3. Stadtwerke und Energieversorger als Rivalen oder Partner: keine belegten Angaben.
4. Branche B: Primärquellen zu Plattformen (Geschäftsberichte) fehlen.
