# 🛠 Makefile

Le `Makefile` centralise plusieurs commandes utiles :
- `make up` lance les services Docker et le serveur FastAPI ;
- `make down` arrête les conteneurs ;
- `make rebuild` recrée les images Docker sans cache ;
- `make docs-serve` prévisualise la documentation ;
- `make docs-deploy` la publie sur GitHub Pages.
- `make universe` exécute tous les tests et génère `rapports/universe.log`.

En résumé, il simplifie le quotidien en évitant de longues lignes de commande.
