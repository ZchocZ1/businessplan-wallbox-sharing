# Businessplan – Uniprojekt

## Kontext
- Modul „Businessplan“; Gruppe von 6 Personen entwickelt einen vollständigen Businessplan zu einem selbst gewählten Produkt.
- **Endprodukt:** vollständige Präsentation zum Plan (PowerPoint, `.pptx`, Deutsch) in `praesentation/`.
- **Zwischenprodukte:** Abgaben zum Businessplan (Formate und Termine noch unklar, siehe `ABGABENPLAN.md`).
- Zusammenarbeit der Gruppe über ein **privates GitHub-Repository** (Regeln: `GIT-ZUSAMMENARBEIT.md`, Einstieg: `ONBOARDING.md`). Dateinamen eindeutig und ohne Sonderzeichen halten.
- Sprache aller Texte, Dateien und Folien: **Deutsch**.

## Produkt
- Digitales Produkt: **App für Wallbox-Sharing** (Privatpersonen teilen ihre Wallbox mit E-Auto-Fahrern).
- Zum digitalen Produkt gehört eine **Dienstleistung**, die noch nicht definiert ist. Sie muss im Projekt erarbeitet werden (offene Frage, nicht erfinden, sondern Optionen vorschlagen und mit der Gruppe entscheiden).
- Markt: Einstieg Deutschland, später DACH. Kunden: B2C. Anbieter: private Wallboxen und gewerbliche Ladepunkte (Kleingewerbe, Firmen) von Anfang an (Beschluss 2026-10-26). Für gewerbliche Ladepunkte liegt noch keine belegte Marktzahl vor; keine Annahme setzen, bis eine Quelle gefunden ist.

## Gliederung des Businessplans
1. Executive Summary
2. Produkt und Dienstleistung
3. Markt und Wettbewerb
4. Marketing und Vertrieb
5. Organisation und Team
6. Rechtsform und rechtliche Rahmenbedingungen
7. Finanzplan
8. Risiken
9. Meilensteine

Kapitel liegen als eigene Dateien in `kapitel/` (z. B. `02-produkt-dienstleistung.md`).

## Rolle von Claude
Schreibassistent und Rechercheur. Claude recherchiert, entwirft Kapitel, rechnet den Finanzplan und überarbeitet Texte; die Gruppe entscheidet und prüft.
- Entscheidungen der Gruppe (Dienstleistung, Preismodell, Rechtsform usw.) nicht eigenmächtig treffen, sondern Optionen mit Empfehlung vorlegen.
- Konsistenz zwischen Kapiteln, Finanzplan und Präsentation prüfen (gleiche Zahlen, gleiche Begriffe).

## Regeln für Zahlen und Quellen
- Jede Marktzahl mit **Quelle** (URL und Abrufdatum) in `recherche/` belegen.
- Eigene Schätzungen sind **Annahmen** und stehen mit ID (A-nn) in `ANNAHMEN-GLOSSAR.md`; im Text klar als Annahme kennzeichnen.
- Nichts erfinden. Ist keine Quelle auffindbar, das offen sagen.
- Finanzmodell in `finanzen/` (Excel), alle Eingaben aus der Annahmenliste.

## Dateien
| Datei/Ordner | Zweck |
|---|---|
| `ABGABENPLAN.md` | Abgaben, Kapitel, Verantwortliche, Status, Deadlines |
| `ANNAHMEN-GLOSSAR.md` | Begriffe und alle Markt-/Finanzannahmen |
| `abgaben/` | Fertige Abgaben im Abgabeformat |
| `kapitel/` | Arbeitsentwürfe der Kapitel |
| `recherche/` | Quellen, Marktdaten, Wettbewerbsanalysen |
| `recherche/statista-auswertung.md` | Vollständige Daten der 6 Statista-PDFs (S-1 bis S-6). Die PDFs in `recherche/statista/` liegen nur lokal (Lizenz, nicht in Git); Daten immer aus dieser Datei zitieren |
| `finanzen/` | Finanzplan und Berechnungen |
| `praesentation/` | Endpräsentation (.pptx) |
| `GIT-ZUSAMMENARBEIT.md` | Git-Regeln, Sicherheitsvorgaben, Einrichtung |
| `ONBOARDING.md` | Einstieg für neue Teammitglieder |
| `team/onboarding/` | Probe-Pull-Requests aus dem Onboarding |

## Handoff-System
Aktiv (`.claude/`: `statusline.sh`, `jq`, Hooks `load-handoffs.sh` und `handoff-threshold-notify.sh`, Skill `handoff`). Handoffs liegen in `.claude/handoff_temp/`.

## Git-Zusammenarbeit und Onboarding
- **Onboarding zuerst:** Fehlt in diesem Ordner die Datei `.git/onboarding-done`, führe zu Beginn der Sitzung den Skill `onboarding` aus (`.claude/skills/onboarding/SKILL.md`), bevor du andere Aufgaben übernimmst.
- Nie direkt auf `main`. Arbeit auf Branch, Übergabe per Pull Request im Browser mit Freigabe einer anderen Person. GitHub erzwingt das im Free-Plan nicht; es ist verbindliche Gruppenregel.
- Nur committen oder pushen, wenn die Person es ausdrücklich verlangt. Nie `--force`, nie `--no-verify`, Commit-Signierung nie abschalten.
- Nie private Schlüssel (`~/.ssh/id_*` ohne `.pub`), Tokens oder `.env` lesen, ausgeben oder committen. Vor jedem Commit `git status` prüfen; keine lizenzierten PDFs (`recherche/statista/`), keine personenbezogenen Interviewdaten.
- Änderungen an `CLAUDE.md`, `.claude/` und `GIT-ZUSAMMENARBEIT.md` brauchen zusätzlich die Freigabe von Ben oder Jannik, weil sie das Verhalten von Claude bei allen steuern.
