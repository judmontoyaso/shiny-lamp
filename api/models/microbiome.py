from sqlalchemy import Column, VARCHAR, Float
from .base import Base

class Microbiome(Base):
    __tablename__ = 'microbiome'

    sampleId = Column(VARCHAR(12), primary_key=True)
    fullSampleId = Column(VARCHAR(12))
    kitId = Column(VARCHAR(20))
    runId = Column(VARCHAR(20))
    animalId = Column(VARCHAR(20))
    sampleLocation = Column(VARCHAR(14))
    alphaShannon = Column(Float)
    alphaObserved = Column(Float)

    __table_args__ = {'redshift_diststyle': 'KEY', 'redshift_distkey': 'sampleId', 'redshift_sortkey': 'sampleId'}