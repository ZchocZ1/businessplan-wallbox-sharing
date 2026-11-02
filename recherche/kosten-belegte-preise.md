# Recherche: belegbare Preise für Kostenpositionen

Stand der Recherche: 2026-10-26. Zu `finanzen/kapitalbedarf-kostenpositionen.xlsx`. Nur Preise, die auf der Seite der verlangenden Stelle direkt abgerufen wurden, stehen in Tabelle A. Alle Beträge sind Listenpreise, keine Angebote für unser Vorhaben. Es ist **noch nichts in die Excel-Tabelle eingetragen**, weil Menge, Klassen und Anbieter von Entscheidungen der Gruppe abhängen.

## A Belegt (Primärquelle direkt abgerufen)
| ID | Position in der Tabelle | Preis | Quelle (Abruf 2026-10-26) | Hinweise |
|---|---|---|---|---|
| K-01 | Marke und Domain | Deutsche Marke (DPMA), Anmeldegebühr einschließlich bis zu drei Klassen: **300 €** (Papier), **290 €** (elektronisch). Ab der vierten Klasse je **100 €**. Verlängerung nach 10 Jahren (bis drei Klassen) **750 €**, ab der vierten Klasse je 260 €. | https://www.dpma.de/service/gebuehren/marken/index.html (Seitenstand 29.09.2026) | Domain-Preise nicht erhoben. Gewählte Klassen (Waren/Dienstleistungen) noch nicht festgelegt. Nur Amtsgebühren, ohne Anwalt. |
| K-02 | Recht/Verwaltung: Rechtsform und Gründung | **Handelsregister, Ersteintragung GmbH/UG: 225,00 €** (Nr. 2100); mit Sacheinlage **360,00 €** (Nr. 2101). | HRegGebV, Anlage zu § 1: https://www.gesetze-im-internet.de/hreggebv/anlage.html | Nur die Registergebühr, ohne Notar. Fassungsstand der Seite nicht erkennbar (Fundstelle BGBl. I 2010, 1732; Fußnoten fehlen im abgerufenen Text), Beträge daher vor Verwendung gegen die aktuelle Fassung prüfen. Rechtsform nicht entschieden. |
| K-03 | Software/App: App-Store-Konten | **Apple Developer Program: 99 USD je Mitgliedsjahr** (Preis in Landeswährung bei der Anmeldung; Gebührenerlass nur für Non-Profit, Bildungseinrichtungen, Behörden). | https://developer.apple.com/programs/enroll/ | Euro-Betrag nicht belegt (Wechselkurs/Landespreis erst bei der Anmeldung sichtbar). |
| K-04 | Software/App: App-Store-Konten | **Google Play Console: einmalig 25 USD** Registrierungsgebühr. | https://support.google.com/googleplay/android-developer/answer/6112435 | Euro-Betrag nicht belegt. |
| K-05 | Zahlung: Zahlungsdienstleister | **Beispiel Stripe (Deutschland):** Standardkarten aus dem EWR **1,5 % + 0,25 €**, Premiumkarten EWR 2,8 % + 0,25 €, Karten aus dem Vereinigten Königreich 2,5 % + 0,25 €, ausländische Karten 3,15 % + 0,25 € (+ 2 % bei Währungsumrechnung). **SEPA-Lastschrift 0,35 €.** Standardauszahlungen kostenlos, Sofortauszahlung 1 % (mind. 0,50 €). Stripe Connect (Plattformen) ist im Standardtarif inbegriffen; für Plattformen mit eigener Zahlungspreisgestaltung 0,25 % Startgebühr. Kontogebühren und Auszahlungsgebühren für Connect nennt die Seite nicht. | https://stripe.com/de/pricing | **Nur ein Beispielanbieter, keine Anbieterentscheidung.** Standardpreise; ob für ein Plattform-/Marktplatzmodell mit Auszahlungen an Wallbox-Anbieter Sonderkonditionen oder zusätzliche Gebühren gelten, nicht geklärt. Ob ein Dienstleister Reservierungsgebühren und Pfand verarbeiten darf, nicht geprüft. Vergleich weiterer Anbieter steht aus (Mollie, Adyen, PayPal u. a., nicht recherchiert). |

## B Nur aus Ratgebern oder Suchzusammenfassungen (nicht verwenden, bis Primärquelle gelesen)
| ID | Position | Angabe laut Quelle | Problem |
|---|---|---|---|
| K-B1 | EU-Marke (EUIPO) | 850 € für die erste Klasse, 50 € zweite Klasse, 150 € je weitere (elektronisch). Ein Drittanbieter nennt 1.000 € bei Papier. | EUIPO-Seiten nicht abrufbar (403/404). Nur Anwaltsseiten und eine portugiesische Behörde. |
| K-B2 | Notar bei UG/GmbH-Gründung | Musterprotokoll rund 176 € bis 300 €, individuelle Satzung rund 500 € bis 816 €; Gründungskosten gesamt 300 € bis 1.200 €. | Quellen widersprechen sich (z. B. Handelsregister 150 € gegenüber 300 €; die Verordnung nennt 225 €, siehe K-02). Notarkosten hängen von Gesellschaftszahl, Kapital und Satzung ab; Anfrage beim Notar nötig. Musterprotokoll nur bei höchstens drei Gesellschaftern und einem Geschäftsführer zulässig (Ratgeberaussage, nicht geprüft; die Gruppe hat 6). |
| K-B3 | Steuerberatung | 1.000 € bis 1.200 € je Jahr für Buchführung bei einer UG. | Ratgeberwert, keine Preisliste. Steuerberatervergütung folgt einer Gebührenverordnung; nicht geprüft. |
| K-B4 | Gewerbeanmeldung | rund 35 € | Ratgeberwert, kommunal unterschiedlich. |

## C Nicht recherchiert oder nicht belegbar
Diese Positionen brauchen Angebote oder eigene Annahmen mit ID (A-nn): App-MVP, White-Label-Lizenz, Hosting, Gadget-Entwicklung, Prototypen, Zertifizierung (Eichrecht, CE), Fertigung und Mindestabnahme, Vorfinanzierung, Lager/Versand, Patentanwalt, Verträge/AGB/DSGVO, Versicherungen, Marketing, Support, Berater, Reserve. Ein belegter Listenpreis existiert für diese Posten nicht oder ist vom Umfang abhängig. Anfragen und Angebote kann nur die Gruppe einholen.

## D Hinweise zur Übernahme in die Excel-Tabelle
- Beträge nur eintragen, wenn Umfang entschieden ist (Zahl der Markenklassen, Rechtsform, Stückzahl).
- USD-Beträge nicht ohne belegten Wechselkurs in Euro umrechnen.
- Amtsgebühren (DPMA, Handelsregister) sind Mindestbeträge; Notar und Anwalt kommen hinzu.
