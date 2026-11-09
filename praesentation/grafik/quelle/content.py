"""Textinhalt, Sprechernotizen und Alt-Texte der 14 Folien. Erzeugt content.json."""
import json

SECTIONS = {1: "Einstieg", 2: "Geschäftsmodell", 3: "Geschäftsmodell", 4: "Geschäftsmodell", 5: "Geschäftsmodell", 6: "Geschäftsmodell",
            7: "Zielmarkt", 8: "Zielmarkt", 9: "Zielmarkt", 10: "SWOT", 11: "SWOT", 12: "SWOT", 13: "SWOT", 14: "Action"}

S = []
def add(n, kicker, title, sub, source, notes, alt, secs):
    S.append(dict(n=n, kicker=kicker, title=title, sub=sub, source=source, notes=notes, alt=alt, secs=secs, section=SECTIONS[n]))

add(1, "", "WallShare", "Der Marktplatz für ungenutzte Wallbox-Zeit",
    "Quellen: KBA, Pressemitteilung 09/2026 (Bestand am 1.1.2026); Fraunhofer ISI, Pressemitteilung vom 20.11.2025 (rund 80 % der E-Autos werden zu Hause geladen).",
    "[0:00 bis 0:40, Attention] Mit der Zahl einsteigen: 2.034.260 reine E-Autos (KBA, 1.1.2026). Rund jedes fünfte wird nicht zu Hause geladen (Fraunhofer ISI). Gleichzeitig stehen private Wallboxen den größten Teil des Tages still. WallShare, Arbeitsname, bringt beides zusammen. Wir starten in Mannheim–Heidelberg und im Odenwald. Hinweis: Alles in dieser Präsentation ist Entwurf; Szenarien und Bewertungen sind als Annahmen gekennzeichnet.",
    "Karte der Region Mannheim, Heidelberg und Odenwald mit leuchtenden Ladepunkten; links die Zahl 2.034.260 E-Autos und fünf Autosymbole, von denen eines hervorgehoben ist.", 0)
add(2, "I.1 GESCHÄFTSFELD · I.2 ZIELE", "Ein Marktplatz für ungenutzte Wallbox-Zeit, ohne eine einzige Ladesäule",
    "Private und gewerbliche Wallbox-Besitzer treffen E-Auto-Fahrer, Wachstum Region für Region 2027–2031",
    "Quelle: Beschlüsse der Gruppe, kapitel/00d (I.1, I.2). Phasen sind Planung, Mengenziele (Anbieter, Fahrer, Umsatz) sind noch offen.",
    "[0:40 bis 1:30, Interest] I.1 Geschäftsfeld: zweiseitiger Marktplatz für Wallbox-Kapazität, privat und gewerblich. Wir besitzen keine Ladesäulen, das hält uns kapitalarm. I.2 Ziele in drei Phasen: 2027 Pilot in zwei Regionen, 2028 bis 2029 weitere Regionen mit Break-even je Region, 2030 bis 2031 bundesweit; DACH nur als Option nach dem Pilot. Mengenziele folgen nach den Pilotdaten.",
    "Links das Dreieck Wallbox-Besitzer, WallShare und E-Auto-Fahrer, darunter die Aussage null eigene Ladesäulen; rechts eine Zeitleiste 2027, 2028 bis 2029 und 2030 bis 2031 mit wachsenden Punktnetzen.", 1)
add(3, "I.3 NUTZENVERSPRECHEN · I.4 KUNDEN", "Fahrer planen und laden nah, Anbieter lehnen sich zurück",
    "Kein Preisversprechen: „günstiger als öffentlich“ ist nicht belegt",
    "Quelle: Beschlüsse kapitel/00d (I.3, I.4). Die Segmente sind Annahmen (A-10, A-11); rund 20 % der E-Autos werden nicht zu Hause geladen (Fraunhofer ISI, 2025).",
    "[1:30 bis 2:20, Interest] I.3 Fahrer: reservieren statt suchen, und laden, wo öffentliche Säulen fehlen. Bewusst kein Preisversprechen, denn Cocharge liegt mit 0,59 € über vielen öffentlichen AC-Preisen. Anbieter: rundum sorglos mit Abrechnung, Versicherung und Support; Einnahmen nur als Möglichkeit. I.4 Kunden: Fahrer ohne Wallbox an der Wohnung, Kern sind Mieter ohne Ladeplatz; Anbieter alle Wallbox-Besitzer mit Akquise-Schwerpunkt PV.",
    "Zwei Karten: Fahrer mit den Versprechen Reservieren statt suchen und Laden wo Säulen fehlen, Anbieter mit Rundum sorglos und Einnahmen als Möglichkeit; darunter Kundensegmente F1 bis F3 und A1 bis A3.", 1)
add(4, "I.5 WERTSCHÖPFUNG · PARTNER", "Eigene Marktplatzlogik, zugekaufte Bausteine",
    "Den Kern bauen wir selbst; Zahlung, Fertigung, Versand und Hosting kommen von Partnern",
    "Quelle: kapitel/00d (I.5), kapitel/05a-ressourcen. Die genannten Partner sind Kandidaten und nicht geprüft; ein Zahlungsdienstleister ist nicht gewählt.",
    "[2:20 bis 3:00, Interest] I.5 Wertschöpfung: Der Kern, App, Radar und Reservierung, ist unsere Kernkompetenz und wird eigen gebaut. Das Gadget entsteht in Auftragsfertigung und geht über einen Fulfillment-Dienst zum Anbieter; es steht unter Vorbehalt des Gates. Zahlung, Backend-Bausteine, Versicherung und EU-Hosting kaufen wir zu. Wichtig: Die Partner sind Kandidaten, noch nichts ist entschieden.",
    "Wertschöpfungskette von Wallbox-Besitzer über Gadget und WallShare Plattform zum E-Auto-Fahrer; darunter gestrichelt die Partner Auftragsfertigung, Fulfillment, Zahlungsdienst, Backend mit EU-Hosting und Versicherer.", 1)
add(5, "I.6 PRODUKTE · DIENSTLEISTUNGEN · ERLÖSE", "Sechs Leistungen, ein Erlösmodell: Provision im Preis",
    "Pilot-Erlöse: Provision und Reservierungsgebühr, kein Abo, keine Werbung",
    "Quelle: kapitel/02, kapitel/00d (I.6); Beispielrechnung realistisches Szenario (Annahmen A-14 bis A-17), Stripe-Listenpreise, finanzen/unit-economics.md.",
    "[3:00 bis 3:45, Interest] I.6 Sechs Leistungen: Vermittlung, Abrechnung, Absicherung, Radar, das Gadget und später Energie. Erlös: Der Fahrer zahlt einen kWh-Preis, die Provision ist darin enthalten; es gibt zwei Preise, PV-Strom und Normalstrom. Beispiel im realistischen Szenario: Von 110 € im Monat gehen 93,50 € an den Anbieter, 16,50 € sind Provision, davon 6,48 € Zahlungskosten und 10,02 € Deckungsbeitrag. Dazu die Reservierungsgebühr nur bei Nichtnutzung. Abos kommen erst nach dem Pilot.",
    "Sechs Kacheln für die Leistungen Vermittlung, Abrechnung, Absicherung, Radar, Gadget und Energie; rechts ein Balken, der zeigt, wie sich 110 Euro verteilen: 93,50 Euro Anbieter, 6,48 Euro Zahlungskosten, 10,02 Euro Deckungsbeitrag.", 1)
add(6, "I.7 USP · KERNKOMPETENZ", "Gadget plus Reservierung für Fahrer ohne Wallbox",
    "Der USP steht unter Vorbehalt: Eichrecht und Machbarkeit werden vor der Fertigung geprüft",
    "Quelle: Herstellerseiten cocharge.de, airelectric.de (Abruf 09.11.2026), electrive 29.07.2026 (VoltExchange). „Nicht erwähnt“ bedeutet nicht „fehlt“.",
    "[3:45 bis 4:35, Interest] I.7 USP: die Kombination aus Gadget, das bestehende Wallboxen teilbar macht, und Reservierung für Fahrer ohne Wallbox. Wir sagen nie erste oder einzige. Der Vergleich zeigt, was auf den Anbieterseiten belegt ist: Cocharge bietet Abrechnung und Auszahlung; Reservierung, Hardware-Lösung und Versicherung sind bei keinem der drei erwähnt. Das heißt nicht, dass sie fehlen. Kernkompetenz: den zweiseitigen Marktplatz aufbauen und beide Seiten regional gleichzeitig gewinnen. Vorbehalt: Das Eichrecht ist unser Gate.",
    "Vergleichstabelle von WallShare, Cocharge, AirElectric und VoltExchange für Abrechnung, Reservierung, Gadget und Versicherung; rechts die Karte Kernkompetenz mit vier Häkchen und einem Hinweis auf das Gate Eichrecht.", 1)
add(7, "II.1 ZIELMARKT · II.2 POTENZIAL", "Fahrer ohne Heimladen: 2 bis 26 Mio. Euro Markt, begrenzt durch die Nachfrage",
    "Szenarien auf Annahmen, Deutschland pro Jahr; Plattformerlös 0,2 bis 5,2 Mio. Euro",
    "Quelle: KBA; BDEW 82 % Heimladen (Näherung 18 %; Fraunhofer ISI nennt rund 20 %); Szenarien A-08, A-12, A-14, A-18 bis A-20, finanzen/marktgroesse-szenarien.md.",
    "[4:35 bis 5:25, Desire] II.1 Zielmarkt: Fahrer ohne Heimladen. Vom E-Auto-Bestand bleiben in einer vorsichtigen Näherung rund 366.000 Fahrer ohne Heimladen. II.2 Potenzial: Je nachdem, wie viele davon Sharing nutzen, 1, 3 oder 5 Prozent, ist der Markt 2, 10,9 oder 25,9 Millionen Euro im Jahr groß; unser Erlös daraus 0,2 bis 5,2 Millionen. In allen Szenarien begrenzt die Nachfrage, nicht das Angebot. Für den Pilot rechnen wir mit 11.000 bis 289.000 Euro Umsatz. Alles sind Annahmen, die die Umfrage prüft.",
    "Trichter von 2.034.260 E-Autos über etwa 366.000 Fahrer ohne Heimladen und die nutzungsbereiten Fahrer zum Markt von 2,0 bis 25,9 Millionen Euro; rechts ein Säulendiagramm der drei Szenarien für Markt und Plattformerlös.", 2)
add(8, "II.3 MARKTENTWICKLUNG · ATTRAKTIVITÄT · RENDITE", "Der Markt wächst, die Rendite hängt an der Nutzung je Wallbox",
    "Keine belegte Branchenrendite; eigene Rechnung: Deckungsbeitrag je Anbieter und Monat",
    "Quelle: KBA 03.03.2026; Bundesnetzagentur 01.09.2026 (+15,6 %: Presse); AlixPartners über Statista (Prognose 2030); finanzen/unit-economics.md, recherche/branchenrendite.md.",
    "[5:25 bis 6:10, Desire] II.3 Entwicklung: Der E-Auto-Bestand wuchs 2025 um 23,2 Prozent, öffentliche Ladepunkte liegen bei 214.334, private Ladepunkte sollen laut Prognose bis 2030 von 2,36 auf 4,07 Millionen steigen. Rendite: Es gibt keine belegte Branchenrendite. Unsere eigene Rechnung zeigt: Der Deckungsbeitrag je Anbieter liegt zwischen 0,37 und 30,36 Euro im Monat. Unter etwa 100 kWh je Wallbox und Monat frisst die Zahlungsabwicklung die Provision. Deshalb ist die Nutzung unsere wichtigste Kennzahl.",
    "Links drei Wachstumszeilen: E-Auto-Bestand plus 23,2 Prozent, 214.334 öffentliche Ladepunkte, private Ladepunkte 2023 und Prognose 2030; rechts Deckungsbeitrag je Anbieter und Monat in drei Szenarien mit dem Anteil der Zahlungskosten an der Provision.", 2)
add(9, "II.4 BRANCHE · PORTER 5 FORCES", "Hohe Rivalität und viele Substitute, enge Nische als Ausweg",
    "Zwei Branchen getrennt betrachtet: Laden von E-Autos und Sharing-Plattformen",
    "Quelle: kapitel/03b-porter-five-forces.md. Einstufungen sind Einschätzungen der Gruppe (hoch = 4, mittel = 3, mittel bis hoch = 3,5).",
    "[6:10 bis 6:50, Desire] II.4 Branche nach Porter, in zwei getrennten Analysen. Laden von E-Autos: Rivalität, Substitute und Käufermacht sind hoch, Neue Anbieter mittel bis hoch, Lieferanten mittel. Sharing-Plattformen: Rivalität mittel, weil der Markt klein ist, aber Substitute und Käufermacht hoch; die Macht der Anbieter ist offen. Folge: Wir gehen nicht in die Breite, sondern in eine enge Nische. Die Einstufungen sind Einschätzungen.",
    "Zwei Radardiagramme nach Porter für Laden von E-Autos und für Sharing-Plattformen mit den Achsen Rivalität, Neue Anbieter, Substitute, Käufermacht und Lieferanten beziehungsweise Anbieter-Macht.", 2)
add(10, "SWOT · ÜBERBLICK", "SWOT: 7 Stärken, 9 Schwächen, 9 Chancen, 9 Risiken",
    "Intern beeinflussbar, extern nicht; gemessen an Cocharge, AirElectric und VoltExchange. Punktgröße zeigt das Gewicht",
    "Quelle: kapitel/03c-swot-analyse.md; Bewertungen sind Einschätzungen der Gruppe und werden noch geprüft.",
    "[6:50 bis 7:25, Desire] Die SWOT-Analyse in einem Blick. Oben intern: sieben Stärken, überwiegend Konzept, und neun Schwächen. Unten extern: neun Chancen und neun Risiken. Die Punktgröße zeigt das Gewicht. Größte Schwäche: keine Marke und keine Nutzerbasis. Größtes Risiko: das Eichrecht. Größte Chance: die Fahrer ohne Heimladen.",
    "Klassische Vier-Felder-Matrix: Stärken und Schwächen oben, Chancen und Risiken unten, jeweils mit den Faktoren S1 bis S7, W1 bis W9, O1 bis O9 und T1 bis T9; die Punktgröße zeigt das Gewicht.", 2)
add(11, "SWOT · INTERNE FAKTOREN", "Intern überwiegen die Schwächen: Mittelwert −0,85",
    "Die Stärken sind Konzept und Planung, die Schwächen treffen genau die Erfolgsfaktoren",
    "Quelle: kapitel/03c, Abschnitt 8. Punkte = Gewicht in % × Ausprägung (−3 bis +3), Einschätzung der Gruppe.",
    "[7:25 bis 7:55, Desire] Bewertet nach Gewicht und Ausprägung gegenüber dem Wettbewerb: Die Stärken summieren sich auf plus 38, die Schwächen auf minus 123. Der gewichtete Mittelwert ist minus 0,85. Die größte Schwäche ist die fehlende Nutzerbasis, dann Know-how, Finanzierung und die ungeprüfte Machbarkeit des Gadgets.",
    "Balkendiagramm der internen Faktoren: grüne Balken für sieben Stärken nach rechts, rote Balken für neun Schwächen nach links; rechts der gewichtete Mittelwert minus 0,85.", 2)
add(12, "SWOT · EXTERNE FAKTOREN", "Extern wiegen die Risiken schwerer: Saldo −40",
    "Größtes Risiko ist das Eichrecht (Wert 25), größte Chancen sind Nicht-Heimlader und zukaufbare Bausteine",
    "Quelle: kapitel/03c, Abschnitt 8. Wert = Wahrscheinlichkeit × Auswirkung (je 1 bis 5), Einschätzung der Gruppe.",
    "[7:55 bis 8:25, Desire] Extern: Chancenwert 101, Risikowert 141, Saldo minus 40. Das Eichrecht ist das größte Einzelrisiko mit dem Wert 25: Laut Eichamt Sachsen sind Pauschal- und Standzeitabrechnung unzulässig. Danach folgen die fehlende Marktdurchsetzung bisheriger Anbieter und Steuer- und Haftungsfragen. Dem stehen der E-Auto-Boom, die Nicht-Heimlader und zukaufbare Bausteine gegenüber.",
    "Zwei Balkenlisten: Chancen in Grün und Risiken in Rot, nach Wert sortiert; darunter ein Balken, der Chancen 101 gegen Risiken 141 zeigt, Saldo minus 40.", 2)
add(13, "TOWS · STRATEGIE", "Position WT: erst Machbarkeit klären, dann gezielt in die Nische",
    "16 Strategien aus der Verknüpfung von Stärken, Schwächen, Chancen und Risiken; die Zahl im Kreis ist der Rang",
    "Quelle: kapitel/03c, Abschnitte 8 und 9. Rang nach Prioritätswert (externe Werte × interne Gewichte), Einschätzung der Gruppe.",
    "[8:25 bis 9:05, Desire] Aus der Verknüpfung entstehen 16 Strategien in vier Quadranten. Unsere Grundposition ist WT: Schwächen und Risiken überwiegen, also Risiken minimieren. Die drei wichtigsten Strategien: WT2 Kapital schonen und Wechseloptionen offenhalten, WT1 ein Gate vor jeder Investition und ST1 Compliance als Produktmerkmal. Auch wenn alle Gates bestanden werden, bleibt die Position WT, rückt aber näher an Absicherung und Aufholen. Selektiv bleibt die Offensive SO1: reservierbares Nachtladen für Fahrer ohne Heimladen.",
    "Vier-Felder-Matrix der Strategien SO, ST, WO und WT mit je vier Strategien; die drei wichtigsten sind nummeriert. Rechts ein Koordinatenfeld, das die Grundposition im Quadranten WT zeigt, plus ein Pfeil zum Szenario bestandene Gates.", 2)
add(14, "ACTION", "Gemeinsam durch drei Gates zum Pilot 2027",
    "Wir suchen Pilot-Anbieter, Förderer und Fachwissen für Mannheim–Heidelberg und den Odenwald",
    "Quelle: kapitel/03c, Abschnitt 11. Die Gate-Kriterien sind Vorschläge; die Gruppe beschließt sie vor der Erhebung.",
    "[9:05 bis 10:00, Action] Der Weg: Drei Gates vor der Investition. Erstens das Eichamt bestätigt die kWh-Abrechnung, zweitens Recht und Zahlung sind geklärt, drittens Umfrage und Interviews zeigen Nachfrage. Dann folgt der Pilot 2027. Dafür suchen wir heute: Pilot-Anbieter, also Wallbox-Besitzer in Mannheim–Heidelberg und im Odenwald; Förderer, etwa Hochschule, Gründerzentren und Programme; und Fachwissen zu Eichrecht, Zahlungsverkehr und Recht. Sprechen Sie uns heute an.",
    "Weg über drei nummerierte Gates Eichrecht, Recht und Zahlung und Nachfrage zum leuchtenden Pilot 2027; rechts die Karte Wir suchen mit Pilot-Anbietern, Förderern und Fachwissen.", 3)

json.dump(S, open("content.json", "w"), ensure_ascii=False, indent=1)
print("content.json", len(S))
