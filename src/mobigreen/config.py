"""
Configuration du package mobigreen.

Charge les variables d'environnement depuis le fichier .env
et expose les parametres de configuration.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Charger le fichier .env depuis la racine du projet
_project_root = Path(__file__).resolve().parent.parent.parent
load_dotenv(_project_root / ".env")


def get_database_url() -> str:
    """Retourne l'URL de connexion a la base de donnees.

    L'URL est lue depuis la variable d'environnement DATABASE_URL.

    Returns:
        str: URL de connexion PostgreSQL au format SQLAlchemy.

    Raises:
        ValueError: Si la variable DATABASE_URL n'est pas definie.
    """
    database_url = os.getenv("DATABASE_URL")
    if database_url is None:
        raise ValueError(
            "La variable d'environnement DATABASE_URL n'est pas definie. "
            "Copiez le fichier .env.example en .env et renseignez vos identifiants."
        )
    return database_url
