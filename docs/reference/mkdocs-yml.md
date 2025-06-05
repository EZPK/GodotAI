# 📚 mkdocs.yml

Ce fichier configure le site de documentation généré par **MkDocs**.

Principales sections :

- `site_name` et `site_url` définissent le nom du projet et son adresse en ligne.
- `theme` indique le thème Material utilisé pour le rendu.
- `plugins` active `mkdocs-d2-plugin` pour gérer les diagrammes.
- `nav` liste l'ensemble des pages et leur organisation dans la barre de navigation.
- `markdown_extensions` configure un fence `d2` via **SuperFences**.
  Material charge alors automatiquement la bibliothèque D2.

Après chaque ajout de page, exécutez :

```bash
mkdocs build
```

Cette commande s'assure que la documentation est valide avant une éventuelle publication.

Pour faciliter ces actions, utilisez `make docs-serve` pour un aperçu local et `make docs-deploy` pour la publication.

## Voir aussi

- [Présentation de MkDocs](../explications/mkdocs.md)
