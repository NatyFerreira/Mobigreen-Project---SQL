"""
Repository generique fournissant les operations CRUD de base.

Ce module definit la classe BaseRepository qui peut etre heritee
pour creer des repositories specifiques a chaque entite du modele.
"""

from typing import TypeVar, Generic, Type, Optional, List

from sqlalchemy.orm import Session

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """Repository generique fournissant les operations CRUD de base.

    A heriter pour chaque entite du modele de donnees.

    Attributes:
        model: La classe du modele ORM gere par ce repository.
        session: La session SQLAlchemy utilisee pour les operations.

    Example:
        class MonRepository(BaseRepository[MonModele]):
            def __init__(self, session: Session) -> None:
                super().__init__(MonModele, session)

            def find_by_name(self, name: str) -> list[MonModele]:
                return self.session.query(self.model).filter_by(name=name).all()
    """

    def __init__(self, model: Type[T], session: Session) -> None:
        """Initialise le repository avec le modele et la session.

        Args:
            model: La classe du modele ORM a gerer.
            session: La session SQLAlchemy a utiliser.
        """
        self.model = model
        self.session = session

    def get_by_id(self, entity_id: int) -> Optional[T]:
        """Recupere une entite par son identifiant.

        Args:
            entity_id: L'identifiant de l'entite a recuperer.

        Returns:
            L'entite correspondante ou None si non trouvee.
        """
        return self.session.get(self.model, entity_id)

    def get_all(self) -> List[T]:
        """Recupere toutes les entites.

        Returns:
            Liste de toutes les entites presentes en base.
        """
        return self.session.query(self.model).all()

    def create(self, entity: T) -> T:
        """Cree une nouvelle entite en base.

        L'entite est ajoutee a la session et flushee pour obtenir
        son identifiant genere. Le commit doit etre effectue
        par l'appelant (ou par le context manager get_session).

        Args:
            entity: L'entite a creer.

        Returns:
            L'entite creee avec son identifiant genere.
        """
        self.session.add(entity)
        self.session.flush()
        return entity

    def delete(self, entity: T) -> None:
        """Supprime une entite de la base.

        Args:
            entity: L'entite a supprimer.
        """
        self.session.delete(entity)
        self.session.flush()

    def count(self) -> int:
        """Compte le nombre total d'entites.

        Returns:
            Le nombre d'entites presentes en base.
        """
        return self.session.query(self.model).count()
