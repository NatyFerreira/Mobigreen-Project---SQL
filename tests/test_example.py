"""
Fichier de test exemple — a adapter a votre schema.

Pour chaque repository cree, ajoutez un fichier tests/test_xxx_repository.py
en suivant la structure ci-dessous.
"""

# TODO: importer votre repository et votre modele
# from mobigreen.repositories.votre_repository import VotreRepository
# from mobigreen.models import VotreModele


class TestExempleRepository:
    """
    Classe de test exemple pour un repository.
    Renommez cette classe et adaptez les tests a votre modele.
    """

    def test_create_et_get_by_id(self, session):
        """Verifie qu'une entite creee est recuperable par son identifiant."""
        # TODO: instancier votre repository avec la session du fixture
        # TODO: creer une instance de votre modele avec des donnees valides
        # TODO: appeler repository.create(entite)
        # TODO: verifier que l'id a ete genere (not None)
        # TODO: recuperer via get_by_id et verifier les attributs
        raise NotImplementedError

    def test_count(self, session):
        """Verifie que count() retourne le bon nombre d'entites."""
        # TODO: creer plusieurs entites
        # TODO: verifier que count() retourne le bon nombre
        raise NotImplementedError

    def test_delete(self, session):
        """Verifie qu'une entite supprimee n'est plus recuperable."""
        # TODO: creer une entite
        # TODO: la supprimer via repository.delete()
        # TODO: verifier que get_by_id retourne None
        raise NotImplementedError

    def test_get_all(self, session):
        """Verifie que get_all() retourne toutes les entites inserees."""
        # TODO: creer plusieurs entites
        # TODO: appeler get_all()
        # TODO: verifier que toutes les entites sont retournees
        raise NotImplementedError
