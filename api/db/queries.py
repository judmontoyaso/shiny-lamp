import pandas as pd
from .session_manager import session_scope
from ..models.base import Microbiome, Taxonomy, FeatureCountExtendedView

# Consultas
def get_taxonomy_all(limit=100):
    """Consulta a la tabla Taxonomy con un límite especificado."""
    with session_scope() as session:
        query = session.query(Taxonomy).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')

def get_microbiome_all(limit=100):
    """Consulta a la tabla Microbiome con un límite especificado."""
    with session_scope() as session:
        query = session.query(Microbiome).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
    

def get_microbiome_by_runid(run_id=None, limit=100):
    """Consulta a la tabla Microbiome con un límite especificado y opcionalmente filtra por runId."""
    with session_scope() as session:
        # Iniciar la consulta
        query = session.query(Microbiome)

        # Filtrar por runId si se proporciona
        if run_id:
            query = query.filter(Microbiome.runId == run_id)

        # Aplicar el límite
        query = query.limit(limit)

        # Ejecutar la consulta y convertir el resultado en un diccionario
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
    
    
def get_featureCountExtendedView_all(limit=100):
    """Consulta a la tabla FeatureCountExtendedView con un límite especificado y opcionalmente filtra por runId."""
    with session_scope() as session:
        query = session.query(FeatureCountExtendedView).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
    
    
def get_featureCountExtendedView_by_project_id(project_id=None, limit=100):
    """Consulta a la tabla Microbiome con un límite especificado y opcionalmente filtra por runId."""
    with session_scope() as session:
        # Iniciar la consulta
        query = session.query(FeatureCountExtendedView)

        # Filtrar por runId si se proporciona
        if project_id:
            query = query.filter(FeatureCountExtendedView.projectId == project_id)

        # Aplicar el límite
        query = query.limit(limit)

        # Ejecutar la consulta y convertir el resultado en un diccionario
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
    
    
def get_projectid_all(limit=100):
    """Consulta a la tabla FeatureCountExtendedView con un límite especificado y opcionalmente filtra por runId."""
    with session_scope() as session:
        query = session.query(FeatureCountExtendedView.projectId).limit(limit)
        df = pd.read_sql(query.statement, session.bind)
        return df.to_dict(orient='records')
    