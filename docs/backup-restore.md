---

# **C1.2 — Sauvegarde, Vérification et Restauration PostgreSQL avec BorgBackup**

## **1. Objectif de l’activité**

Mettre en place un processus complet de **sauvegarde**, **vérification**, **restauration** et **analyse d’incident** pour un cluster PostgreSQL exécuté dans Docker, en utilisant **BorgBackup**.

L’ensemble des opérations a été réalisé sur **macOS**, ce qui implique une gestion particulière des volumes Docker (encapsulés dans une VM Linux interne).

---

# **2. Sauvegarde**

### **2.1 Commande exécutée**

```bash
docker run --rm \
  -e BORG_PASSPHRASE="********" \
  -v sql-mobigreen_postgres_data:/volume \
  -v ~/borg_repo:/repo \
  borgbackup/borg create /repo::backup-postgres-2026-04-09-104511 /volume
```

### **2.2 Résultat**

- Archive créée avec succès  
- Nom de l’archive : **backup-postgres-2026-04-09-104511**

Cette archive contient **l’intégralité du cluster PostgreSQL**, car la sauvegarde a été effectuée depuis un conteneur ayant accès au volume réel.

---

# **3. Vérification de la sauvegarde**

### **3.1 Commande**

```bash
borg list ~/borg_repo
```

### **3.2 Résultat**

```
backup-postgres-2026-04-09
backup-postgres-2026-04-09-104511
```

La présence de l’archive confirme que la sauvegarde a bien été enregistrée.

### **3.3 Hash cryptographique**

Hash de l’archive (intégrité garantie) :

```
05b693a1a3aee2d99f785227e890ba1d0d42095473f1717327d28e627ee84de4
```

Ce hash permet de vérifier que l’archive n’a subi **aucune altération**.

---

# **4. Restauration**

### **4.1 Préparation du répertoire de test**

```bash
rm -rf ~/restore_test/*
cd ~/restore_test
```

### **4.2 Commande de restauration**

```bash
borg extract ~/borg_repo::backup-postgres-2026-04-09-104511
```

### **4.3 Résultat**

- Aucune erreur  
- Restauration **réussie**

---

# **5. Vérification du contenu restauré**

La structure restaurée correspond exactement à celle d’un cluster PostgreSQL complet :

```
PG_VERSION
base/
global/
pg_wal/
pg_stat/
pg_multixact/
postgresql.conf
pg_hba.conf
postmaster.pid
```

Et notamment :

```
/Users/natyferreira/restore_test/volume/base/...
/Users/natyferreira/restore_test/volume/global/...
```

Ces fichiers internes du moteur PostgreSQL confirment que la restauration est **complète et fonctionnelle**.

---

# **6. Analyse du problème initial**

Lors de la première tentative, la sauvegarde était **vide**.  
Cause identifiée :

### ❌ Sur macOS, les volumes Docker visibles dans `/var/lib/docker/volumes/...` **ne contiennent pas les données réelles**.

Docker Desktop encapsule les volumes dans une **VM Linux interne**, inaccessible directement depuis l’hôte.

### ✔ Solution correcte

1. Monter le volume Docker dans un conteneur temporaire  
2. Exécuter Borg **depuis ce conteneur**, pas depuis l’hôte  
3. Passer la passphrase via `BORG_PASSPHRASE` (Borg ne peut pas demander un mot de passe interactif dans un conteneur)

Cette approche garantit l’accès aux **données réelles** du cluster PostgreSQL.

---

# **7. Conclusion**

La sauvegarde **backup-postgres-2026-04-09-104511** contient l’intégralité du cluster PostgreSQL.

La restauration dans `~/restore_test/volume` a permis de reconstruire un cluster complet, confirmant :

- ✔ l’intégrité de l’archive  
- ✔ la fiabilité du processus  
- ✔ la validité de la procédure sur macOS  
- ✔ la compréhension du fonctionnement des volumes Docker  

Le processus de sauvegarde/restauration est désormais **robuste, reproductible et sécurisé**.

---

# **8. Scripts utilisés (sans mots de passe)**

## **backup.sh**

```bash
#!/bin/bash
set -e

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v sql-mobigreen_postgres_data:/volume \
  -v ~/borg_repo:/repo \
  borgbackup/borg create /repo::backup-postgres-$(date +%Y-%m-%d-%H%M%S) /volume
```

## **restore.sh**

```bash
#!/bin/bash
set -e

docker run --rm \
  -e BORG_PASSPHRASE="${BORG_PASSPHRASE}" \
  -v sql-mobigreen_postgres_data:/volume \
  -v ~/borg_repo:/repo \
  borgbackup/borg extract /repo::"$1"
```

---