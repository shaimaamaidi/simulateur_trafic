# simulateur_trafic

Un simulateur modulaire du trafic routier en Python.  
Ce projet permet de simuler des routes, des véhicules et des feux rouges, avec des tests unitaires et une intégration continue via GitHub Actions.

## Fonctionnalités

- Gestion des routes et des véhicules
- Gestion des feux rouges (vert, orange, rouge)
- Mise à jour des positions des véhicules en fonction de la vitesse et des feux
- Tests unitaires avec `pytest`
- Couverture de code avec `pytest-cov`
- CI/CD configurée avec GitHub Actions

## Installation

```bash
poetry install
poetry shell
