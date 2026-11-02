# Recherche: Zahlungsdienstleister für Abrechnung und Auszahlung (D-2)

Stand der Recherche: 2026-10-26. Zu Position „Zahlungsdienstleister“ in `finanzen/kapitalbedarf-kostenpositionen.xlsx`. Alle Angaben sind Listenpreise von den Seiten der Anbieter, abgerufen am 2026-10-26. **Keine Anbieterentscheidung.** Preise gelten für Standardfälle, nicht für ein Plattformmodell mit Auszahlung an Wallbox-Anbieter, außer wo ausdrücklich genannt.

Unser Modell (Beschlusslage): Fahrer zahlt über die App; Wallbox-Anbieter erhalten ihren Anteil ausgezahlt; wir behalten eine Provision; Reservierungsgebühr und Pfand werden eingezogen. Das ist ein **Marktplatz mit Mehrparteien-Zahlungsfluss**.

## A Belegt (Preis- oder Dokumentationsseite abgerufen)
| Anbieter | Zahlungsannahme | Plattform/Marktplatz (Auszahlung an Dritte) | Quelle |
|---|---|---|---|
| **Stripe** | Karten EWR Standard 1,5 % + 0,25 €; Premium 2,8 % + 0,25 €; UK 2,5 % + 0,25 €; Ausland 3,15 % + 0,25 € (+ 2 % bei Währungsumrechnung); SEPA-Lastschrift 0,35 €. | **Connect, Modell „Sie übernehmen die Preisgestaltung“:** 2 € je monatlich aktivem Konto (Konto aktiv, wenn im Monat ausgezahlt wird); 0,25 % + 0,10 € je Auszahlung; Verbundenes Konto trägt bei Direktzahlungen die Kosten für Gebühren, Erstattungen und Rückbuchungen, Stripe übernimmt dort die Verlusthaftung. Zusätzlich beim Modell mit eigener Preisgestaltung 0,25 % Startgebühr (Seite https://stripe.com/de/pricing). Alternativ Modell „Stripe übernimmt die Preisgestaltung“ (Konditionen nicht genannt). | https://stripe.com/de/pricing ; https://stripe.com/de/connect/pricing (kein Aktualisierungsdatum, © 2026) |
| **Mollie** | Karten EWR-Verbraucher 1,80 % + 0,25 €; Firmenkarten EWR 2,90 % + 0,25 €; Karten außerhalb EWR 3,25 % + 0,25 €; American Express 2,90 % + 0,25 €; SEPA-Lastschrift 0,35 €; PayPal: PayPal-Gebühren + 0,10 €. Pay as you go 0 €/Monat, Pro 20 €/Monat. Auszahlung: bis 5 je Monat kostenlos, jede weitere 0,25 € (unter 500.000 € Jahresvolumen), in Fremdwährung 1 %. | **Mollie Connect:** Zwei Modelle (Platforms, Marketplaces). Marketplaces: Plattform ist Zahlungsinhaber und trägt die erste Haftung bei Rückbuchungen, verdient durch einbehaltene Provision, Weiterleitung an mehrere Verkäufer, verzögerte Weiterleitung bis 90 Tage. Laut Dokumentation übernimmt Mollie Lizenzierung, Compliance, Identitätsprüfung (KYB) und Risikomanagement; „eine eigene Zahlungsinstitutslizenz ist laut Dokumentation nicht erforderlich“. **Gebührenhöhe für Connect: nicht genannt**, Kontakt zum Partner Manager. | https://www.mollie.com/de/pricing (Seitenstand 26.10.2026) ; https://docs.mollie.com/connect/overview |
| **Adyen** | Bearbeitungsgebühr 0,11 € je Transaktion plus Zahlungsmittelgebühr: SEPA-Lastschrift 0,27 € pauschal, iDEAL 0,22 €, Alipay 3 %; Karten Interchange++ (Interchange + Systemgebühr + 0,60 % Adyen-Gebühr). Keine Einrichtungs- oder Monatsgebühr; in manchen Branchen Mindestabrechnungsbetrag. | Marktplatz-Konditionen auf der Seite **nicht genannt** (eigenes Produkt Adyen for Platforms, Preise nicht abgerufen). | https://www.adyen.com/de_DE/preise (kein Datum sichtbar) |
| **PayPal** | PayPal Checkout 2,99 % + 0,39 € (inländisch, geschäftlich); QR-Code 0,90 %; Waren/Dienstleistungen senden/empfangen 2,49 % + Festgebühr. | Sammelzahlungen (Massenauszahlungen): Inland 2 % des Betrags, Obergrenze 12 € je Zahlung (international 70 €). PayPal Commerce Platform (Plattformpreise): auf der Seite **nicht** enthalten (Text abgeschnitten). | https://www.paypal.com/de/business/paypal-business-fees (zuletzt aktualisiert 07.09.2026) |
| **Mangopay** | Keine öffentlichen Preise; individuelles Angebot (Staffel nach Volumen, Payout nach Länderzonen, keine Beträge). | Spezialisiert auf Marktplätze; E-Wallets, virtuelle IBANs, Split-Payments, Identitätsprüfung. Mangopay ist laut eigener Angabe „licensed Electronic Money Institution (EMI)“. | https://mangopay.com/pricing (Pressemitteilung 28.04.2026 verlinkt, © 2026) |

## B Nicht belegt oder nicht verglichen
| Punkt | Stand |
|---|---|
| Aufschlüsselung von Transaktionskosten für unseren Fall (z. B. 10-€-Ladevorgang) | Nicht berechnet. Dafür fehlen Annahmen (Zahlart-Mix, Betrag je Ladevorgang, Zahl der Anbieter, Auszahlungsrhythmus). Als Annahmen A-nn nötig. |
| Gebührenhöhe Mollie Connect, Adyen for Platforms, PayPal Commerce Platform | Nicht öffentlich oder nicht abgerufen; Angebote nötig. |
| Rechtliche Einordnung (ZAG, Zahlungserlaubnis, Agentenmodell, Treuhand/Pfand) | **Nicht geprüft.** Die Aussage „keine eigene Lizenz nötig“ stammt allein aus der Mollie-Dokumentation (Herstellerangabe). Ob unser Modell (Auszahlung an Privatpersonen, Einbehalt von Pfand und Reservierungsgebühren) damit zulässig ist, muss rechtlich geklärt werden (BaFin/Anwalt). |
| Weitere Anbieter (z. B. Klarna, Adyen-Alternativen, Banken-Lösungen, Ladeabrechnungsanbieter) | Nicht recherchiert. |
| Verarbeitung von Pfand und Reservierungsgebühren bei Nichtnutzung (automatische Abbuchung) | Bei keinem Anbieter geprüft; Nutzungsbedingungen, Kartenregeln und Verbraucherrecht offen. |

## C Beobachtungen für die Entscheidung (keine Empfehlung der Gruppe vorweggenommen)
- Preise für die reine Zahlungsannahme liegen in der gleichen Größenordnung (Karten EWR ca. 1,5 % bis 1,8 % + 0,25 € bei Stripe und Mollie; Adyen mit Interchange++ und anderem Modell). **Entscheidend ist das Plattformmodell:** Nur Stripe nennt öffentlich Connect-Gebühren (2 € je aktivem Konto und Monat, 0,25 % + 0,10 € je Auszahlung). Bei Mollie, Adyen, PayPal und Mangopay sind sie nur per Angebot zu erfahren.
- Fixkosten je aktivem Wallbox-Anbieter (z. B. Stripe 2 € je Monat) wirken sich auf die Provision aus. Ob die Unit Economics tragen, ist im Finanzplan zu rechnen, mit Annahmen für Beträge je Ladevorgang.
- **Entscheidung der Gruppe (2026-10-26):** Das Gadget-Pfand wird **über den Zahlungsdienstleister** abgewickelt (nicht über ein eigenes Firmenkonto). Rechtliche Machbarkeit beim gewählten Anbieter ist noch zu prüfen.

## D Nächste Schritte
1. Rechtliche Vorfrage klären: Ist ein Mehrparteien-Zahlungsfluss mit Auszahlung an Privatpersonen über den Dienstleister ohne eigene Erlaubnis möglich, und wie wird das Pfand behandelt (Anwalt oder Datenschutz-/Zahlungs-Beratung der Hochschule, nicht von mir zu klären).
2. Angebote bei 2 bis 3 Anbietern einholen (Mollie Connect Marketplaces, Stripe Connect, Mangopay).
3. Annahmen für den Transaktionsmix festlegen (A-nn), dann Zahlungskosten je Ladevorgang im Finanzplan rechnen.
