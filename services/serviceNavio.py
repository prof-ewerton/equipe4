from database.repositoryNavio import CRUDnavio
from entities.navio import Navio

class Services:
    
    def create(self, nome, capacidade, tipoNavio):
        if not nome or not nome.strip():
            raise ValueError("ERRO! Nome não informado.")
        if not capacidade or not capacidade.strip():
            raise ValueError("ERRO! Capacidade não informada.")
        if not tipoNavio or not tipoNavio.strip():
            raise ValueError("ERRO! Tipo do Navio não informado.")
        
        navio = Navio()
        navio.nome = nome.strip()
        navio.capacidade = capacidade.strip()
        navio.emViagem = False
        navio.tipoNavio = tipoNavio.strip()
        navio.id = self.repositoryNavio.create(navio)
        
        return navio
        