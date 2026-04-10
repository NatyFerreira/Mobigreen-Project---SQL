# 🌿 **MobiGreen Urban — Projet SQL & ORM**

Analyse, modélisation et exploration des données de mobilité urbaine dans le cadre du projet **MobiGreen Urban**.  
Ce dépôt contient l’ensemble du pipeline : **SQL**, **ORM SQLAlchemy**, **pattern Repository**, **visualisations**, et **notebooks d’analyse**.

---

## 🚀 **Objectifs du projet**

- Concevoir une base de données relationnelle complète pour un système de mobilité urbaine.  
- Manipuler les données via **SQL avancé** (jointures, agrégations, vues, contraintes).  
- Implémenter un **ORM SQLAlchemy** propre et structuré.  
- Appliquer le **Repository Pattern** pour séparer logique métier et accès aux données.  
- Produire des **analyses visuelles** (matplotlib / seaborn).  
- Fournir des notebooks pédagogiques, reproductibles et bien documentés.

---

## 🗂️ **Structure du dépôt**

```
Mobigreen-Project---SQL/
│
├── notebooks/
│   ├── 01_SQL_Exploration.ipynb
│   ├── 02_SQL_Analyses.ipynb
│   ├── 03_ORM_Introduction.ipynb
│   ├── 04_ORM_Repositories.ipynb   ← version finale corrigée
│
├── src/mobigreen/
│   ├── database.py                 ← gestion des sessions SQLAlchemy
│   ├── models.py                   ← modèles ORM
│   ├── repositories/
│   │   ├── base_repository.py
│   │   ├── station_repository.py
│   │   ├── usager_repository.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧱 **Technologies utilisées**

- **Python 3.11+**
- **SQLAlchemy ORM**
- **PostgreSQL**
- **Docker (optionnel)**
- **Pandas**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

## 🧩 **Fonctionnalités principales**

### 🔹 Base de données & SQL
- Création du schéma complet (stations, usagers, trajets, véhicules, incidents…)
- Requêtes SQL avancées :
  - jointures multiples  
  - agrégations  
  - vues  
  - contraintes d’intégrité  

### 🔹 ORM SQLAlchemy
- Modèles Python propres et typés  
- Relations ORM (One-to-Many, Many-to-One)  
- Sessions sécurisées via context manager  

### 🔹 Pattern Repository
- `BaseRepository` générique  
- `StationRepository` (filtrage, disponibilité, zones)  
- `UsagerRepository` (abonnements, trajets, recherche par email)  
- Chargement optimisé via `joinedload`  

### 🔹 Analyses & Visualisations
- Nombre de trajets par usager  
- Taux d’occupation des stations  
- Statistiques globales de mobilité  

---

## 📊 **Exemples de visualisations**

- Histogrammes d’utilisation  
- Barplots des trajets par usager  
- Analyse des stations les plus occupées  

Les visualisations sont générées dans les notebooks 03 et 04.

---

## ⚙️ **Installation**

### 1. Cloner le dépôt

```bash
git clone https://github.com/NatyFerreira/Mobigreen-Project---SQL.git
cd Mobigreen-Project---SQL
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer votre base PostgreSQL  
Créer un fichier `.env` (non fourni dans le dépôt) :

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=yourpassword
DB_NAME=mobigreen
```

---

## 📘 **Notebooks disponibles**

| Notebook | Contenu |
|---------|---------|
| **01 – SQL Exploration** | Découverte des tables, premières requêtes |
| **02 – SQL Analyses** | Analyses avancées, KPIs, agrégations |
| **03 – ORM Introduction** | Modèles SQLAlchemy, sessions, premières requêtes ORM |
| **04 – ORM + Repository** | Pattern Repository, analyses, visualisations |

---

## 🧑‍💻 **Auteur**

**Natália Ferreira**  
Biologiste, PhD & Data Engineer en transition  
Projet réalisé dans le cadre du Campus Numérique in the Alps.

---

## 📄 **Licence**

Projet académique — libre d’utilisation à des fins pédagogiques.
