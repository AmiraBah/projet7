# Projet API de Prédiction de Défaut

## Introduction

Ce projet met en place une API RESTful utilisant FastAPI pour prédire la probabilité de défaut d'un client. L'API utilise un modèle de régression logistique entraîné pour évaluer les données des clients et fournir une prédiction en fonction des caractéristiques spécifiées.

## Objectifs du Projet

- Fournir une interface API pour les prédictions de défaut.
- Permettre aux utilisateurs de soumettre des données de clients et de recevoir des probabilités de défaut et des classes (accepté ou refusé).
- Utiliser un seuil optimisé pour les prédictions en fonction des besoins métier (0.53).

## Découpage des Dossiers

- **app/**: Contient le code de l'API
  - **app.py**: Point d'entrée de l'application FastAPI.
  
- **data/**: Contient les fichiers de données nécessaires pour l'imputation, la normalisation et le modèle de prédiction.

- **requirements.txt**: Liste des packages Python nécessaires pour exécuter l'application.
