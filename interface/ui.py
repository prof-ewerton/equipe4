from services.serviceNavio import Services
class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Sobrevivente", self.menu_entity_one),
            (2, "Navio", self.menu_entity_two),
            (3, "Entidade Gusta", self.menu_entity_three),
        ]

    def show(self):
        while True:
            print("\n===== Naufrágio =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_entity_one(self):
        print("\n===== Naufrágio =====")
        print("= sobrevivente ==")
        while True:
            print("Cadastrar sobrevivente -> 1")
            
            resposta = input("O que deseja fazer? ")
        
    def menu_entity_two(self):
        print("\n===== Naufrágio =====")
        print("= Navio ==")
        nome = input("Digite o nome do Navio: ")
        capacidade = int(input("Digite a capacidade do navio(KG): "))
        tipoNavio = input("Digite o tipo do Navio: ")
        
        try:
            navio = self.serviceNavio.create(nome, capacidade, tipoNavio)
            print(f"CADASTRADO COM SUCESSO => ID = {navio.id}")
            if navio.emViagem:
                confirma = "SIM"
            else:
                confirma = "NÃO"
            print(f"NOME: {navio.nome}// CAPACIDADE: {navio.capacidade} // TIPO: {navio.tipo} // EM VIAGEM? {confirma}")
        
        except:
            raise ValueError("Ocorreu algum erro, tente novamente...")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    def menu_entity_three(self):
        print("\n===== TEMA DA EQUIPE =====")
        print("= tema do estudante ==")