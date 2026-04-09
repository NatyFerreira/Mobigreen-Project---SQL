from datetime import datetime, timedelta, timezone
import random

from mobigreen.database import get_session
from mobigreen.models import (
    ZoneMetro, Station, Usager, Vehicule, Trajet, CapteurAir, Incident, DonneeMeteo, MesureAir
)

random.seed(42)

# -----------------------------
# 1. ZONAS
# -----------------------------
ZONES = [
    ("38185", "Grenoble"),
    ("38053", "Échirolles"),
    ("38079", "Fontaine"),
    ("38151", "Meylan"),
    ("38169", "Saint-Martin-d'Hères"),
]

# -----------------------------
# 2. ESTAÇÕES
# -----------------------------
STATIONS = [
    ("Victor Hugo", 45.1885, 5.7245, 20),
    ("Gare SNCF", 45.1910, 5.7144, 25),
    ("Caserne de Bonne", 45.1842, 5.7234, 18),
    ("Hoche", 45.1921, 5.7310, 22),
    ("Grand'Place", 45.1645, 5.7320, 30),
    ("Europole", 45.1918, 5.7085, 15),
    ("Presqu'île", 45.1970, 5.7050, 20),
]

NOMES = ["Martin", "Bernard", "Dubois", "Thomas", "Robert", "Richard"]
PRENOMS = ["Alice", "Lucas", "Emma", "Hugo", "Léa", "Louis"]
ABOS = ["mensuel", "annuel", "occasionnel"]

TYPE_VEH = ["velo", "trottinette"]


def seed():
    with get_session() as session:

        # -----------------------------
        # Criar zonas
        # -----------------------------
        zones = []
        for code, nome in ZONES:
            z = ZoneMetro(code_insee=code, nom=nome)
            session.add(z)
            zones.append(z)

        session.commit()

        # -----------------------------
        # Criar estações
        # -----------------------------
        stations = []
        for nome, lat, lon, cap in STATIONS:
            zone = random.choice(zones)
            s = Station(
                nom=nome,
                latitude=lat,
                longitude=lon,
                capacite=cap,
                places_dispo=random.randint(5, cap),
                zone_id=zone.zone_id,
            )
            session.add(s)
            stations.append(s)

        session.commit()

        # -----------------------------
        # Criar usuários
        # -----------------------------
        usagers = []
        for i in range(20):
            u = Usager(
                nom=random.choice(NOMES),
                prenom=random.choice(PRENOMS),
                email=f"user{i}@example.com",
                type_abonnement=random.choice(ABOS),
            )
            session.add(u)
            usagers.append(u)

        session.commit()

        # -----------------------------
        # Criar veículos
        # -----------------------------
        vehicules = []
        for i in range(30):
            tipo = random.choice(TYPE_VEH)

            v = Vehicule(
                type_veh=tipo,
                statut="disponible",
                niveau_batterie=(
                    random.randint(20, 100) if tipo == "trottinette" else None
                ),
                station_id=random.choice(stations).station_id,
                latitude=None,
                longitude=None,
            )
            session.add(v)
            vehicules.append(v)

        session.commit()

        # -----------------------------
        # Criar trajetos
        # -----------------------------
        for _ in range(50):
            u = random.choice(usagers)
            v = random.choice(vehicules)
            s1, s2 = random.sample(stations, 2)

            start = datetime.now(timezone.utc) - timedelta(days=random.randint(0, 10))
            end = start + timedelta(minutes=random.randint(5, 25))

            t = Trajet(
                usr_id=u.usr_id,
                veh_id=v.veh_id,
                station_depart=s1.station_id,
                station_arrivee=s2.station_id,
                date_debut=start,
                date_fin=end,
                duree_min=(end - start).total_seconds() / 60,
                distance_km=random.uniform(0.5, 5.0),
                montant_eur=random.uniform(1.0, 5.0),
            )
            session.add(t)

        session.commit()

        # -----------------------------
        # Criar sensores de ar
        # -----------------------------
        for s in stations:
            c = CapteurAir(
                station_id=s.station_id,
                type_capteur="qualite_air"
            )
            session.add(c)

        session.commit()

        # -----------------------------
        # Criar incidentes
        # -----------------------------
        for _ in range(10):
            inc = Incident(
                description="Incident aléatoire",
                type_incident="général",
                statut="ouvert",
                usr_id=random.choice(usagers).usr_id
            )
            session.add(inc)

        session.commit()

        print("Seed concluído com sucesso!")

        # -----------------------------
        # Criar données météo
        # -----------------------------
        for s in stations:
            for _ in range(3):
                m = DonneeMeteo(
                    station_id=s.station_id,
                    temperature=random.uniform(5, 30),
                    humidite=random.uniform(20, 90),
                    vent_kmh=random.uniform(0, 40),
                )
                session.add(m)

        session.commit()

        # -----------------------------
        # Criar mesures de qualité de l'air
        # -----------------------------
        for cap in session.query(CapteurAir).all():
            for _ in range(3):
                ma = MesureAir(
                    capteur_id=cap.capteur_id,
                    pm25=random.uniform(5, 50),
                    pm10=random.uniform(10, 80),
                    no2=random.uniform(5, 60),
                )
                session.add(ma)

        session.commit()

def demo_donnees_meteo():
    print("\n=== DEMO : Données Météo ===")

    with get_session() as session:
        repo = DonneeMeteoRepository(session)

        print("\n📌 Dernières données météo :")
        for m in repo.get_all()[:5]:
            print("  →", m)


def demo_mesures_air():
    print("\n=== DEMO : Mesures de Qualité de l'Air ===")

    with get_session() as session:
        repo = MesureAirRepository(session)

        print("\n📌 Dernières mesures d'air :")
        for m in repo.get_all()[:5]:
            print("  →", m)

demo_donnees_meteo()
demo_mesures_air()
