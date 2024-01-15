import pandas as pd
from .session_manager import session_scope
from ..models.microbiome import Microbiome
from ..models.taxonomy import Taxonomy

# Consultas
def query_taxonomy(limit=100):
    """Consulta a la tabla Taxonomy con un límite especificado."""
    with session_scope() as session:
        query = session.query(Taxonomy).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')

def query_microbiome(limit=100):
    """Consulta a la tabla Microbiome con un límite especificado."""
    with session_scope() as session:
        query = session.query(Microbiome).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
