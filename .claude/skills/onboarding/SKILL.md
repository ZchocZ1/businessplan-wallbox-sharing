---
name: onboarding
description: Kurzes Erst-Onboarding für neue Teammitglieder im Businessplan-Repo. Prüft Git-, SSH- und Signatur-Einrichtung, erklärt Projekt und Git-Regeln in wenigen Zeilen und führt einen Probe-Pull-Request durch. Läuft automatisch, wenn die Datei .git/onboarding-done fehlt (siehe CLAUDE.md), oder auf Wunsch mit /onboarding.
---

# Onboarding Businessplan-Repo

Ziel: in ca. 10 Minuten ein sicher eingerichtetes Teammitglied mit einem erfolgreichen Probe-Pull-Request. Antworte auf Deutsch, knapp, ein Schritt nach dem anderen. Warte nach jedem Schritt auf die Rückmeldung der Person.

## Sicherheitsregeln für dich (gelten immer)
- Private Schlüssel nie lesen, anzeigen oder kopieren: Dateien `~/.ssh/id_*` ohne Endung `.pub`, `.env`, Tokens. Nie bitten, so etwas in den Chat zu schreiben.
- `git config --global` nur ändern, nachdem du die Änderung genannt und die Person zugestimmt hat.
- Nie direkt auf `main` committen oder pushen, nie `--force`, nie `--no-verify`, nie Signierung abschalten.
- Nur committen oder pushen, wenn die Person es in diesem Onboarding ausdrücklich bestätigt.

## Schritt 1: Einrichtung prüfen (nur lesen)
Führe aus und werte aus:
```
git --version
git config --global user.name
git config --global user.email
git config --global gpg.format
git config --global commit.gpgsign
git config --global user.signingkey
ssh -T git@github.com
git remote -v
git branch --show-current
```
Soll-Zustand:
- `user.email` endet auf `@users.noreply.github.com` (keine private Adresse). Sonst: Noreply-Adresse unter GitHub *Settings → Emails* nachschlagen lassen.
- `gpg.format` = `ssh`, `commit.gpgsign` = `true`, `user.signingkey` zeigt auf eine vorhandene `.pub`-Datei (prüfe nur, ob sie existiert).
- `ssh -T` meldet „successfully authenticated“.
- `origin` zeigt auf das Repo `businessplan-wallbox-sharing` per SSH (`git@github.com:`), nicht per HTTPS.
Bei jeder Abweichung: Fehler in einem Satz erklären, den Befehl zur Korrektur vorschlagen, auf Zustimmung warten, ausführen, erneut prüfen. Fehlt der SSH-Key ganz, verweise auf `ONBOARDING.md` Teil A.
Erinnere zum Schluss: 2FA bei GitHub muss aktiv sein (kannst du nicht prüfen, die Person bestätigt es).

## Schritt 2: Projekt in sechs Zeilen
Erkläre, ohne die Dateien zu zitieren:
1. Projekt: Businessplan für eine App zum Wallbox-Sharing, Endprodukt ist eine Präsentation; alle Texte auf Deutsch.
2. Ordner: `kapitel/` (Entwürfe), `recherche/` (Quellen und Daten), `abgaben/`, `finanzen/`, `praesentation/`.
3. Lies `ABGABENPLAN.md` und nenne der Person ihr Kapitel und die nächste Deadline, falls eingetragen. Frage nach dem Vornamen, falls unklar.
4. Zahlen: jede Marktzahl mit Quelle (URL, Abrufdatum) in `recherche/`; eigene Schätzungen als Annahme A-nn in `ANNAHMEN-GLOSSAR.md`.
5. Die Statista-PDFs liegen nur lokal und nicht im Repo (Lizenz); Daten stehen in `recherche/statista-auswertung.md`.
6. Entscheidungen (Dienstleistung, Preis, Rechtsform) trifft die Gruppe, nicht Claude.

## Schritt 3: Git-Regeln in sieben Punkten
1. Nie direkt auf `main`. Pro Aufgabe ein Branch, z. B. `kapitel/03-markt-vorname`.
2. Vor dem Arbeiten: `git switch main && git pull`.
3. Ein Kapitel oder eine Datei gehört einer Person; Excel und PowerPoint bearbeitet immer nur eine Person gleichzeitig.
4. Kleine Commits, deutsche Nachricht im Imperativ. Commits sind signiert.
5. Änderung per Pull Request im Browser; eine andere Person gibt frei. Änderungen an `CLAUDE.md`, `.claude/` und `GIT-ZUSAMMENARBEIT.md` prüft zusätzlich ein Admin.
6. Keine Geheimnisse, keine privaten Daten, keine Klarnamen aus Interviews, keine lizenzierten PDFs ins Repo. Vor jedem Commit `git status` ansehen.
7. Ist doch ein Geheimnis committet worden: sofort melden, nicht selbst die History umbauen.

## Schritt 4: Probelauf
Mit Zustimmung der Person:
1. `git switch main && git pull`, dann `git switch -c onboarding/<vorname>` (Vorname klein, ohne Umlaute).
2. Lege `team/onboarding/<vorname>.md` an mit Vorname, Datum und dem Satz „Onboarding abgeschlossen“.
3. `git add team/onboarding/<vorname>.md`, `git status` zeigen, Commit mit Nachricht `Onboarding <Vorname>` (signiert; nach der SSH-Passphrase fragen lassen, falls nötig).
4. `git log --show-signature -1` zeigen. Meldet es „Good signature“ oder (bei fehlender allowed_signers-Datei) nur einen Hinweis darauf, ist das in Ordnung; entscheidend ist, dass der Commit einen `gpgsig`-Block hat (`git cat-file commit HEAD | head -5`).
5. Nach Bestätigung `git push -u origin onboarding/<vorname>`. Der Push auf `main` muss abgelehnt werden (nicht versuchen, nur erklären).
6. Gib den Link `https://github.com/ZchocZ1/businessplan-wallbox-sharing/pull/new/onboarding/<vorname>` aus. Die Person erstellt den Pull Request im Browser, schreibt in den Gruppenchat, dass jemand freigeben soll, und gibt selbst einen anderen Onboarding-Pull-Request frei, wenn einer offen ist.
7. Nach dem Merge: `git switch main && git pull`, Branch löschen mit `git branch -d onboarding/<vorname>`.

## Schritt 5: Abschluss
Lege die lokale Marke an (liegt in `.git`, wird nie committet): `touch .git/onboarding-done`. Sage in zwei Zeilen, wie es täglich weitergeht (Regeln 2 bis 5) und dass die ganze Anleitung in `GIT-ZUSAMMENARBEIT.md` steht.
