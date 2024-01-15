from sqlalchemy import Column, VARCHAR, BIGINT
from .base import Base

class Kit(Base):
    __tablename__ = 'kit'

    kitId = Column(VARCHAR(20), primary_key=True)
    projectId = Column(VARCHAR(20))
    age = Column(VARCHAR(100))
    treatment = Column(VARCHAR)
    treatmentNumber = Column(BIGINT)
    client = Column(VARCHAR(100))

    __table_args__ = {'redshift_diststyle': 'KEY', 'redshift_distkey': 'kitId', 'redshift_sortkey': 'kitId'}
