from database.connection import get_db_connection

def install():
    connection = get_db_connection()

    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS navio (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, capacidade INTEGER NOT NULL, emViagem BOOLEAN NOT NULL DEFAULT 0, tipoNavio TEXT NOT NULL)""")
        
        resposta = connection.execute("SELECT COUNT(*) FROM navio")
        resultado = resposta.fetchone()[0]
        
        if resultado == 0:
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            ("sereia", 2000, True,"cargueiro"))
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            ("concha do mar", 300, False,"Passeio"))
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            ("amélia", 600, False,"Passeio"))
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            ("destruidor de ondas", 2000, True,"cargueiro"))
            connection.execute("""INSERT INTO navio(nome, capacidade, emViagem, tipoNavio) VALUES (?, ?, ?, ?)""",
            ("summer", 350, True,"Passeio"))
            
        connection.commit()
    finally:
        connection.close()
    
    connection = get_db_connection()
  
    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS sobrevivente (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, idade INTEGER NOT NULL, infectado BOOLEAN NOT NULL DEFAULT 0, habilidade TEXT NOT NULL)""")
        
        cursor = connection.execute("SELECT COUNT(*) FROM sobrevivente")
        resultado = cursor.fetchone()[0]
        
        if resultado == 0:
            connection.execute("""INSERT INTO sobrevivente(nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Cruz", 19, False, "Tiro Rápido"))
            connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Gustavo", 20, False, "Corrida Intensa"))
            connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Leh", 20, False, "Hacker"))
            connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Mariazinha", 19, False, "Surfar"))
            connection.execute("""INSERT INTO sobrevivente (nome, idade, infectado, habilidade) VALUES (?, ?, ?, ?)""", ("Joaozinho", 30, False, "Carregamento Rápido"))
        
    
        connection.commit()

    finally:
        connection.close()
    
    
    connection = get_db_connection()

    try:
        connection.execute("""CREATE TABLE IF NOT EXISTS tesouro (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, valor INTEGER NOT NULL, encontrado BOOLEAN NOT NULL DEFAULT 0, raridade TEXT NOT NULL)""")
        respostaTesouro = connection.execute("SELECT COUNT (*) FROM tesouro")
        resultadoTesouro = respostaTesouro.fetchone()[0]
        if resultadoTesouro == 0:
            connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""",
            (tesouro.nome, tesouro.valor, tesouro.encontrado, tesouro.raridade))
        connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""", ('Bau de madeira', 500 , False , 'pouco raro'))
        connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""", ('Bau de ferro', 600 , False , 'medio raro'))
        connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""", ('Bau de cobre', 700 , False , 'bastante raro'))
        connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""", ('Bau de ouro', 800 , False , 'muito raro'))
        connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""", ('Bau de diamante', 900 , False , 'extremamente raro'))
        
    
        connection.commit()
    finally:
        connection.close()

if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")
