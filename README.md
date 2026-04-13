# 🌿 **MobiGreen Urban — Projet SQL, ORM & Sécurité**

Projet complet de modélisation, manipulation, sécurisation et analyse de données de mobilité urbaine.  
Ce dépôt couvre l’ensemble du pipeline : **PostgreSQL**, **SQL avancé**, **ORM SQLAlchemy**, **Repository Pattern**, **Docker**, **audit & sécurité**, **visualisations**, et **notebooks d’analyse**.

---

## 🚀 **Objectifs du projet**

- Concevoir une base de données relationnelle robuste pour un système de mobilité urbaine.  
- Manipuler les données via **SQL avancé** (jointures, agrégations, vues, contraintes).  
- Implémenter un **ORM SQLAlchemy** propre, typé et structuré.  
- Appliquer le **Repository Pattern** pour séparer logique métier et accès aux données.  
- Mettre en place un environnement **Dockerisé** reproductible.  
- Implémenter un pipeline complet de **sécurité & audit** :
  - prévention d’injection SQL  
  - pgaudit  
  - logs structurés (CSV / JSON)  
  - rôles & privilèges minimaux  
- Produire des **analyses visuelles** (matplotlib / seaborn).  
- Fournir des notebooks pédagogiques, reproductibles et bien documentés.

---

## 🗂️ **Structure du dépôt**

```
SQL-mobigreen/
│
├── init/                          ← scripts SQL d'initialisation (schema + seed)
│   ├── 01_init.sql
│   ├── 02_schema.sql
│   ├── 03_seed.sql
│
├── notebooks/
│   ├── Notebook 01.ipynb          ← Exploration SQL
│   ├── Notebook 02.ipynb          ← Analyses SQL
│   ├── Notebook 03.ipynb          ← ORM SQLAlchemy
│   ├── Notebook 04.ipynb          ← Repository Pattern
│
├── scripts/
│   ├── backup.sh                  ← sauvegarde PostgreSQL
│   ├── restore.sh                 ← restauration PostgreSQL
│
├── src/mobigreen/
│   ├── database.py                ← gestion des sessions SQLAlchemy
│   ├── models.py                  ← modèles ORM
│   ├── config.py                  ← configuration DB 
│   ├── seed.py                    ← génération de données réalistes
│   ├── repositories/
│       ├── base_repository.py
│       ├── station_repository.py
│       ├── usager_repository.py
│       ├── vehicule_repository.py
│       ├── trajet_repository.py
│
├── tests/
│   ├── test_injection_vulnerable.py
│   ├── test_injection_secure.py
│   ├── test_pgcrypto.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## 🧱 **Technologies utilisées**

- **Python 3.11+**
- **SQLAlchemy ORM**
- **PostgreSQL 16**
- **pgaudit** (audit SQL)
- **Docker & Docker Compose**
- **Pandas**
- **Matplotlib / Seaborn**
- **Jupyter Notebook**

---

## 🔐 **Sécurité & Audit**

### 🔹 Prévention d’injection SQL
- démonstration d’une requête vulnérable  
- correction via **requêtes paramétrées** et ORM  
- tests automatisés (`test_injection_secure.py`)

### 🔹 Audit PostgreSQL avec pgaudit
- activation via `shared_preload_libraries = 'pgaudit'`
- journalisation des opérations :
  - SELECT  
  - INSERT  
  - UPDATE  
  - DELETE  
  - accès aux métadonnées  
- logs structurés en **CSV** et **JSON**

### 🔹 Logging avancé
- `logging_collector = on`
- rotation automatique des logs
- stockage dans `pg_log/`
- format JSON compatible SIEM

### 🔹 Rôles & privilèges
- création d’un rôle **analyste** en lecture seule  
- accès limité à une vue pseudonymisée (`usagers_pseudo`)  
- interdiction d’accès aux données sensibles

---

## 🧩 **Fonctionnalités principales**

### 🔹 Base de données & SQL
- schéma complet : usagers, véhicules, stations, trajets, incidents, capteurs, météo  
- vues analytiques  
- contraintes d’intégrité  
- seed réaliste (trajets, incidents, mesures d’air, météo)

### 🔹 ORM SQLAlchemy
- modèles typés  
- relations One-to-Many / Many-to-One  
- sessions sécurisées via context manager  

### 🔹 Repository Pattern
- séparation stricte logique métier / accès DB  
- méthodes spécialisées :
  - recherche d’usagers  
  - disponibilité des stations  
  - statistiques de trajets  
  - filtrage des véhicules  

### 🔹 Analyses & Visualisations
- KPIs de mobilité  
- taux d’occupation  
- distribution des trajets  
- analyses temporelles  

---

## 📊 **Exemples de visualisations**

- histogrammes d’utilisation  
- heatmaps de stations  
- barplots des trajets par usager  
- analyses temporelles (jour / heure / météo)

Les visualisations sont générées dans les notebooks 02, 03 et 04.

---

## ⚙️ **Installation**

### 1. Cloner le dépôt

```bash
git clone https://github.com/NatyFerreira/SQL-mobigreen.git
cd SQL-mobigreen
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

### 4. Configurer PostgreSQL  
Créer un fichier `.env` (non fourni) :

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=admin
DB_PASSWORD=yourpassword
DB_NAME=mobigreen_urban
```

### 5. Lancer l’environnement Docker

```bash
docker compose up -d
```

---

## 📘 **Notebooks disponibles**

| Notebook | Contenu |
|---------|---------|
| **01 – Exploration SQL** | Découverte du schéma, premières requêtes |
| **02 – Analyses SQL** | KPIs, agrégations, vues analytiques |
| **03 – ORM SQLAlchemy** | Modèles, sessions, requêtes ORM |
| **04 – Repository Pattern** | Repositories, analyses, visualisations |

---

## 🧑‍💻 **Auteur**

**Natália Ferreira**  
Biologiste, PhD — Data Engineer en transition  
Projet réalisé dans le cadre du Campus Numérique in the Alps.

---

## 📄 **Licence**

Projet académique — libre d’utilisation à des fins pédagogiques.
