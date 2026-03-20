"""
Configuration pytest — Fixtures communes pour les tests.

Ce module fournit l'infrastructure de test via une base SQLite in-memory.
Les tests s'executent sans connexion PostgreSQL.
"""

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mobigreen.models import Base


@pytest.fixture(scope="session")
def engine():
    """Cree un engine SQLite en memoire et genere le schema depuis les modeles ORM.

    Ce fixture ne cree des tables qu'une fois vos modeles declares dans models.py.
    """
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    """Fournit une session SQLAlchemy isolee pour chaque test.

    Chaque test s'execute dans une transaction annulee apres le test (rollback),
    garantissant l'isolation totale entre les tests sans recreer la base.
    """
    connection = engine.connect()
    transaction = connection.begin()
    test_session = Session(bind=connection)
    yield test_session
    test_session.close()
    transaction.rollback()
    connection.close()
