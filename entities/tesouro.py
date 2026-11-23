class Tesouro:
    def __init__(self, nome, valor, encontrado=False, id=None):
        self.id = id
        self.nome = nome
        self.valor = valor
        self.encontrado = encontrado