# 🔍 .vale.ini

`Vale` est un outil de lint pour la rédaction. Ce fichier minimal active le style par défaut et affiche les alertes à partir du niveau *warning*. L’objectif est d’harmoniser le ton de la documentation sans surcharger les auteurs de messages.

Contenu principal :
- `MinAlertLevel = warning` : ne signale que les règles importantes.
- `BasedOnStyles = Vale` : utilise le jeu de règles standard fourni par l’outil.

Ainsi, `.vale.ini` permet de vérifier rapidement les textes sans configuration complexe.

## Voir aussi

- [Guide d'utilisation de Vale](../guides/qualite-redaction-vale.md)
