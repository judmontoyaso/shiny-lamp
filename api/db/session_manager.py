from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from .db_config import get_engine

# Creación de la sesión
Session = sessionmaker(bind=get_engine())

# Gestor de contexto para manejar sesiones
@contextmanager
def session_scope():
    """Proporciona un scope transaccional alrededor de una serie de operaciones."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
