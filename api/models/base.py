from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base



# Creación de MetaData y Declarative Base
metadata = MetaData()
Base = declarative_base(metadata=metadata)
