from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select
from mobigreen.models import Usager
from mobigreen.repositories.base_repository import BaseRepository

class UsagerRepository(BaseRepository[Usager]):
    def __init__(self, session: Session):
        super().__init__(session, Usager)

    def get_by_email(self, email: str) -> Usager | None:
        stmt = select(Usager).where(Usager.email == email)
        return self.session.scalars(stmt).first()

    def get_by_abonnement(self, type_abonnement: str) -> list[Usager]:
        stmt = select(Usager).where(Usager.type_abonnement == type_abonnement)
        return self.session.scalars(stmt).all()

    def get_with_trajets(self) -> list[Usager]:
        stmt = (
            select(Usager)
            .options(joinedload(Usager.trajets))
        )
        return self.session.execute(stmt).unique().scalars().all()
