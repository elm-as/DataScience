# WORKFLOW.md — Protocole de Gouvernance & Synchronisation Multi-Dépôts

> **Protocole d'ingénierie et de maintenance pour le hub `DataScience/` et ses sous-projets.**  
> Ce document formalise les règles de synchronisation parent-enfant et les standards de livraison d'ElmasCore.

---

## 1. Règle de Synchronisation Parent-Enfant (Git Submodules)

Le dépôt `DataScience/` est le point d'entrée unique (Hub) qui référence l'ensemble des projets de recherche et de modélisation sous forme de **sous-modules Git**.

Chaque intervention sur un sous-projet doit suivre ce workflow strict :

### A. Création d'un Nouveau Sous-Projet
1. Initialiser le sous-dossier comme dépôt Git autonome sous `elm-as/<PROJET>`.
2. L'enregistrer dans le dépôt racine comme sous-module officiel :
   ```bash
   cd c:\Users\elmas\Desktop\DataScience
   git submodule add https://github.com/elm-as/<PROJET>.git <PROJET>
   ```
3. **Mettre à jour immédiatement `DataScience/README.md`** :
   - Ajouter le projet dans le tableau des **Projets Actifs** (nom, domaine, métriques de validation, statut, lien du dépôt).
   - Actualiser le schéma d'arborescence.
   - Ajouter une section de synthèse avec capture d'écran dans `DataScience/images/`.

### B. Évolution ou Livraison d'un Sous-Projet Existant
1. Valider la suite de tests unitaires (`pytest`).
2. Exporter les graphiques représentatifs dans `<PROJET>/images/` et copier une copie dans `DataScience/images/`.
3. Commiter et pousser dans le sous-dépôt :
   ```bash
   cd <PROJET>
   git add .
   git commit -m "feat/fix: description"
   git push origin main
   ```
4. Revenir à la racine `DataScience/`, actualiser les métriques de validation dans `DataScience/README.md`, commiter et pousser le hub parent :
   ```bash
   cd c:\Users\elmas\Desktop\DataScience
   git add <PROJET> images/ README.md
   git commit -m "chore(submodule): update <PROJET> and sync documentation"
   git push origin main
   ```

---

## 2. Standard de Documentation Technique

Tout projet doit comporter :
1. **Un README riche et illustré** :
   - En-tête centré avec badges de stack technique et licences.
   - Tableau synthétique des indicateurs clés (`<h2>...</h2><sub>...</sub>`).
   - Diagrammes Mermaid formalisant l'architecture et les séquences de calcul.
   - Graphiques de résultats intégrés localement depuis le dossier `images/`.
   - Dictionnaire complet des variables et tableau des hyperparamètres.
2. **Un Notebook de Référence (`notebooks/`)** :
   - Notebook Jupyter autonome permettant à un tiers de reproduire les calculs pas à pas.
3. **Une Suite de Tests Automatisée (`tests/`)** :
   - Couvrant l'intégrité des données, la validation sans fuite et les métriques de sortie.
