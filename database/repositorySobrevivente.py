from database.connection import get_db_connection
from entities.sobrevivente import Sobrevivente

class CRUDsobrevivente:
    
    def create(self, sobrevivente):
        connection = get_db_connection()
        
        try:
            cursor = connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""",
            (sobrevivente.nome, sobrevivente.idade, sobrevivente.infectado))
            
            connection.commit()
            
            return cursor.lastrowid
        finally:
            connection.close()