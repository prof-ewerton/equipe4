class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Sobrevivente", self.menu_entity_one),
            (2, "Entidade Leh", self.menu_entity_two),
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
        print("= Sobrevivente ==")
        while True:
            print("Cadastrar sobrevivente -> 1")
            
            resposta = input("O que deseja fazer? ")
            
            if resposta == 1:
                nome = input("Selecione o nome do sobrevivente a ser cadastrado: ")
                idade = input("Selecione a idade do sobrevivente a ser cadastrado: ")
                habilidade = input("Selecione a habilidade do sobrevivente a ser cadastrado: ")
        
    def menu_entity_two(self):
        print("\n===== TEMA DA EQUIPE =====")
        print("= tema do estudante ==")
        
    def menu_entity_three(self):
        print("\n===== TEMA DA EQUIPE =====")
        print("= tema do estudante ==")