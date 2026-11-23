from database.connection import get_db_connection

def install():
    connection = get_db_connection()

    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS navio (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, capacidade INTEGER NOT NULL, emViagem BOOLEAN NOT NULL DEFAULT 0, tipoNavio TEXT NOT NULL)""")
        
        resposta = connection.execute("SELECT COUNT(*) FROM navio")
        resultado = resposta.fetchall()[0]
        
        if resultado == 0:
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            (navio.nome, navio.capacidade, navio.emViagem, navio.tipoNavio))
        
    
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")
