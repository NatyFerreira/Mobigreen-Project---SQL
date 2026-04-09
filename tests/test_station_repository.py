 # tests/test_station_repository.py

from mobigreen.repositories.station_repository import StationRepository

def test_get_by_zone(session, sample_data):
    repo = StationRepository(session)
    stations = repo.get_by_zone("38185")
    assert len(stations) == 2

def test_get_disponibles(session, sample_data):
    repo = StationRepository(session)
    stations = repo.get_disponibles(nb_places_min=6)
    assert len(stations) == 1
