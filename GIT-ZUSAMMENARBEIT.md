# Git-Zusammenarbeit: Regeln und Einrichtung

Status: Entwurf, von der Gruppe zu bestätigen. Stand 2026-11-02: Das Repo läuft im **GitHub-Free-Plan** (persönliches Konto, privat). Dort gibt es **keinen technischen Schutz von `main`** und **keine Rollen** außer Owner und Collaborator mit Schreibrecht. Die Schutzregeln unten gelten deshalb als **Gruppenregeln**, bis der Schutz technisch möglich ist (siehe Abschnitt 7).

## 1. Entscheidungen der Gruppe (vor dem Start)

| Nr. | Frage | Empfehlung |
|---|---|---|
| G-1 | Hosting | **Beschlossen: GitHub, privates Repository** unter dem Konto von Ben, 5 Eingeladene mit Schreibrecht. Alternativen für später: GitHub Pro über das Student Developer Pack, GitLab.com Free, GitLab der Hochschule. |
| G-2 | Wer ist Admin? | Im Free-Plan nur der Owner (Ben). Jannik ist fachlich Vertretung, hat technisch aber nur Schreibrecht. Absicherung: alle haben einen vollständigen Klon als Backup. |
| G-3 | Bleibt der Cloud-Ordner? | Nein, parallel nutzen führt zu Konflikten. Git ist die einzige Quelle der Wahrheit; der Cloud-Ordner wird nach der Migration archiviert. |

## 2. Sicherheitsregeln (verbindlich)

1. **Repository privat**, nur namentlich eingeladene Mitglieder, kein „Anyone with link“.
2. **2-Faktor-Authentifizierung** für jedes Konto (Pflicht, in der Organisation erzwingbar).
3. **Zugang per SSH-Key oder Passkey/Credential-Manager**, keine Passwörter oder Tokens in Dateien, Chats oder Commits. Tokens nur mit minimalem Scope und Ablaufdatum.
4. **Signierte Commits** (SSH-Signatur, `git config gpg.format ssh`), damit Autorschaft belegbar ist. Pflicht per Gruppenregel; GitHub erzwingt sie im Free-Plan nicht.
5. **Schutz von `main`**: kein direkter Push, kein Force-Push, kein Löschen, Merge nur über Pull Request mit mindestens 1 Freigabe einer anderen Person, Konversationen gelöst. **Aktuell nur Gruppenregel, nicht technisch erzwungen** (Free-Plan, private Repos). Ersatzmaßnahmen: Abschnitt 7.
6. **Keine Geheimnisse und keine personenbezogenen Daten** im Repo: keine Zugangsdaten, keine privaten Adressen, Telefonnummern, Interviewdaten mit Klarnamen. Interviews nur anonymisiert (Kürzel).
7. **Secret-Scanning und Push-Protection**: unter *Settings → Code security* prüfen, ob sie für dieses Repo verfügbar sind (für private Repos im Free-Plan voraussichtlich nicht). Wenn nicht: vor jedem Commit `git status` und `git diff --cached` ansehen, zusätzlich lokal einen Pre-Commit-Hook (z. B. `gitleaks`) einrichten.
8. **Urheberrecht prüfen**: Die Statista-PDFs in `recherche/statista/` sind lizenzierte Inhalte. Nicht ins Repo, solange die Lizenz Weitergabe nicht klar erlaubt. Im Repo bleibt die Quellenangabe (URL, Abrufdatum) in `recherche/quellen.md`; die PDFs liegen in einem getrennten, zugriffsbeschränkten Ordner.
9. **Claude-Code-Konfiguration**: `.claude/settings.json` enthält absolute Pfade eines Nutzers und gehört nicht ins Repo. Persönliche Dateien (`settings.local.json`, `handoff_temp/`, `statusline.sh`, das Binary `jq`) bleiben lokal. Claude darf nie ohne ausdrückliche Anweisung committen oder pushen.
10. **Rückgängig machen**: Wurde versehentlich ein Geheimnis committet, gilt es als kompromittiert: sofort widerrufen/ändern, danach erst History bereinigen.

## 3. Arbeitsmodell

- **Trunk-basiert mit kurzlebigen Branches** (max. 1 Tag bis wenige Tage). Ein Branch pro Aufgabe.
- Branch-Namen: `kapitel/03-markt-anna`, `recherche/wettbewerber`, `finanzen/kapitalbedarf`. Kleinbuchstaben, ohne Umlaute und Leerzeichen.
- **Eine Person besitzt ein Kapitel/eine Datei zur Zeit** (Spalte „Verantwortliche“ in `ABGABENPLAN.md`). Das verhindert die meisten Konflikte.
- **Kleine Commits**, Nachricht auf Deutsch im Imperativ, z. B. `Kapitel 3: Marktgröße aus Angebot und Nachfrage ergänzt`. Ein Commit = eine Änderung.
- **Pull Request** mit kurzer Beschreibung: Was, welche Quellen, offene Fragen. Review durch eine andere Person; Prüfpunkte: Quelle vorhanden, Zahl in `ANNAHMEN-GLOSSAR.md`, Konsistenz mit anderen Kapiteln.
- **Vor dem Arbeiten** `git pull --rebase` auf `main`, vor dem PR erneut.
- Squash-Merge, damit `main` lesbar bleibt; Branch nach dem Merge löschen.

### Binärdateien (xlsx, pptx, pdf)

Lassen sich nicht zusammenführen. Regeln:
- Excel-Finanzmodell und Präsentation hat **je eine Person gleichzeitig** in Arbeit; Übergabe per Hinweis im Gruppenchat und Merge des Branches.
- Alternativ Texte/Zahlen als Markdown/CSV führen und die xlsx daraus bauen.
- Optional `.gitattributes` mit `*.xlsx binary`, `*.pptx binary`.

## 4. Einrichtung heute (Reihenfolge)

**Person A (Admin), ca. 20 Min.**
1. Privates Repository `businessplan-wallbox-sharing` anlegen, Mitglieder einladen (Rolle Write), 2FA verlangen.
2. Secret-Scanning und Push-Protection einschalten.
3. Lokal: `git init -b main`, `.gitignore` und `.gitattributes` anlegen (Abschnitt 5), Statista-PDFs und persönliche `.claude`-Dateien ausschließen, **erst `git status` prüfen**, dann ersten Commit, dann `git remote add origin …` und `git push -u origin main`.
4. Schutz von `main`: im Free-Plan nicht möglich, siehe Abschnitt 7.
5. `CODEOWNERS` optional: `kapitel/07-*` → Finanzverantwortliche.

**Alle anderen, je ca. 10 Min.**
1. Git installieren, 2FA aktivieren, SSH-Key erzeugen (`ssh-keygen -t ed25519`) und im Konto hinterlegen; Commit-Signatur konfigurieren; `user.name` und `user.email` (private Adresse bei GitHub ausblenden, „noreply“-Adresse nutzen).
2. `git clone`, Branch anlegen, Testdatei ändern, PR erstellen, von einer anderen Person freigeben lassen (Probelauf).

**Danach**
- Aufgaben in `ABGABENPLAN.md` den Personen zuweisen (ein Kapitel = eine Person).
- Cloud-Ordner auf schreibgeschützt setzen.

## 5. Vorlage `.gitignore`

Die gültige Fassung liegt als `.gitignore` im Projektordner. Wesentlich: `.claude/` (absolute Pfade, interne Handoffs, Binary `jq`) mit der einzigen Ausnahme `.claude/skills/onboarding/` und `recherche/statista/` (Lizenz) bleiben lokal; Geheimnisse (`.env*`, `*.pem`, `*.key`, `id_*`) und Office-Temporärdateien (`~$*`) sind ausgeschlossen.

## 6. Offene Punkte

- Lizenzlage der Statista-Dateien (siehe 2.8): wer prüft?
- Gibt es personenbezogene Daten in `kapitel/05b-rollen-kompetenzbereiche.md` oder `01b-personas.md`? Vor dem ersten Commit durchsehen.
- Hochschulvorgaben zu Hosting/Datenablage (G-1) klären.
- GitHub Student Developer Pack beantragen (siehe Abschnitt 7).

## 7. Ersatzmaßnahmen im Free-Plan und Weg zum technischen Schutz

Bis `main` technisch geschützt ist:
- **Gruppenregeln einhalten:** Nie direkt auf `main`, nie Force-Push, jede Änderung per Pull Request mit Freigabe einer anderen Person. Verstöße im Gruppenchat ansprechen.
- **Kontrolle:** Der Owner prüft regelmäßig bei GitHub unter *Commits* von `main`, ob dort Commits ohne Pull Request oder ohne „Verified“-Kennzeichen stehen.
- **Backup:** Jede Person hat durch den Klon die vollständige History. Wird `main` versehentlich überschrieben, stellt der Owner ihn aus einem aktuellen Klon wieder her.
- **Claude-Regeln:** `CLAUDE.md` verbietet Claude Push auf `main` und Force-Push.
- **Konten:** 2FA bei allen Mitgliedern (nicht erzwingbar, vor Einladung bestätigen lassen).

Weg zum technischen Schutz:
1. **GitHub Student Developer Pack** (education.github.com/pack, Nachweis über DHBW) gibt dem Konto kostenlos GitHub Pro. Danach wirken Rulesets (Pull-Request-Pflicht, Freigaben, Force-Push-Sperre, signierte Commits) auch im privaten Repo. Prüfung dauert Tage bis Wochen.
2. Alternativ GitLab.com Free (Rollen Maintainer/Developer, `main` für Direkt-Pushes sperrbar; Freigabepflicht und Signaturpflicht dort kostenpflichtig) oder eine GitHub-Organisation im Bezahltarif.
3. Nach dem Wechsel: Ruleset `main-schutz` mit den Punkten aus Abschnitt 2.5 anlegen und diese Datei aktualisieren.

## Quellen

Allgemein bekannte Praxis, nicht einzeln abgerufen: GitHub-Dokumentation (Branch Protection, Secret Scanning, 2FA, Commit-Signatur), Pro Git, OWASP-Hinweise zu Secrets Management. Vor Abgabe mit URL und Abrufdatum belegen, falls im Plan zitiert.
