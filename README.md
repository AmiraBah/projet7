# Mon projet de Machine Learning 

## Objectif
Ce projet vise à entraîner un modèle de machine learning pour prédire des scores de crédit. Le projet utilise `MLflow` pour le suivi des expérimentations et `FastAPI` pour déployer une API permettant d'utiliser le modèle en production.

## Structure du projet
- `notebooks/` : Contient le notebook Jupyter pour l'entraînement et le test du modèle.
- `api/` : Code FastAPI pour exposer le modèle via une API REST.
- `models/` : Modèles entraînés et sauvegardés via MLflow.
- `README.md` : Ce fichier, expliquant l'objectif du projet et sa structure.
- `requirements.txt` : Liste des packages nécessaires pour faire tourner le projet.
- `test/` : Contient les tests unitaires pour l'API.

## Installation
1. Cloner ce dépôt.
2. Installer les dépendances via pip :
   ```bash
   pip install -r requirements.txt
3. Lancer l'API:
   uvicorn api.app:app --reload
