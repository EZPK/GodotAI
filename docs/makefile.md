# 🛠 Makefile

Le `Makefile` centralise plusieurs commandes utiles :
- `make up` lance tous les conteneurs via Docker Compose ;
- `make down` arrête les conteneurs ;
- `make rebuild` recrée les images Docker sans cache ;
- `make purge-models` supprime les modèles enregistrés dans les volumes Docker ;
- `make up-models` lance la stack en choisissant `MODEL_TEXT` et `MODEL_IMAGE`,
  puis affiche les noms retenus ;
- `make docs-serve` prévisualise la documentation ;
- `make docs-deploy` la publie sur GitHub Pages.
- `make universe` exécute tous les tests et génère `rapports/universe.log`.

En résumé, il simplifie le quotidien en évitant de longues lignes de commande.
