# Adapter le prompt système

Le fichier `Modelfile` définit le prompt système envoyé au modèle lors de chaque génération. Pour le personnaliser :

1. Éditez `Modelfile` et modifiez la section `SYSTEM` selon vos besoins.
2. Si vous changez d'autres paramètres (par exemple `PARAMETER temperature 0.7`), enregistrez le fichier.
3. Redémarrez Ollama pour appliquer les modifications :
   ```bash
   make down
   make up
   ```
   Le prompt modifié sera pris en compte lors des prochaines requêtes.

## Voir aussi

- [Référence du `Modelfile`](../reference/modelfile.md)

## FAQ

### Comment vérifier que le nouveau prompt est appliqué ?

Redémarrez Ollama avec `make down` puis `make up`. Les journaux indiquent le
modèle et le prompt chargés.

### Peut‑on définir plusieurs prompts ?

Non. Le fichier `Modelfile` ne contient qu'une seule section `SYSTEM`. Modifiez
cette section pour changer de prompt.
