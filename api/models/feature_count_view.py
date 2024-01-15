from sqlalchemy import Column, VARCHAR, Float, Integer
from .base import Base

class FeatureCountExtendedView(Base):
    __tablename__ = 'feature_count_view'

    sampleId = Column(VARCHAR, primary_key=True)
    value = Column(Float)
    otu = Column(VARCHAR)
    kitId = Column(VARCHAR)
    runId = Column(VARCHAR)
    sampleLocation = Column(VARCHAR)
    alphaShannon = Column(Float)
    alphaObserved = Column(Float)
    projectId = Column(VARCHAR)
    age = Column(VARCHAR)
    treatment = Column(VARCHAR)
    treatmentNumber = Column(Integer)
    client = Column(VARCHAR)
    animalId = Column(VARCHAR)
    animalType = Column(VARCHAR)
    animalNumber = Column(Integer)
    species = Column(VARCHAR)
    genus = Column(VARCHAR)
    family = Column(VARCHAR)
    order = Column(VARCHAR)
    class_ = Column('class', VARCHAR)  # 'class' is a reserved keyword in Python, hence the underscore
    phylum = Column(VARCHAR)
    kingdom = Column(VARCHAR)

    # No specific distribution or sort key is provided, so you might want to add them if necessary
