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
        
        connection.execute("""CREATE TABLE IF NOT EXISTS tesouro (id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL, valor INTEGER NOT NULL, encontrado BOOLEAN NOT NULL DEFAULT 0, raridade TEXT NOT NULL)""")
        respostaTesouro = connection.execute("SELECT COUNT (*) FROM tesouro")
        resultadoTesouro = resposta.fetchall()[0]
        if resultadoTesouro == 0:
            connection.execute("""INSERT INTO tesouro(nome, valor, encontrado, raridade) VALUES (?, ?, ?, ?)""",
            (tesouro.nome, tesouro.valor, tesouro.encontrado, tesouro.raridade))
    
        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    install()
    print("Banco de dados instalado com sucesso.")
