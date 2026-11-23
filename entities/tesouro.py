class Tesouro:
    def __init__(self, nome, valor, encontrado=False, raridade, id=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.encontrado = encontrado
        self.raridade = raridade