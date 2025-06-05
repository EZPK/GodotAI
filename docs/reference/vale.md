# 🔍 .vale.ini

`Vale` est un outil de lint pour la rédaction. Le projet active un style personnalisable pour un ton plus direct et cohérent.

Contenu principal :
- `MinAlertLevel = warning` : ne signale que les règles importantes.
- `StylesPath = .vale/styles` : localisation des règles maison.
- `BasedOnStyles = Vale` : conserve le jeu de règles standard.
- `Packages = CoolStyle` : applique nos règles supplémentaires.

Ainsi, `.vale.ini` permet de vérifier rapidement les textes tout en profitant de règles adaptées au projet.
