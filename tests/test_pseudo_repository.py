from mobigreen.database import SessionLocal
from mobigreen.repositories.trajet_analytics_repository import TrajetAnalyticsRepository

session = SessionLocal()
repo = TrajetAnalyticsRepository(session)

repo.list_by_station(1)