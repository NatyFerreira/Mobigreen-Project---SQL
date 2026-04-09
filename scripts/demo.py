"""
Script de démonstration — package mobigreen
Usage :
    python scripts/demo.py
"""

from mobigreen.database import get_session

from mobigreen.repositories.usager_repository import UsagerRepository
from mobigreen.repositories.station_repository import StationRepository
from mobigreen.repositories.trajet_repository import TrajetRepository
from mobigreen.repositories.incident_repository import IncidentRepository
from mobigreen.repositories.vehicule_repository import VehiculeRepository
from mobigreen.repositories.donnee_meteo_repository import DonneeMeteoRepository
from mobigreen.repositories.mesure_air_repository import MesureAirRepository


# -----------------------------
# DEMO USAGERS
# -----------------------------
def demo_usagers():
    print("\n=== DEMO : Usagers ===")

    with get_session() as session:
        repo = UsagerRepository(session)

        print("\n📌 Tous les usagers :")
        for u in repo.get_all()[:5]:
            print("  →", u)

        print("\n📌 Recherche par abonnement 'mensuel' :")
        for u in repo.get_by_abonnement("mensuel"):
            print("  →", u)

        print("\n📌 Recherche par email :")
        u = repo.get_by_email("user0@example.com")
        print("  →", u)


# -----------------------------
# DEMO STATIONS
# -----------------------------
def demo_stations():
    print("\n=== DEMO : Stations ===")

    with get_session() as session:
        repo = StationRepository(session)

        print("\n📌 Stations disponibles :")
        for s in repo.get_disponibles(nb_places_min=1):
            print("  →", s.nom, f"({s.places_dispo}/{s.capacite})")

        print("\n📌 Stations à Grenoble (38185) :")
        for s in repo.get_by_zone("38185"):
            print("  →", s)


# -----------------------------
# DEMO TRAJETS
# -----------------------------
def demo_trajets():
    print("\n=== DEMO : Trajets ===")

    with get_session() as session:
        repo = TrajetRepository(session)

        print("\n📌 Trajets de l'usager 1 :")
        for t in repo.get_by_user(1):
            print("  →", t)


# -----------------------------
# DEMO INCIDENTS
# -----------------------------
def demo_incidents():
    print("\n=== DEMO : Incidents ===")

    with get_session() as session:
        repo = IncidentRepository(session)

        print("\n📌 Incidents ouverts :")
        for inc in repo.get_open_incidents():
            print("  →", inc)


# -----------------------------
# DEMO VEHICULES
# -----------------------------
def demo_vehicules():
    print("\n=== DEMO : Véhicules ===")

    with get_session() as session:
        repo = VehiculeRepository(session)

        print("\n📌 Véhicules disponibles :")
        for v in repo.get_disponibles():
            print("  →", v)

        print("\n📌 Trottinettes :")
        for v in repo.get_by_type("trottinette"):
            print("  →", v)

        print("\n📌 Vélos :")
        for v in repo.get_by_type("velo"):
            print("  →", v)


# -----------------------------
# DEMO DONNEES METEO
# -----------------------------
def demo_donnees_meteo():
    print("\n=== DEMO : Données Météo ===")

    with get_session() as session:
        repo = DonneeMeteoRepository(session)

        print("\n📌 Dernières données météo :")
        for m in repo.get_all()[:5]:
            print("  →", m)

        print("\n📌 Données météo pour la station 1 :")
        for m in repo.get_all():
            if m.station_id == 1:
                print("  →", m)


# -----------------------------
# DEMO MESURES AIR
# -----------------------------
def demo_mesures_air():
    print("\n=== DEMO : Mesures de Qualité de l'Air ===")

    with get_session() as session:
        repo = MesureAirRepository(session)

        print("\n📌 Dernières mesures d'air :")
        for m in repo.get_all()[:5]:
            print("  →", m)

        print("\n📌 Mesures du capteur 1 :")
        for m in repo.get_all():
            if m.capteur_id == 1:
                print("  →", m)


# -----------------------------
# MAIN
# -----------------------------
if __name__ == "__main__":
    print("=== DEMONSTRATION MobiGreen Urban ===")

    demo_usagers()
    demo_stations()
    demo_trajets()
    demo_incidents()
    demo_vehicules()
    demo_donnees_meteo()
    demo_mesures_air()
