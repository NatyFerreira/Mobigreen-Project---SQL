-- ============================================================
-- SCHEMA MOBIGREEN — GERADO A PARTIR DO models.py
-- ============================================================

-- ============================
-- TABLE zones_metro
-- ============================
CREATE TABLE zones_metro (
    zone_id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    code_insee VARCHAR(10) NOT NULL UNIQUE,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- TABLE stations
-- ============================
CREATE TABLE stations (
    station_id SERIAL PRIMARY KEY,
    nom VARCHAR(150) NOT NULL,
    adresse VARCHAR(255),
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    capacite INTEGER NOT NULL,
    places_dispo INTEGER NOT NULL DEFAULT 0,
    zone_id INTEGER REFERENCES zones_metro(zone_id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- TABLE vehicules
-- ============================
CREATE TABLE vehicules (
    veh_id SERIAL PRIMARY KEY,
    type_veh VARCHAR(20) NOT NULL,
    statut VARCHAR(30) NOT NULL DEFAULT 'disponible',
    niveau_batterie SMALLINT,
    latitude FLOAT,
    longitude FLOAT,
    station_id INTEGER REFERENCES stations(station_id) ON DELETE SET NULL,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- TABLE usagers
-- ============================
CREATE TABLE usagers (
    usr_id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    telephone VARCHAR(20),
    type_abonnement VARCHAR(30) NOT NULL DEFAULT 'payant',
    date_inscription TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- TABLE usager_pseudo
-- ============================
CREATE TABLE usager_pseudo (
    usager_id INTEGER PRIMARY KEY,
    usager_pseudo_id UUID NOT NULL UNIQUE
);

-- ============================
-- TABLE trajets
-- ============================
CREATE TABLE trajets (
    trj_id SERIAL PRIMARY KEY,
    date_debut TIMESTAMPTZ NOT NULL,
    date_fin TIMESTAMPTZ,
    duree_min FLOAT,
    distance_km FLOAT,
    montant_eur FLOAT,
    usr_id INTEGER REFERENCES usagers(usr_id) ON DELETE SET NULL,
    veh_id INTEGER REFERENCES vehicules(veh_id) ON DELETE SET NULL,
    station_depart INTEGER REFERENCES stations(station_id) ON DELETE SET NULL,
    station_arrivee INTEGER REFERENCES stations(station_id) ON DELETE SET NULL
);

-- ============================
-- TABLE capteurs_air
-- ============================
CREATE TABLE capteurs_air (
    capteur_id SERIAL PRIMARY KEY,
    type_capteur VARCHAR(50),
    station_id INTEGER REFERENCES stations(station_id) ON DELETE SET NULL
);

-- ============================
-- TABLE incidents
-- ============================
CREATE TABLE incidents (
    inc_id SERIAL PRIMARY KEY,
    type_incident VARCHAR(100),
    statut VARCHAR(50),
    description TEXT,
    usr_id INTEGER REFERENCES usagers(usr_id) ON DELETE SET NULL
);

-- ============================
-- TABLE donnees_meteo
-- ============================
CREATE TABLE donnees_meteo (
    meteo_id SERIAL PRIMARY KEY,
    station_id INTEGER REFERENCES stations(station_id) ON DELETE SET NULL,
    temperature FLOAT,
    humidite FLOAT,
    vent_kmh FLOAT,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- TABLE mesures_air
-- ============================
CREATE TABLE mesures_air (
    mesure_id SERIAL PRIMARY KEY,
    capteur_id INTEGER REFERENCES capteurs_air(capteur_id) ON DELETE SET NULL,
    pm25 FLOAT,
    pm10 FLOAT,
    no2 FLOAT,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- ============================
-- VIEW trajets_analytics (placeholder)
-- ============================
CREATE OR REPLACE VIEW trajets_analytics AS
SELECT
    t.trj_id,
    up.usager_pseudo_id,
    t.date_debut,
    t.date_fin,
    t.duree_min,
    t.distance_km,
    t.montant_eur,
    t.station_depart,
    t.station_arrivee,
    t.veh_id
FROM trajets t
LEFT JOIN usager_pseudo up ON up.usager_id = t.usr_id;
