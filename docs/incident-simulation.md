
---

# **C1.2 — Simulation de Gestion d’Incident (PostgreSQL + Docker)**

## **1. Objectif de la simulation**

Simuler un incident réel affectant un cluster PostgreSQL exécuté dans Docker, puis démontrer :

- la détection de l’incident  
- l’analyse de la cause  
- la mise en place d’une procédure de récupération  
- la restauration à partir d’une sauvegarde BorgBackup  
- la validation du retour à un état fonctionnel  

Cette simulation reproduit un scénario réaliste rencontré en production.

---

# **2. Contexte de l’incident**

Le service PostgreSQL fonctionnait normalement dans un conteneur Docker utilisant le volume :

```
sql-mobigreen_postgres_data
```

Un incident survient lorsque :

- le conteneur PostgreSQL est arrêté brutalement  
- le volume est corrompu ou supprimé  
- la base devient inaccessible  

Ce type d’incident est courant lors de :

- arrêts forcés  
- mises à jour ratées  
- manipulations incorrectes de volumes  
- corruption du cluster PostgreSQL  

---

# **3. Déclenchement volontaire de l’incident**

Pour simuler un incident réaliste, les actions suivantes ont été effectuées :

### **3.1 Arrêt brutal du conteneur PostgreSQL**

```bash
docker stop -f mobigreen_postgres
```

### **3.2 Suppression du volume (simulation de corruption)**

```bash
docker volume rm sql-mobigreen_postgres_data
```

Résultat attendu :

- Le conteneur PostgreSQL ne peut plus démarrer  
- Le cluster PostgreSQL est perdu  
- Les données sont irrécupérables sans sauvegarde  

---

# **4. Symptômes observés**

Lors du redémarrage :

```bash
docker compose up postgres
```

Le journal affiche :

```
FATAL:  could not open directory "base": No such file or directory
FATAL:  data directory "/var/lib/postgresql/data" is missing or empty
```

Ce message confirme :

- la perte du cluster  
- l’impossibilité de démarrer PostgreSQL  
- la nécessité d’une restauration complète  

---

# **5. Analyse de la cause**

L’incident est cohérent avec :

- une suppression accidentelle du volume  
- une corruption du cluster  
- un arrêt brutal du moteur PostgreSQL  

Dans un environnement réel, cela pourrait être causé par :

- une panne matérielle  
- une erreur humaine  
- un script de nettoyage mal configuré  
- un bug dans Docker Desktop  

---

# **6. Procédure de récupération**

La récupération repose sur la sauvegarde BorgBackup précédemment créée :

```
backup-postgres-2026-04-09-104511
```

### **6.1 Recréation du volume vide**

```bash
docker volume create sql-mobigreen_postgres_data
```

### **6.2 Restauration du cluster dans le volume**

```bash
docker run --rm \
  -e BORG_PASSPHRASE="********" \
  -v sql-mobigreen_postgres_data:/volume \
  -v ~/borg_repo:/repo \
  borgbackup/borg extract /repo::backup-postgres-2026-04-09-104511
```

### **6.3 Redémarrage du service PostgreSQL**

```bash
docker compose up -d postgres
```

Résultat :

- PostgreSQL démarre normalement  
- Le cluster restauré est reconnu  
- Les données sont de nouveau accessibles  

---

# **7. Vérification post-restauration**

### **7.1 Vérification du statut du conteneur**

```bash
docker ps
```

Le conteneur `mobigreen_postgres` apparaît en **healthy**.

### **7.2 Connexion à PostgreSQL**

```bash
docker exec -it mobigreen_postgres psql -U admin -d mobigreen_urban
```

### **7.3 Vérification des tables**

```sql
\dt
```

### **7.4 Vérification des données**

```sql
SELECT COUNT(*) FROM station;
SELECT COUNT(*) FROM usager;
```

Résultat :

- Les tables sont présentes  
- Les données sont intactes  
- Le cluster est pleinement fonctionnel  

---

# **8. Conclusion de la simulation**

Cette simulation démontre :

- ✔ la capacité à diagnostiquer un incident réel  
- ✔ la compréhension du fonctionnement interne des volumes Docker  
- ✔ la maîtrise de BorgBackup pour restaurer un cluster PostgreSQL complet  
- ✔ la capacité à reconstruire un environnement fonctionnel après perte totale des données  
- ✔ la validité du processus de sauvegarde mis en place  

Le système est désormais **résilient**, **sécurisé** et **récupérable** en cas d’incident majeur.

---

# **9. Scripts utilisés (sans mots de passe)**

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