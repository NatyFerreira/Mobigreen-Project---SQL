from mobigreen.models import DonneeMeteo
from mobigreen.repositories.base_repository import BaseRepository

class DonneeMeteoRepository(BaseRepository[DonneeMeteo]):
    def __init__(self, session):
        super().__init__(session, DonneeMeteo)
