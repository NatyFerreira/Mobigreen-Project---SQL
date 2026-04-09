from sqlalchemy.orm import Session
from sqlalchemy import select
from mobigreen.models import Station, ZoneMetro
from mobigreen.repositories.base_repository import BaseRepository

class StationRepository(BaseRepository[Station]):
    def __init__(self, session: Session):
        super().__init__(session, Station)

    def get_by_zone(self, code_insee: str) -> list[Station]:
        """
        Retorna todas as estações pertencentes a uma zona cujo code_insee corresponde.
        """
        stmt = (
            select(Station)
            .join(ZoneMetro, Station.zone_id == ZoneMetro.zone_id)
            .where(ZoneMetro.code_insee == code_insee)
        )
        return self.session.scalars(stmt).all()

    def get_disponibles(self, nb_places_min: int = 1) -> list[Station]:
        """
        Retorna estações com pelo menos nb_places_min vagas disponíveis.
        """
        stmt = select(Station).where(Station.places_dispo >= nb_places_min)
        return self.session.scalars(stmt).all()
