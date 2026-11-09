# ElmasCore — Data Science & Competitive ML Hub

> **"From Data to Systems"** — Monorepo et laboratoire central des projets Data Science, Machine Learning compétitif (Kaggle) et systèmes analytiques signés **ElmasCore**.

---

## Architecture du Dépôt (Multi-Projets / Sous-Dépôts)

Ce dépôt racine (`DataScience/`) regroupe l'ensemble des projets Data Science sous forme de sous-dossiers autonomes (ou sous-modules Git). Chaque sous-projet respecte intégralement la charte [ELMAS.md](./ELMAS.md) :

```text
DataScience/
├── ELMAS.md                  # Charte de développement non négociable ElmasCore
├── README.md                 # Index central des projets Data Science
├── .gitignore                # Exclusion globale des datasets lourds, secrets et artefacts
└── PCCF/                     # [Kaggle S6E11] Predicting Credit Card Fraud
    ├── ELMAS.md
    ├── README.md
    ├── requirements.txt
    ├── src/                  # Architecture modulaire par domaine métier
    ├── tests/                # Suite de tests unitaires et d'intégrité
    └── main.py               # Orchestrateur d'entraînement et de soumission
```

---

## Projets Actifs

| Code Projet | Nom Complet | Compétition / Domaine | Métrique | Statut |
| :--- | :--- | :--- | :--- | :--- |
| **[PCCF](./PCCF)** | Predicting Credit Card Fraud | Kaggle Playground Series S6E11 | `ROC-AUC` | En cours (Cible : #1 LB) |

---

## Ajouter un Nouveau Sous-Projet

Chaque nouveau projet Data Science doit être créé dans son propre répertoire dédié à la racine de `DataScience/` :

1. Créer le dossier du projet (`mkdir NomDuProjet`) ou l'ajouter en tant que sous-module (`git submodule add <url> NomDuProjet`).
2. Copier la charte `ELMAS.md` à la racine du sous-projet.
3. Structurer le code exclusivement par domaine métier (`data_pipeline/`, `feature_engineering/`, `modeling/`, `validation/`, `ensembling/`, `submission/`).
4. Ne jamais versionner de données brutes (`data/raw/`) ni de clés d'API (`kaggle.json`, `.env`).
5. Référencer le sous-projet dans le tableau ci-dessus.

---

— **Elmas**, ElmasCore
