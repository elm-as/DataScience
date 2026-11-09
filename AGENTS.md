# AGENTS.md — Protocole Obligatoire pour Agents IA (ElmasCore)

> **Ce protocole est une directive impérative pour tout agent IA (Claude Code, Cursor, Codex, Gemini, Antigravity) opérant dans le workspace `DataScience/`.**  
> Il complète et renforce la charte [ELMAS.md](./ELMAS.md).

---

## 1. Règle d'Or de Synchronisation Parent-Enfant (Submodule Hub)

Le dossier racine `DataScience/` est le **dépôt central (Hub)** qui référence et orchestre tous les projets sous forme de **sous-modules Git**.

Chaque fois qu'un agent IA :
1. **Crée un nouveau sous-projet** (ex: `PCCF/`, `GGVCF/`, nouveau projet Kaggle ou recherche) :
   - Initialiser git dans le sous-dossier, créer le remote GitHub sous l'organisation `elm-as/<PROJECT>`.
   - L'ajouter comme sous-module officiel dans le repo parent :
     ```bash
     cd c:\Users\elmas\Desktop\DataScience
     git submodule add https://github.com/elm-as/<PROJECT>.git <PROJECT>
     ```
   - **Mettre à jour immédiatement `DataScience/README.md`** :
     - Ajouter le projet dans le tableau des **Projets Actifs** (Nom, domaine, métriques de validation, statut, lien du dépôt).
     - Mettre à jour l'arborescence des dossiers.
     - Ajouter une section de synthèse du nouveau projet.

2. **Améliore un sous-projet existant** (nouveau modèle, nouveau score CV, nouveaux graphiques, ajout de notebook) :
   - Commiter et pusher les modifications dans le sous-dépôt (`git push origin main`).
   - Revenir à la racine `DataScience/`, mettre à jour les métriques dans `DataScience/README.md` si un palier a été franchi.
   - Mettre à jour le pointeur du sous-module :
     ```bash
     cd c:\Users\elmas\Desktop\DataScience
     git add <PROJECT> README.md
     git commit -m "chore(submodule): update <PROJECT> to <commit_hash>"
     git push origin main
     ```

---

## 2. Standard Esthétique des READMEs (Niveau Publication / "LatentHealth Standard")

Tout README de sous-projet (et le README parent) ne doit **JAMAIS être plat ni textuel uniquement**. Il doit comporter :

1. **En-tête centré** avec :
   - Titre percutant et baseline métier.
   - Badges shields.io cohérents (Python, stack technique, licences, métriques).
2. **Tableau des KPIs Clés** :
   - Cartouche synthétique en haut de page (`<table align="center"><tr>...</tr></table>`) avec chiffres clés en grand (`<h2>...</h2><sub>...</sub>`).
3. **Table des matières** cliquable.
4. **Diagrammes Mermaid** obligatoires :
   - Au minimum 1 `flowchart LR` ou `flowchart TD` montrant le pipeline de données et de modélisation.
   - Au minimum 1 `sequenceDiagram` pour les mécanismes critiques (ex: cross-validation sans fuite, inférence).
5. **Graphiques & Preuves Visuelles** :
   - Fichiers graphiques stockés dans `images/` et intégrés dans des tableaux Markdown (`<table><tr><td>...</td></tr></table>`).
   - Dictionnaire des variables clair (code source, type, description).
   - Tableau de benchmark des modèles avec hyperparamètres et métriques réelles.
6. **Support Notebooks** :
   - Tout projet d'analyse ou de modélisation doit proposer un notebook Jupyter documenté dans `notebooks/` permettant à un tiers de reproduire les visualisations en local ou sur Google Colab.

---

## 3. Checklist Obligatoire pour chaque Turn Agent

Avant de considérer une tâche terminée dans `DataScience` :
- [ ] Le code respecte les 350 lignes max par fichier et les 3 niveaux d'indentation max ([ELMAS.md](./ELMAS.md)).
- [ ] La suite de tests unitaires passe (`pytest`).
- [ ] Le `README.md` du sous-projet est riche, illustré et documenté.
- [ ] Le `README.md` du dépôt parent `DataScience/` a été synchronisé.
- [ ] Les commits du sous-projet et du parent sont synchronisés sur GitHub.
