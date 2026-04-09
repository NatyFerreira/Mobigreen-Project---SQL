from mobigreen.models import MesureAir
from mobigreen.repositories.base_repository import BaseRepository

class MesureAirRepository(BaseRepository[MesureAir]):
    def __init__(self, session):
        super().__init__(session, MesureAir)