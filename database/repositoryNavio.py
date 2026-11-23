from database.connection import get_db_connection()
from entities.navio import Navio

class CRUDnavio:
    
    def create(self, navio):
        connection = get_db_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO navio (nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            (navio.nome, navio.capacidade, navio.emViagem, navio.tipoNavio))
            
            connection.commit()
            
            return cursor.lastrowid
        finally:
            connection.close()