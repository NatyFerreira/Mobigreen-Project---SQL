from mobigreen.models import TrajetAnalytics
from mobigreen.repositories.base_repository import BaseRepository

class TrajetAnalyticsRepository(BaseRepository[TrajetAnalytics]):
    def __init__(self, session):
        super().__init__(TrajetAnalytics, session)

    def list_by_station(self, station_id: int):
        return (
            self.session.query(TrajetAnalytics)
            .filter(TrajetAnalytics.station_depart == station_id)
            .all()
        )
