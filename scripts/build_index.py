#!/usr/bin/env python3
"""Régénère les index du coffre (navigation par divulgation progressive).

Niveau 1 : _index.md à la racine  -> les dossiers et quand y aller.
Niveau 2 : <dossier>/_index.md     -> une ligne par note (description du frontmatter).
Niveau 3 : la note elle-même.

Usage : python3 scripts/build_index.py   (à lancer après chaque ajout/renommage de note)
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", ".obsidian", "scripts", ".trash"}

FOLDERS = {
    "00-Inbox": "Vrac pas encore trié, questionnaires en cours.",
    "01-Journal": "Une note par jour (AAAA-MM-JJ.md).",
    "02-Personnes": "Une fiche par personne : relation, dates, centres d'intérêt, idées cadeaux.",
    "03-Projets": "Choses avec un objectif et une fin : side projects, démarches administratives.",
    "04-Domaines": "Responsabilités continues : famille, maison, voiture, finances, travail, objectifs, réseau, papiers.",
    "05-Idees": "Idées, réflexions, pistes business.",
    "06-Ressources": "Listes et savoirs : livres, films, liens, envies d'achat, méthodes.",
    "07-Archives": "Projets terminés ou abandonnés.",
    "Templates": "Modèles de notes (ne pas lire sauf pour créer une note).",
}

def frontmatter(path):
    try:
        txt = open(path, encoding="utf-8").read()
    except Exception:
        return {}
    m = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm

def notes_in(d):
    out = []
    for f in sorted(os.listdir(d)):
        p = os.path.join(d, f)
        if f.endswith(".md") and not f.startswith("_index") and os.path.isfile(p):
            out.append((f[:-3], frontmatter(p)))
    return out

def write(path, content):
    old = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    if old != content:
        open(path, "w", encoding="utf-8").write(content)
        return True
    return False

def main():
    missing, changed = [], []
    # Niveau 2 : un index par dossier
    for folder, purpose in FOLDERS.items():
        d = os.path.join(ROOT, folder)
        if not os.path.isdir(d) or folder == "Templates":
            continue
        rows = []
        for name, fm in notes_in(d):
            desc = fm.get("description", "")
            for sep in (" — ", " - "):
                if desc.startswith(name.split(" (")[0] + sep):
                    desc = desc[len(name.split(" (")[0] + sep):]
            if not desc:
                missing.append(f"{folder}/{name}.md")
            aliases = fm.get("aliases", "").strip("[]")
            extra = f" · alias : {aliases}" if aliases else ""
            rows.append(f"- [[{name}]] — {desc or '(description manquante)'}{extra}")
        body = "\n".join(rows) if rows else "*(vide)*"
        content = (f"---\ntype: index\ndescription: Index généré de {folder} — ne pas éditer à la main\n---\n"
                   f"# {folder}\n\n{purpose}\n\n{body}\n")
        if write(os.path.join(d, "_index.md"), content):
            changed.append(f"{folder}/_index.md")
    # Niveau 1 : index racine
    lines = ["---", "type: index", "description: Point d'entrée du coffre — généré par scripts/build_index.py", "---",
             "# Index du coffre", "",
             "Lire ce fichier, puis seulement le `_index.md` du dossier pertinent, puis seulement les notes utiles.", "",
             "## Dossiers"]
    for folder, purpose in FOLDERS.items():
        d = os.path.join(ROOT, folder)
        n = len(notes_in(d)) if os.path.isdir(d) else 0
        lines.append(f"- `{folder}/` ({n}) — {purpose}")
    lines += ["", "## À la racine"]
    for f in sorted(os.listdir(ROOT)):
        p = os.path.join(ROOT, f)
        if f.endswith(".md") and os.path.isfile(p) and f not in ("_index.md", "README.md", "CLAUDE.md"):
            fm = frontmatter(p)
            if not fm.get("description"):
                missing.append(f)
            lines.append(f"- [[{f[:-3]}]] — {fm.get('description', '(description manquante)')}")
    if write(os.path.join(ROOT, "_index.md"), "\n".join(lines) + "\n"):
        changed.append("_index.md")
    print("index modifiés :", ", ".join(changed) or "aucun")
    if missing:
        print("⚠️  description manquante :", *missing, sep="\n  - ")
        sys.exit(1)

if __name__ == "__main__":
    main()
