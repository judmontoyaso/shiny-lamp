import os
from sqlalchemy.engine.url import URL
import sqlalchemy as sa
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Configuración de la conexión a la base de datos
def get_engine():
    url = URL.create(
        drivername=os.getenv('DB_DRIVER'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        username=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    engine = sa.create_engine(url)
    return engine
