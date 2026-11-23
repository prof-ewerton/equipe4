from database.repositoryTesouro import CrudTesouro
from entities.tesouro import Tesouro

class Service:
    def create(self, nome, valor, raridade):
        if not nome or not nome.strip():
            raise ValueError("Nome não enviado")
        if not valor or not valor.strip():
            raise ValueError("Valor não enviado")
        if not raridade or not raridade.strip():
            raise ValueError("Raridade não enviada")
        
        tesouro = Tesouro()
        tesouro.nome = nome.strip()
        tesouro.valor = valor.strip()
        tesouro.encontrado = False
        tesouro.raridade raridade.strip()
        tesouro.id = self.repositoryTesouro.create(tesouro)
        
        return tesouro
