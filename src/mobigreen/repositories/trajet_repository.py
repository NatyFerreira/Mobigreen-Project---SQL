from sqlalchemy.orm import Session
from sqlalchemy import select
from mobigreen.models import Trajet
from mobigreen.repositories.base_repository import BaseRepository


class TrajetRepository(BaseRepository[Trajet]):
    def __init__(self, session: Session):
        super().__init__(session, Trajet)

    def get_by_user(self, usr_id: int):
        stmt = select(Trajet).where(Trajet.usr_id == usr_id)
        return self.session.scalars(stmt).all()

    def get_by_vehicle(self, veh_id: int):
        stmt = select(Trajet).where(Trajet.veh_id == veh_id)
        return self.session.scalars(stmt).all()

    def get_by_station_depart(self, station_id: int):
        stmt = select(Trajet).where(Trajet.station_depart == station_id)
        return self.session.scalars(stmt).all()

    def get_by_station_arrivee(self, station_id: int):
        stmt = select(Trajet).where(Trajet.station_arrivee == station_id)
        return self.session.scalars(stmt).all()
