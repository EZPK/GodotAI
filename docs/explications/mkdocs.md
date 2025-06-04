# 📚 MkDocs

MkDocs transforme les fichiers Markdown du dossier `docs/` en un site statique prêt à être publié. Le thème Material apporte un rendu moderne et agréable.

La configuration active également le plugin [Mermaid](https://github.com/fralau/mkdocs-mermaid2-plugin) pour intégrer des schémas.

```mermaid
flowchart LR
    M[Markdown] --> MK(MkDocs)
    MK --> HTML[Site statique]
```

Pour tester en local :
```bash
make install
make docs-serve
```

## Ressources
- [Site officiel](https://www.mkdocs.org/)
- [Documentation](https://www.mkdocs.org/user-guide/)
