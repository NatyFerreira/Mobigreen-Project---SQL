# MobiGreen Urban — Librairie Python

## 1. Presentation

Ce projet est le support des **Jours 4 et 5** du module Base de donnees SQL,
dans le cadre de la formation Data Engineer (RNCP 37624 — Bloc 1).
Il constitue le squelette d'une librairie Python d'acces a votre base `mobigreen_urban`,
concue et implementee lors des trois premiers jours (Kit 1).

## 2. Structure du projet

```
mobigreen-urban-db/
│
├── README.md                            # Ce fichier
├── .env.example                         # Template des variables d'environnement
├── .gitignore                           # Fichiers ignores par Git
├── pyproject.toml                       # Configuration du projet Python
│
├── notebooks/                           # Jour 4 — Notebooks Jupyter
│   ├── apprenant_01_psycopg2.ipynb      # Connexion directe avec psycopg2
│   ├── apprenant_02_pandas.ipynb        # Integration pandas + SQL
│   └── apprenant_03_sqlalchemy_intro.ipynb  # Introduction a SQLAlchemy
│
├── src/
│   └── mobigreen/                       # Package principal — Jour 5
│       ├── __init__.py                  # Initialisation du package
│       ├── config.py                    # Chargement de la configuration
│       ├── database.py                  # Gestion de la connexion et des sessions
│       ├── models.py                    # Modeles ORM (a completer)
│       └── repositories/
│           ├── __init__.py              # Initialisation des repositories
│           └── base_repository.py       # Repository generique CRUD
│
├── scripts/
│   └── demo.py                          # Script de demonstration (a completer)
│
└── tests/
    ├── conftest.py                      # Fixtures pytest
    └── test_example.py                  # Tests exemple (a completer)
```

## 3. Installation

```bash
git clone <url-du-repo>
cd mobigreen-urban-db
python -m venv .venv && source .venv/bin/activate   # Linux/macOS
pip install -e ".[notebooks,dev]"
cp .env.example .env
# Editez .env et renseignez DATABASE_URL avec vos identifiants PostgreSQL
```

## 4. Pre-requis

- PostgreSQL 15+ operationnel en local
- Base `mobigreen_urban` creee et peuplee (resultat du Kit 1)
- Fichier `.env` configure

## 5. Jour 4 — Notebooks

Lancez Jupyter Lab pour travailler sur les notebooks :

```bash
jupyter lab notebooks/
```

**Notebooks disponibles :**

| Notebook | Description |
|----------|-------------|
| `apprenant_01_psycopg2.ipynb` | Connexion directe a PostgreSQL avec psycopg2, requetes SQL brutes |
| `apprenant_02_pandas.ipynb` | Lecture de donnees SQL dans des DataFrames pandas |
| `apprenant_03_sqlalchemy_intro.ipynb` | Introduction a SQLAlchemy Core et ORM |

Completez les notebooks dans l'ordre pour progresser du bas niveau (psycopg2) vers l'abstraction (SQLAlchemy).

## 6. Jour 5 — Completer le package mobigreen

**Etape 1 — Declarer les modeles ORM**

Ouvrir `src/mobigreen/models.py` et creer une classe pour chaque table de votre schema.
Suivre le patron et les instructions fournis dans le fichier.

**Etape 2 — Creer les repositories**

Dans `src/mobigreen/repositories/`, creer un fichier `xxx_repository.py` par entite principale,
en heritant de `BaseRepository` et en ajoutant les methodes metier specifiques.

**Etape 3 — Completer et lancer le script de demo**

```bash
python scripts/demo.py
```

## 7. Tests

```bash
pytest                                        # tous les tests
pytest -v                                     # mode verbeux
pytest --cov=mobigreen --cov-report=term      # couverture de code
```

> Les tests utilisent **SQLite en memoire** — aucune connexion PostgreSQL requise.
> Ils necessitent que vos modeles soient declares dans `models.py`.

## 8. Objectif de la journee

Chaque `raise NotImplementedError` est un exercice a completer.
La journee est reussie quand tous les `NotImplementedError` sont remplaces
par du code fonctionnel et couvert par au moins un test.
