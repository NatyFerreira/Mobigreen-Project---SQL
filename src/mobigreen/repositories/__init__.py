"""
Package repositories — Couche d'acces aux donnees.

Ce package contient les repositories qui encapsulent les operations
d'acces a la base de donnees pour chaque entite du modele.

Chaque repository herite de BaseRepository et peut ajouter des methodes
metier specifiques a son entite.

Pour creer un nouveau repository :
1. Creez un fichier xxx_repository.py dans ce dossier
2. Importez BaseRepository et votre modele
3. Creez une classe heritant de BaseRepository[VotreModele]
4. Ajoutez vos methodes metier specifiques

Exemple :
    from mobigreen.repositories.base_repository import BaseRepository
    from mobigreen.models import VotreModele

    class VotreRepository(BaseRepository[VotreModele]):
        def __init__(self, session: Session) -> None:
            super().__init__(VotreModele, session)

        def find_by_nom(self, nom: str) -> list[VotreModele]:
            return self.session.query(self.model).filter_by(nom=nom).all()
"""
