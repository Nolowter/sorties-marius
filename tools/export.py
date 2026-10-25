#!/usr/bin/env python3
"""Exporte la base de l'artifact (dossier de snapshot ArtifactData) vers data/*.json.
Usage : python3 tools/export.py <dossier_snapshot>
Le dossier contient activites/*.json et meta/{etat,meteo}.json (sortie de ArtifactData list avec out_dir).
Affiche les ids d'images absentes de img/ (à récupérer avec Artifact read, path=<id>)."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
snap = sys.argv[1]
items = []
missing = []
def img(o):
    if not isinstance(o, dict) or not o.get("id"): return o
    o = dict(o); f = os.path.join(root, "img", o["id"] + ".jpg")
    o["url"] = "img/" + o["id"] + ".jpg"
    if not os.path.exists(f): missing.append(o["id"])
    return o
for f in sorted(glob.glob(os.path.join(snap, "activites", "*.json"))):
    d = json.load(open(f)); d["_id"] = os.path.basename(f)[:-5]
    if d.get("image"): d["image"] = img(d["image"])
    if isinstance(d.get("photos"), list): d["photos"] = [img(p) for p in d["photos"]]
    items.append(d)
json.dump(items, open(os.path.join(root, "data", "activites.json"), "w"), ensure_ascii=False, separators=(",", ":"))
for k in ("etat", "meteo"):
    p = os.path.join(snap, "meta", k + ".json")
    if os.path.exists(p):
        m = json.load(open(p)); m.pop("trigger_id", None)
        json.dump(m, open(os.path.join(root, "data", k + ".json"), "w"), ensure_ascii=False)
print(len(items), "activites ;", "images manquantes :", " ".join(sorted(set(missing))) or "aucune")
