from sqlalchemy import Column, VARCHAR
from .base import Base

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
