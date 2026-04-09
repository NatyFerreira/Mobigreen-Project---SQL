from sqlalchemy.orm import Session
from sqlalchemy import select
from mobigreen.models import Vehicule
from mobigreen.repositories.base_repository import BaseRepository


class VehiculeRepository(BaseRepository[Vehicule]):
    def __init__(self, session: Session):
        super().__init__(session, Vehicule)

    def get_disponibles(self):
        stmt = select(Vehicule).where(Vehicule.statut == "disponible")
        return self.session.scalars(stmt).all()

    def get_by_type(self, type_veh: str):
        stmt = select(Vehicule).where(Vehicule.type_veh == type_veh)
        return self.session.scalars(stmt).all()
