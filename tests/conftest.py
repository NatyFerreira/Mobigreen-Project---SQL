import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from mobigreen.models import Base, ZoneMetro, Station, Usager


@pytest.fixture(scope="session")
def engine():
    """Cria um engine SQLite em memória e gera o schema uma única vez."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    return engine


@pytest.fixture
def session(engine):
    """Cria uma sessão isolada para cada teste (rollback após cada teste)."""
    connection = engine.connect()
    transaction = connection.begin()
    test_session = Session(bind=connection)

    try:
        yield test_session
    finally:
        test_session.close()
        transaction.rollback()
        connection.close()


@pytest.fixture
def sample_data(session):
    """Popula a base SQLite com dados mínimos para os testes."""
    # Zona
    z = ZoneMetro(code_insee="38185", nom="Grenoble")
    session.add(z)
    session.flush()

    # Estações
    s1 = Station(
        nom="Victor Hugo",
        latitude=45.18,
        longitude=5.72,
        capacite=20,
        places_dispo=10,
        zone_id=z.zone_id,
    )
    s2 = Station(
        nom="Gare SNCF",
        latitude=45.19,
        longitude=5.71,
        capacite=25,
        places_dispo=5,
        zone_id=z.zone_id,
    )
    session.add_all([s1, s2])

    # Usagers
    u1 = Usager(
        nom="Martin",
        prenom="Alice",
        email="a@test.com",
        type_abonnement="mensuel",
    )
    u2 = Usager(
        nom="Bernard",
        prenom="Lucas",
        email="b@test.com",
        type_abonnement="annuel",
    )
    session.add_all([u1, u2])

    session.commit()

    return {
        "zone": z,
        "stations": [s1, s2],
        "usagers": [u1, u2],
    }
