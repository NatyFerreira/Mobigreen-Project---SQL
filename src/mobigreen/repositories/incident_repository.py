from sqlalchemy import select
from sqlalchemy.orm import Session
from mobigreen.models import Incident
from mobigreen.repositories.base_repository import BaseRepository


class IncidentRepository(BaseRepository[Incident]):
    def __init__(self, session: Session):
        super().__init__(session, Incident)

    def get_open_incidents(self):
        stmt = select(Incident).where(Incident.statut == "ouvert")
        return self.session.scalars(stmt).all()

    def get_by_user(self, usr_id: int):
        stmt = select(Incident).where(Incident.usr_id == usr_id)
        return self.session.scalars(stmt).all()
