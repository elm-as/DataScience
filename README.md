# ElmasCore — Data Science & Competitive ML Hub

> **"From Data to Systems"** — Monorepo et laboratoire central des projets Data Science, Machine Learning compétitif (Kaggle) et modélisations économétriques signés **ElmasCore**.

---

## 1. Architecture du Dépôt (Multi-Projets & Sous-Modules Git)

Ce dépôt racine (`DataScience/`) orchestre l'ensemble des systèmes de recherche et de modélisation sous forme de sous-modules Git autonomes. Chaque projet dispose de son propre dépôt GitHub, de son cycle de vie indépendant et applique strictement les règles non négociables définies dans [ELMAS.md](./ELMAS.md) :

```text
DataScience/
├── ELMAS.md                  # Charte de développement non négociable ElmasCore
├── README.md                 # Index central et gouvernance des projets
├── .gitignore                # Exclusion globale des caches et artefacts temporaires
├── .gitmodules               # Déclaration des sous-modules Git officiels
│
├── PCCF/                     # [Kaggle S6E11] Predicting Credit Card Fraud
│   ├── src/                  # Pipeline tabulaire : FE domain-specific, ensembling
│   ├── tests/                # Validation d'intégrité et tests unitaires
│   ├── main.py               # Orchestrateur d'entraînement et de soumission
│   └── README.md             # Documentation spécifique au leaderboard S6E11
│
└── GGVCF/                    # Global Gun Violence & Civilian Firearms (2000–2024)
    ├── src/                  # Panel Two-Way FE, PCA + K-Means, analyse spatiale
    ├── artifacts/            # Dashboard interactif HTML5 / Plotly autonome
    ├── tests/                # Suite de tests d'inférence et d'économétrie
    ├── main.py               # Moteur d'estimation économétrique
    └── README.md             # Rapport méthodologique et empirique complet
```

---

## 2. Projets Actifs

| Code Projet | Nom & Domaine | Cadre Méthodologique | Métriques Clés | Statut | Dépôt Dédié |
| :--- | :--- | :--- | :--- | :---: | :---: |
| **[PCCF](./PCCF)** | **Predicting Credit Card Fraud**<br>*(Kaggle S6E11)* | Gradient Boosting (LGBM, CatBoost, XGB), Wide LM, RealMLP & Blending Rank-Average | `ROC-AUC` $\ge 0.9533$ | **En cours**<br>(Cible : Top 1 Leaderboard) | [`elm-as/PCCF`](https://github.com/elm-as/PCCF) |
| **[GGVCF](./GGVCF)** | **Global Gun Violence & Civilian Firearms**<br>*(2000–2024)* | Panel Two-Way FE (`PanelOLS`), PCA + $K$-Means Archetypes, Random Forest Feature Importance | Spearman $\rho = -0.0026$<br>FE $\beta_{\text{PIB}} = -0.3491$ | **Livré & Validé**<br>(Dashboard interactif inclus) | [`elm-as/GGVCF`](https://github.com/elm-as/GGVCF) |

---

## 3. Synthèse des Projets

### 🛡️ PCCF — Predicting Credit Card Fraud (Kaggle S6E11)
- **Objectif** : Détection de transactions frauduleuses hautement asymétriques sur plus de 1 million d'observations réelles et synthétiques.
- **Stack** : LightGBM, CatBoost, XGBoost, RealMLP, Stratified K-Fold CV, Target Encoding out-of-fold, interaction ratios métier.
- **Architecture** : Conception 100% domaine (`core/`, `data_pipeline/`, `feature_engineering/`, `modeling/`, `validation/`, `ensembling/`, `submission/`).

### 🌍 GGVCF — Global Gun Violence & Civilian Firearms (2000–2024)
- **Objectif** : Résolution du paradoxe empirique mondial entre saturation en armes civiles et létalité par arme à feu across 95 pays (ONUDC $\times$ Small Arms Survey $\times$ Banque Mondiale).
- **Découvertes** :
  - Absence de corrélation bivariée ($\rho = -0.0026$, $p = 0.9804$) entre le taux d'armes pour 100 habitants et le taux d'homicides par arme.
  - Prépondérance absolue des facteurs structurels : l'indice de Gini explique **$59.8\%$** de la variance non-linéaire.
  - Identification de 4 régimes mondiaux et dashboard interactif autonome [`artifacts/dashboard.html`](./GGVCF/artifacts/dashboard.html).

---

## 4. Initialisation & Clonage Complet

Pour cloner le dépôt parent et l'ensemble de ses sous-projets en une seule instruction :

```bash
git clone --recurse-submodules https://github.com/elm-as/DataScience.git
cd DataScience
```

Si le dépôt principal est déjà cloné :
```bash
git submodule update --init --recursive
```

---

## 5. Gouvernance ElmasCore

Chaque sous-système de ce dépôt doit respecter sans dérogation la charte [ELMAS.md](./ELMAS.md) :
1. **Zéro code spaghetti** : Découpage par domaine métier, 3 niveaux d'indentation maximum, sorties précoce obligatoires (*guard clauses*).
2. **Plafond de taille** : **350 lignes maximum par fichier**, sans exception de confort.
3. **Fonctions pures & typage strict** : Maximum 3 arguments par signature, zéro mutation sauvage, traçabilité totale.
4. **Finition visuelle** : Typographie soignée, chiffres tabulaires alignés, zéro template générique.

---

— **Elmas**, ElmasCore
