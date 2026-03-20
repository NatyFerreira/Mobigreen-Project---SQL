"""
Modeles ORM SQLAlchemy — MobiGreen Urban.

Ce fichier definit les classes Python representant les tables de votre base de donnees.
Chaque classe correspond a une table et herite de la classe Base.

=============================================================================
GUIDE DE CREATION D'UN MODELE ORM (SQLAlchemy 2.0)
=============================================================================

1. DECLARATION D'UNE CLASSE MODELE
----------------------------------
Chaque table est representee par une classe qui herite de Base.
Le nom de la table est defini par l'attribut __tablename__.

    class MaTable(Base):
        __tablename__ = "ma_table"  # Nom exact de la table en base


2. DECLARATION DES COLONNES
---------------------------
Utilisez Mapped[type] pour declarer le type Python et mapped_column() pour
les options de la colonne.

    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(100), nullable=False)
    actif: Mapped[bool] = mapped_column(Boolean, default=True)


3. CORRESPONDANCE DES TYPES SQL -> SQLAlchemy
---------------------------------------------
    SQL                         SQLAlchemy              Python
    -----------------------------------------------------------------
    VARCHAR(n), TEXT            String(n), Text         str
    INTEGER, SERIAL             Integer                 int
    SMALLINT                    SmallInteger            int
    BIGINT                      BigInteger              int
    DOUBLE PRECISION            Float                   float
    DECIMAL(p,s), NUMERIC(p,s)  Numeric(p,s)            Decimal
    BOOLEAN                     Boolean                 bool
    DATE                        Date                    date
    TIME                        Time                    time
    TIMESTAMP                   DateTime                datetime
    TIMESTAMP WITH TIME ZONE    TIMESTAMP(timezone=True) datetime (avec tzinfo)

    Pour TIMESTAMP WITH TIME ZONE, importez depuis le dialect PostgreSQL :
        from sqlalchemy.dialects.postgresql import TIMESTAMP
        created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))


4. CLE PRIMAIRE AUTO-INCREMENTEE (SERIAL)
-----------------------------------------
    id: Mapped[int] = mapped_column(primary_key=True)
    # SQLAlchemy gere automatiquement l'auto-increment pour les cles primaires


5. CLE ETRANGERE ET RELATION
----------------------------
Pour une relation Many-to-One (ex: plusieurs locations pour un vehicule) :

    # Dans la table "location"
    vehicule_id: Mapped[int] = mapped_column(ForeignKey("vehicule.id"))
    vehicule: Mapped["Vehicule"] = relationship(back_populates="locations")

    # Dans la table "vehicule"
    locations: Mapped[list["Location"]] = relationship(back_populates="vehicule")

Note : utilisez des guillemets autour du nom de classe si elle n'est pas
encore definie (forward reference).


6. METHODE __repr__
-------------------
Implementez __repr__ pour faciliter le debogage :

    def __repr__(self) -> str:
        return f"<MaTable(id={self.id}, nom={self.nom!r})>"


7. DOCUMENTATION OFFICIELLE
---------------------------
SQLAlchemy 2.0 ORM Quick Start :
    https://docs.sqlalchemy.org/en/20/orm/quickstart.html

SQLAlchemy Column and Data Types :
    https://docs.sqlalchemy.org/en/20/core/type_basics.html

=============================================================================
"""

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, SmallInteger, BigInteger, Float, Numeric
from sqlalchemy import Boolean, Date, Time, DateTime, Text, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP


class Base(DeclarativeBase):
    """Classe de base pour tous les modeles ORM du projet."""
    pass


# =============================================================================
# TODO: Declarez vos modeles ORM ci-dessous
# =============================================================================
#
# Pour chaque table de votre schema mobigreen_urban :
# 1. Creez une classe heritant de Base
# 2. Definissez __tablename__ avec le nom exact de la table
# 3. Declarez chaque colonne avec Mapped[type] et mapped_column()
# 4. Ajoutez les cles etrangeres et relations si necessaire
# 5. Implementez __repr__ pour faciliter le debogage
#
# Exemple minimal (a remplacer par vos propres tables) :
#
#     class Exemple(Base):
#         __tablename__ = "exemple"
#
#         id: Mapped[int] = mapped_column(primary_key=True)
#         nom: Mapped[str] = mapped_column(String(100), nullable=False)
#
#         def __repr__(self) -> str:
#             return f"<Exemple(id={self.id}, nom={self.nom!r})>"
#
# =============================================================================
