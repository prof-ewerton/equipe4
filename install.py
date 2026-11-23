from connection import get_db_connection()

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
        
    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS sobrevivente (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, idade INTEGER NOT NULL, infectado BOOLEAN NOT NULL DEFAULT 0, habilidade TEXT NOT NULL)""")
        
        cursor = connection.execute("SELECT COUNT(*) FROM sobrevivente")
        resultado = cursor.fetchall()[0]
        
        if resultado == 0:
            connection.execute("""INSERT INTO sobrevivente(nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""",
            (sobrevivente.nome, sobrevivente.idade, sobrevivente.infectado, sobrevivente.habilidade))
            
        connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Cruz", 19, False, "Tiro Rápido"))
        connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Gustavo", 20, False, "Corrida Intensa"))
        connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Leh", 20, False, "Hacker"))
        connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Mariazinha", 19, False, "Surfar"))
        connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Joaozinho", 30, False, "Carregamento Rápido"))
        
    
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")
