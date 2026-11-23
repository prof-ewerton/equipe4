from database.repositorySobrevivente import CRUDsobrevivente
from entities.sobrevivente import Sobrevivente

class Services:
    
    def create(self, nome, idade, habilidade):
        if not nome or not nome.strip():
            raise ValueError("Nome não informado.")
        if not idade or not idade.strip():
            raise ValueError("Idade não informada.")
        if not habilidade or not habilidade.strip():
            raise ValueError("Habilidade não informada.")
        
        sobrevivente = Sobrevivente()
        sobrevivente.nome = nome.strip()
        sobrevivente.idade = idade.strip()
        sobrevivente.infectado = False
        sobrevivente.habilidade = habilidade.strip()
        sobrevivente.id = self.repositorySobrevivente.create(sobrevivente)
        
        return sobrevivente