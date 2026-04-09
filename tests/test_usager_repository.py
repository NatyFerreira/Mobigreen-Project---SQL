# tests/test_usager_repository.py

from mobigreen.repositories.usager_repository import UsagerRepository

def test_get_by_email(session, sample_data):
    repo = UsagerRepository(session)
    u = repo.get_by_email("a@test.com")
    assert u is not None

def test_get_by_abonnement(session, sample_data):
    repo = UsagerRepository(session)
    users = repo.get_by_abonnement("mensuel")
    assert len(users) == 1