from database.connection import get_db_connection()
from entities.tesouro import Tesouro

class CrudTesouro:
        def create(self, tesouro):
            
        connection = get_db_connection()
        try:
            cursor = connection.execute("INSERT INTO tesouro (nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)",(tesouro.nome, tesouro.valor, tesouro.encontrado, tesouro.raridade))            
            connection.commit()
            
            return cursor.lastrowid
        finally:
            connection.close()
