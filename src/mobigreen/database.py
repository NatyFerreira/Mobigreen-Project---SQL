from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from mobigreen.config import settings
from contextlib import contextmanager

engine = create_engine(settings.DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
