# 📚 mkdocs.yml

Ce fichier configure le site de documentation généré par **MkDocs**.

Principales sections :

- `site_name` et `site_url` définissent le nom du projet et son adresse en ligne.
- `theme` indique le thème Material utilisé pour le rendu.
- `nav` liste l'ensemble des pages et leur organisation dans la barre de navigation.
- `plugins` active notamment `mermaid2` pour les diagrammes.

Après chaque ajout de page, exécutez :

```bash
mkdocs build
```

Cette commande s'assure que la documentation est valide avant une éventuelle publication.
