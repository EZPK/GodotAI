# 📚 MkDocs

MkDocs transforme les fichiers Markdown du dossier `docs/` en un site statique prêt à être publié. Le thème Material apporte un rendu moderne et agréable.

Le thème Material peut également afficher des diagrammes **D2** depuis des blocs de code `d2`.

```d2
M: "Markdown"
MK: "MkDocs"
HTML: "Site statique"

M -> MK
MK -> HTML
```

Pour tester en local :
```bash
make install
make docs-serve
```

## Voir aussi

- [Fichier `mkdocs.yml`](../reference/mkdocs-yml.md)
- [Contrôler la rédaction avec Vale](../guides/qualite-redaction-vale.md)

## Ressources
- [Site officiel](https://www.mkdocs.org/)
- [Documentation](https://www.mkdocs.org/user-guide/)
