# src/mobigreen/models.py

from sqlalchemy import (
    Column, Integer, String, Float, SmallInteger,
    DateTime, ForeignKey, Text
)
from sqlalchemy.dialects.postgresql import TIMESTAMP, UUID
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timezone

Base = declarative_base()


# ---------------------------------------------------------
# ZONE METRO
# ---------------------------------------------------------
class ZoneMetro(Base):
    __tablename__ = "zones_metro"

    zone_id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    code_insee = Column(String(10), nullable=False, unique=True)
    created_at = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relations
    stations = relationship("Station", back_populates="zone")

    def __repr__(self):
        return f"<ZoneMetro(id={self.zone_id}, nom='{self.nom}')>"


# ---------------------------------------------------------
# STATION
# ---------------------------------------------------------
class Station(Base):
    __tablename__ = "stations"

    station_id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)
    adresse = Column(String(255))
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    capacite = Column(Integer, nullable=False)
    places_dispo = Column(Integer, nullable=False, default=0)
    zone_id = Column(
        Integer,
        ForeignKey("zones_metro.zone_id", ondelete="SET NULL"),
        nullable=True
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relations
    zone = relationship("ZoneMetro", back_populates="stations")
    vehicules = relationship("Vehicule", back_populates="station_actuelle")
    capteurs = relationship("CapteurAir", back_populates="station")

    def __repr__(self):
        return f"<Station(id={self.station_id}, nom='{self.nom}')>"


# ---------------------------------------------------------
# VEHICULE
# ---------------------------------------------------------
class Vehicule(Base):
    __tablename__ = "vehicules"

    veh_id = Column(Integer, primary_key=True)
    type_veh = Column(String(20), nullable=False) 
    statut = Column(String(30), nullable=False, default="disponible")
    niveau_batterie = Column(SmallInteger, nullable=True)  # NULL pour vélos
    latitude = Column(Float)
    longitude = Column(Float)
    station_id = Column(
        Integer,
        ForeignKey("stations.station_id", ondelete="SET NULL"),
        nullable=True
    )
    created_at = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relations
    station_actuelle = relationship("Station", back_populates="vehicules")

    def __repr__(self):
        return (
            f"<Vehicule(id={self.veh_id}, type='{self.type_veh}', "
            f"statut='{self.statut}')>"
        )

# ---------------------------------------------------------
# USAGERS
# ---------------------------------------------------------
class Usager(Base):
    __tablename__ = "usagers"

    usr_id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prenom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    telephone = Column(String(20))
    type_abonnement = Column(String(30), nullable=False, default="payant")
    date_inscription = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    # Relations
    trajets = relationship("Trajet", back_populates="usager")
    incidents = relationship("Incident", back_populates="usager")

    def __repr__(self):
        return f"<Usager(id={self.usr_id}, email='{self.email}')>"


# ---------------------------------------------------------
# USAGER PSEUDO (RGPD)
# ---------------------------------------------------------
class UsagerPseudo(Base):
    __tablename__ = "usager_pseudo"

    # FK lógica (não relacional) para usagers.usr_id
    usager_id = Column(Integer, primary_key=True)

    # Identificador pseudonimizado
    usager_pseudo_id = Column(UUID(as_uuid=True), unique=True, nullable=False)

    def __repr__(self):
        return (
            f"<UsagerPseudo(usager_id={self.usager_id}, "
            f"pseudo='{self.usager_pseudo_id}')>"
        )


# ---------------------------------------------------------
# TRAJET
# ---------------------------------------------------------
class Trajet(Base):
    __tablename__ = "trajets"

    trj_id = Column(Integer, primary_key=True)
    date_debut = Column(TIMESTAMP(timezone=True), nullable=False)
    date_fin = Column(TIMESTAMP(timezone=True))
    duree_min = Column(Float)
    distance_km = Column(Float)
    montant_eur = Column(Float)

    usr_id = Column(Integer, ForeignKey("usagers.usr_id", ondelete="SET NULL"))
    veh_id = Column(Integer, ForeignKey("vehicules.veh_id", ondelete="SET NULL"))
    station_depart = Column(Integer, ForeignKey("stations.station_id", ondelete="SET NULL"))
    station_arrivee = Column(Integer, ForeignKey("stations.station_id", ondelete="SET NULL"))

    # Relations
    usager = relationship("Usager", back_populates="trajets")
    vehicule = relationship("Vehicule")
    station_depart_rel = relationship("Station", foreign_keys=[station_depart])
    station_arrivee_rel = relationship("Station", foreign_keys=[station_arrivee])

    def __repr__(self):
        return f"<Trajet(id={self.trj_id}, duree={self.duree_min} min)>"


# ---------------------------------------------------------
# CAPTEUR AIR
# ---------------------------------------------------------
class CapteurAir(Base):
    __tablename__ = "capteurs_air"

    capteur_id = Column(Integer, primary_key=True)
    type_capteur = Column(String(50))
    station_id = Column(
        Integer,
        ForeignKey("stations.station_id", ondelete="SET NULL"),
        nullable=True
    )

    station = relationship("Station", back_populates="capteurs")

    def __repr__(self):
        return f"<CapteurAir(id={self.capteur_id})>"


# ---------------------------------------------------------
# INCIDENT
# ---------------------------------------------------------
class Incident(Base):
    __tablename__ = "incidents"

    inc_id = Column(Integer, primary_key=True)
    type_incident = Column(String(100))
    statut = Column(String(50))
    description = Column(Text)
    usr_id = Column(Integer, ForeignKey("usagers.usr_id", ondelete="SET NULL"))

    usager = relationship("Usager", back_populates="incidents")

    def __repr__(self):
        return f"<Incident(id={self.inc_id}, type='{self.type_incident}')>"

# ---------------------------------------------------------
# DONNEE METEO
# ---------------------------------------------------------
class DonneeMeteo(Base):
    __tablename__ = "donnees_meteo"

    meteo_id = Column(Integer, primary_key=True)
    station_id = Column(
        Integer,
        ForeignKey("stations.station_id", ondelete="SET NULL"),
        nullable=True
    )
    temperature = Column(Float)
    humidite = Column(Float)
    vent_kmh = Column(Float)
    timestamp = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    station = relationship("Station")

    def __repr__(self):
        return (
            f"<DonneeMeteo(id={self.meteo_id}, temp={self.temperature}°C, "
            f"station={self.station_id})>"
        )

# ---------------------------------------------------------
# MESURE AIR
# ---------------------------------------------------------
class MesureAir(Base):
    __tablename__ = "mesures_air"

    mesure_id = Column(Integer, primary_key=True)
    capteur_id = Column(
        Integer,
        ForeignKey("capteurs_air.capteur_id", ondelete="SET NULL"),
        nullable=True
    )
    pm25 = Column(Float)
    pm10 = Column(Float)
    no2 = Column(Float)
    timestamp = Column(
        TIMESTAMP(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    capteur = relationship("CapteurAir")

    def __repr__(self):
        return (
            f"<MesureAir(id={self.mesure_id}, PM2.5={self.pm25}, "
            f"capteur={self.capteur_id})>"
        )

# ---------------------------------------------------------
# VIEW: TRAJETS ANALYTICS (RGPD)
# ---------------------------------------------------------
class TrajetAnalytics(Base):
    __tablename__ = "trajets_analytics"
    __table_args__ = {"extend_existing": True}

    trj_id = Column(Integer, primary_key=True)
    usager_pseudo_id = Column(UUID(as_uuid=True))
    date_debut = Column(TIMESTAMP(timezone=True))
    date_fin = Column(TIMESTAMP(timezone=True))
    duree_min = Column(Float)
    distance_km = Column(Float)
    montant_eur = Column(Float)
    station_depart = Column(Integer)
    station_arrivee = Column(Integer)
    veh_id = Column(Integer)

    def __repr__(self):
        return f"<TrajetAnalytics(id={self.trj_id}, pseudo='{self.usager_pseudo_id}')>"
