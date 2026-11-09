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

— **Elmas**, ElmasCore
