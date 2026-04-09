# scripts/delete_user.py

from mobigreen.database import SessionLocal
from mobigreen.models import Usager, UsagerPseudo, Trajet, Incident

def delete_user(user_id: int):
    session = SessionLocal()

    # 1. Remover dados pessoais
    user = session.query(Usager).filter(Usager.usr_id == user_id).first()
    if user:
        session.delete(user)

    # 2. Remover pseudônimo
    pseudo = session.query(UsagerPseudo).filter(UsagerPseudo.usager_id == user_id).first()
    if pseudo:
        session.delete(pseudo)

    # 3. Anonimizar trajetos (usr_id → NULL)
    session.query(Trajet).filter(Trajet.usr_id == user_id).update(
        {Trajet.usr_id: None}
    )

    # 4. Anonimizar incidentes (usr_id → NULL)
    session.query(Incident).filter(Incident.usr_id == user_id).update(
        {Incident.usr_id: None}
    )

    session.commit()
    print("Suppression de l’usager effectuée conformément au RGPD.")

if __name__ == "__main__":
    delete_user(12)  # Exemplo
