# 🛠️ Troubleshooting

Cette page recense les erreurs les plus courantes et comment les résoudre.

## Les conteneurs ne d\u00e9marrent pas

- Assurez-vous que Docker est en cours d'ex\u00e9cution.
- Recr\u00e9ez les images :
  ```bash
  make rebuild
  ```

## L'API reste inaccessible

- Utilisez le script de v\u00e9rification :
  ```bash
  .venv/bin/python utils/test_services.py
  ```
- Examinez les journaux :
  ```bash
  docker compose logs -f
  ```

## Erreurs de d\u00e9pendances Python

- (R\u00e9)installez les paquets :
  ```bash
  make install
  ```

## Probl\u00e8mes de documentation

- Testez la g\u00e9n\u00e9ration :
  ```bash
  mkdocs build
  ```
- V\u00e9rifiez le style :
  ```bash
  vale docs/
  ```

## Mod\u00e8les manquants ou corrompus

- Purgez les volumes et relancez :
  ```bash
  make purge-models
  make up
  ```

## Tout v\u00e9rifier d'un coup

- Lancez toutes les v\u00e9rifications :
  ```bash
  make universe
  ```
  Le rapport complet se trouve dans `rapports/universe.log`.
