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
