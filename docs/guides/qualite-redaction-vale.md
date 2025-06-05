# ✍️ Contrôler la rédaction avec Vale

Ce guide explique comment utiliser **Vale** pour harmoniser la documentation. Vale vérifie la grammaire, la ponctuation et applique un ton cohérent.

## Installer Vale

Téléchargez la dernière version depuis [GitHub](https://github.com/errata-ai/vale/releases) et placez l'exécutable dans votre `PATH`.

```bash
curl -L https://github.com/errata-ai/vale/releases/latest/download/vale_3.11.2_Linux_64-bit.tar.gz \
  | tar -xz
sudo mv vale /usr/local/bin/
```

## Utiliser le fichier `.vale.ini`

Le dépôt fournit une configuration minimale :

```ini
MinAlertLevel = warning
[*]
BasedOnStyles = Vale
```

Lancez Vale sur le dossier `docs` pour vérifier tous les articles :

```bash
vale docs/
```

## Bonnes pratiques

- Rédigez des phrases courtes et directes.
- Préférez la voix active.
- Évitez les adverbes superflus.
- Vérifiez les liens et le format Markdown avant de lancer Vale.

En suivant ces conseils, la documentation reste claire et professionnelle.
