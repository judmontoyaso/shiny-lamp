from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, VARCHAR, Float, BIGINT, Integer



# Creación de MetaData y Declarative Base
metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Taxonomy(Base):
    __tablename__ = 'taxonomy'

    otu = Column(VARCHAR(80), primary_key=True)
    species = Column(VARCHAR(80))
    genus = Column(VARCHAR(80))
    family = Column(VARCHAR(80))
    order = Column(VARCHAR(80))
    tclass = Column(VARCHAR(80))
    phylum = Column(VARCHAR(80))
    kingdom = Column(VARCHAR(80))

    # Redshift-specific options
    __table_args__ = {'redshift_diststyle': 'KEY', 'redshift_distkey': 'otu', 'redshift_sortkey': 'otu'}
    


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
    
    
class Kit(Base):
    __tablename__ = 'kit'

    kitId = Column(VARCHAR(20), primary_key=True)
    projectId = Column(VARCHAR(20))
    age = Column(VARCHAR(100))
    treatment = Column(VARCHAR)
    treatmentNumber = Column(BIGINT)
    client = Column(VARCHAR(100))

    __table_args__ = {'redshift_diststyle': 'KEY', 'redshift_distkey': 'kitId', 'redshift_sortkey': 'kitId'}
    


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