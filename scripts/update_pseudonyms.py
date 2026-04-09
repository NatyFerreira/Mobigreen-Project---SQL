from mobigreen.database import SessionLocal
from mobigreen.models import Usager, UsagerPseudo
from sqlalchemy import select
from uuid import uuid4

def update_pseudonyms():
    session = SessionLocal()

    try:
        usagers = session.execute(select(Usager)).scalars().all()

        for u in usagers:
            pseudo = session.get(UsagerPseudo, u.usr_id)

            if pseudo is None:
                new_pseudo = UsagerPseudo(
                    usager_id=u.usr_id,
                    usager_pseudo_id=uuid4()
                )
                session.add(new_pseudo)
                print(f"Gerado pseudônimo para usr_id={u.usr_id}")

        session.commit()
        print("Pseudonymes mis à jour avec succès.")

    except Exception as e:
        session.rollback()
        print("Erro:", e)

    finally:
        session.close()


if __name__ == "__main__":
    update_pseudonyms()
