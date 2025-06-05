# 📚 MkDocs

MkDocs transforme les fichiers Markdown du dossier `docs/` en un site statique prêt à être publié. Le thème Material apporte un rendu moderne et agréable.

La configuration active également le plugin [Mermaid](https://github.com/fralau/mkdocs-mermaid2-plugin) pour intégrer des schémas. Celui‑ci insère automatiquement la bibliothèque Mermaid et initialise les diagrammes avec `securityLevel: loose`.

```html
<script type="module">
  import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
  mermaid.initialize({ startOnLoad: true });
</script>

<div class="mermaid">
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#6200ee','primaryTextColor':'#ffffff','primaryBorderColor':'#6200ee','lineColor':'#6200ee','fontFamily':'Roboto'}}}%%
flowchart LR
    M[Markdown] --> MK(MkDocs)
    MK --> HTML[Site statique]
    click MK "mkdocs.md" "Voir la page MkDocs"
</div>
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
