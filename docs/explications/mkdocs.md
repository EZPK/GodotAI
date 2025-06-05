# 📚 MkDocs

MkDocs transforme les fichiers Markdown du dossier `docs/` en un site statique prêt à être publié. Le thème Material apporte un rendu moderne et agréable.

Depuis la version 8 du thème, Mermaid est pris en charge nativement. En déclarant simplement un bloc de code `mermaid`, le script est chargé et les diagrammes sont rendus automatiquement.

```mermaid
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#6200ee','primaryTextColor':'#ffffff','primaryBorderColor':'#6200ee','lineColor':'#6200ee','fontFamily':'Roboto'}}}%%
flowchart LR
    M[Markdown] --> MK(MkDocs)
    MK --> HTML[Site statique]
    click MK "mkdocs.md" "Voir la page MkDocs"
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
