# Instructions pour Claude — coffre « brain »

- Toujours commencer par `git pull --rebase` avant de modifier quoi que ce soit.
- Après CHAQUE modification : commit + `git push` immédiatement, pour que le coffre reste synchronisé avec Obsidian (plugin Obsidian Git) sur tous les appareils de Rudy. Ne jamais laisser de changement non poussé.
- Messages de commit courts, en français.
- Règles de rangement : voir README.md.

## Navigation : divulgation progressive (ne jamais lire tout le coffre)
Le coffre est organisé comme des skills : on ne charge que ce qui est pertinent.
1. **Niveau 1** — `_index.md` à la racine : les dossiers et à quoi ils servent.
2. **Niveau 2** — `<dossier>/_index.md` : une ligne par note (sa `description`, et les alias pour les personnes).
3. **Niveau 3** — ouvrir uniquement les notes utiles à la demande.
- Pour retrouver une personne ou un mot précis, préférer `grep -ril "<mot>" <dossier>` à la lecture de plusieurs notes.
- Ne pas ouvrir `Templates/` sauf pour créer une note ; ne pas ouvrir les `_index.md` d'autres dossiers « au cas où ».

## Écrire une note
- Chaque note a dans son frontmatter une `description:` d'une ligne, précise et autonome (qui/quoi + l'info clé), car c'est elle qui permet de choisir la note sans l'ouvrir.
- Après chaque création, renommage ou changement de description : lancer `python3 scripts/build_index.py` (régénère les `_index.md` ; échoue si une description manque), puis commit + push.
- Ne jamais éditer les `_index.md` à la main.
- Garder les notes courtes : au-delà d'environ 150 lignes, découper en sous-notes liées.

## Usages prioritaires de Rudy
- Logistique du foyer : papiers, inscriptions et paiements des enfants, échéances de la voiture → `04-Domaines/Maison.md`, `Voiture.md`, `Papiers et numéros utiles.md`.
- Anniversaires : tableau dans `04-Domaines/Famille.md`. Pour des idées de cadeaux, lire les sections « Centres d'intérêt » et « Idées cadeaux » de la fiche personne, puis chercher sur le web des cadeaux adaptés.
- Tâches avec échéance : `À faire.md`.
