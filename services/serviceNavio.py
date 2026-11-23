from database.repositoryNavio import CRUDnavio
from entities.navio import Navio

class Services:
    
    def create(self, nome, capacidade, tipoNavio):
        if not nome or not nome.strip():
            raise ValueError("ERRO! Nome não informado.")
        if not capacidade:
            raise ValueError("ERRO! Capacidade não informada.")
        if not tipoNavio or not tipoNavio.strip():
            raise ValueError("ERRO! Tipo do Navio não informado.")
        
        navio = Navio()
        navio.nome = nome.strip()
        navio.capacidade = capacidade
        navio.emViagem = False
        navio.tipoNavio = tipoNavio.strip()
        c = CRUDnavio()
        navio.id = c.create(navio)
        
        return navio
        