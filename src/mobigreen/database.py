"""
Gestion de la connexion et des sessions SQLAlchemy.

Ce module fournit :
- engine : le moteur de connexion SQLAlchemy
- SessionLocal : la factory de sessions
- get_session : context manager pour obtenir une session transactionnelle
"""

from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from mobigreen.config import get_database_url

# Creation du moteur de connexion
# pool_pre_ping=True permet de verifier la connexion avant de l'utiliser
engine = create_engine(get_database_url(), pool_pre_ping=True)

# Factory de sessions
# autocommit=False : les transactions doivent etre commitees explicitement
# autoflush=False : pas de flush automatique avant les requetes
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


@contextmanager
def get_session() -> Generator[Session, None, None]:
    """Context manager fournissant une session SQLAlchemy transactionnelle.

    La session est automatiquement commitee en cas de succes,
    ou rollbackee en cas d'exception. Elle est toujours fermee
    a la sortie du bloc with.

    Yields:
        Session: Une session SQLAlchemy prete a l'emploi.

    Example:
        with get_session() as session:
            users = session.query(User).all()
            # commit automatique a la sortie du bloc
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
