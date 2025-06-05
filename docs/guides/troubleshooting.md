# 🛠️ Troubleshooting

Cette page recense les erreurs les plus courantes et comment les résoudre.

## Les conteneurs ne démarrent pas

- Assurez-vous que Docker est en cours d'exécution.
- Recréez les images :
  ```bash
  make rebuild
  ```

## L'API reste inaccessible

- Utilisez le script de vérification :
  ```bash
  .venv/bin/python utils/test_services.py
  ```
- Examinez les journaux :
  ```bash
  docker compose logs -f
  ```

## Erreurs de dépendances Python

- (Ré)installez les paquets :
  ```bash
  make install
  ```

## Problèmes de documentation

- Testez la génération :
  ```bash
  mkdocs build
  ```
- Vérifiez le style :
  ```bash
  vale docs/
  ```

## Modèles manquants ou corrompus

- Purgez les volumes et relancez :
  ```bash
  make cleanall
  make up
  ```

## Tout vérifier d'un coup

- Lancez toutes les vérifications :
  ```bash
  make universe
  ```
  Le rapport complet se trouve dans `rapports/universe.log`.
