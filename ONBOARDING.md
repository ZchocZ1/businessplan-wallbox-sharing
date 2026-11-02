# Onboarding: Zugang zum Git-Repository

Ziel: in ca. 20 Minuten sicher eingerichtet und mit einem ersten Pull Request im Team-Repo. Teil A machst du selbst, Teil B führt dich dein Claude Code.

Repository (privat): `git@github.com:ZchocZ1/businessplan-wallbox-sharing.git`

## Teil A: Vorbereitung (selbst, ca. 15 Min.)

1. **GitHub-Konto mit 2FA.** Konto anlegen oder nutzen, unter *Settings → Password and authentication* die Zwei-Faktor-Authentifizierung einschalten (Authenticator-App oder Passkey). Recovery-Codes im Passwort-Manager speichern, nie im Projekt. Ohne 2FA keine Einladung annehmen.
2. **Einladung annehmen** (E-Mail von GitHub oder unter github.com/notifications). Du bekommst die Rolle *Write*.
3. **Git installieren.** macOS: im Terminal `git --version` (bietet die Installation an). Windows: „Git for Windows“ mit Git Bash.
4. **SSH-Schlüssel anlegen** (im Terminal, Passphrase vergeben und im Passwort-Manager speichern):
   ```
   ssh-keygen -t ed25519 -C "businessplan-github" -f ~/.ssh/id_ed25519_github
   ```
   macOS: `ssh-add --apple-use-keychain ~/.ssh/id_ed25519_github`. Windows (Git Bash): `eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519_github`.
   Den **öffentlichen** Schlüssel (Datei mit `.pub`) bei GitHub eintragen, **zweimal**: *Settings → SSH and GPG keys → New SSH key*, einmal als *Authentication Key* und einmal als *Signing Key*. Der private Schlüssel (ohne `.pub`) wird nie geteilt, nie in einen Chat oder an Claude gegeben.
5. **Verbindung testen:** `ssh -T git@github.com` muss „successfully authenticated“ melden.
6. **Git konfigurieren.** Noreply-Adresse unter GitHub *Settings → Emails* nachsehen (Format `123456+name@users.noreply.github.com`), „Keep my email addresses private“ und „Block command line pushes that expose my email“ aktivieren. Dann:
   ```
   git config --global user.name "DEIN NAME"
   git config --global user.email "DEINE-NOREPLY-ADRESSE"
   git config --global init.defaultBranch main
   git config --global pull.rebase true
   git config --global fetch.prune true
   git config --global gpg.format ssh
   git config --global user.signingkey ~/.ssh/id_ed25519_github.pub
   git config --global commit.gpgsign true
   git config --global tag.gpgsign true
   ```
   Falls der Schlüssel nicht automatisch genutzt wird, in `~/.ssh/config` ergänzen:
   ```
   Host github.com
     AddKeysToAgent yes
     IdentityFile ~/.ssh/id_ed25519_github
     IdentitiesOnly yes
   ```
   (macOS zusätzlich `UseKeychain yes`.)

## Teil B: Klonen und Onboarding mit Claude (ca. 5 Min.)

```
git clone git@github.com:ZchocZ1/businessplan-wallbox-sharing.git
cd businessplan-wallbox-sharing
claude
```

Claude Code fragt beim ersten Start, ob du dem Projektordner vertraust. Bestätige das erst, nachdem du `CLAUDE.md` und `.claude/skills/onboarding/SKILL.md` kurz angesehen hast. Es sind reine Textanweisungen. Beim ersten Start erkennt Claude, dass die lokale Marke `.git/onboarding-done` fehlt, und startet das Onboarding automatisch: Einrichtung prüfen, Projekt und Regeln in Kurzform, Probe-Pull-Request. Später jederzeit mit `/onboarding` wiederholbar.

## Wichtigste Regeln (Kurzfassung)

- Nie direkt auf `main`; immer Branch und Pull Request, eine andere Person gibt frei.
- Keine Geheimnisse, keine privaten Daten, keine lizenzierten PDFs im Repo.
- Ein Kapitel oder eine Datei gehört einer Person; Excel und PowerPoint nie gleichzeitig bearbeiten.
- Claude committet und pusht nur auf deine ausdrückliche Anweisung.
- Bei Problemen oder einem versehentlich committeten Geheimnis: sofort im Gruppenchat melden. Vollständige Regeln: `GIT-ZUSAMMENARBEIT.md`.
