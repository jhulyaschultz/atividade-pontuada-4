import os

os.system("clear") 

ARQUIVO = "funcionarios.csv"


class Funcionario:
    def __init__ (self, nome, cargo, salario, cpf):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.cpf = cpf

    def exibir_dados(self):
        print("\n--- Dados do Funcionário ---")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")


def carregar_dados():
    funcionarios = []
    if (ARQUIVO):
        with open(ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",") 
                cpf, nome, cargo, salario = dados
                funcionario = Funcionario(nome, cargo, salario, cpf)
                funcionarios.append(funcionario)
    return funcionarios


def salvar_dados(funcionarios):
    with open(ARQUIVO, "w") as arquivo:
        for func in funcionarios:
            arquivo.write(f"{func.cpf},{func.nome},{func.cargo},{func.salario}\n") 


def cadastrar_funcionario(funcionarios):
    cpf = input("Digite o CPF do funcionário: ")
    funcionario_existe = False
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionario_existe = True
            break

    if funcionario_existe:
        print("Funcionário com esse CPF já existe.")
        return funcionarios

    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = input("Salário: ")

    funcionario = Funcionario(nome, cargo, salario, cpf)
    funcionarios.append(funcionario)
    print("Funcionário cadastrado com sucesso!")
    return funcionarios


def listar_funcionarios(funcionarios):
    if funcionarios:
        for funcionario in funcionarios:
            funcionario.exibir_dados()
    else:
        print("Nenhum funcionário cadastrado.")


def atualizar_funcionario(funcionarios):
    cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionario.nome = input(f"Novo nome: {funcionario.nome}): ") or funcionario.nome
            funcionario.cargo = input(f"Novo cargo: {funcionario.cargo}): ") or funcionario.cargo
            funcionario.salario = input(f"Novo salário: {funcionario.salario}): ") or funcionario.salario
            print("Dados do funcionário atualizados com sucesso!")
            return funcionarios
    print("Funcionário não encontrado.")
    return funcionarios


def excluir_funcionario(funcionarios):
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    for funcionario in funcionarios:
        if funcionario.cpf == cpf:
            funcionarios.remove(funcionario)
            print("Funcionário excluído.")
            return funcionarios
    print("Funcionário não encontrado.")
    return funcionarios


def menu():
    funcionarios = []  
    while True:
        print("\nMenu DENDÊ TECH:")
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Atualizar Funcionário")
        print("4 - Excluir Funcionário")
        print("5 - Carregar Dados do Arquivo")
        print("6 - Salvar Dados no Arquivo")
        print("7 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcionarios = cadastrar_funcionario(funcionarios)

        elif opcao == "2":
            listar_funcionarios(funcionarios)

        elif opcao == "3":
            funcionarios = atualizar_funcionario(funcionarios)

        elif opcao == "4":
            funcionarios = excluir_funcionario(funcionarios)

        elif opcao == "5":
            funcionarios = carregar_dados()  
            print("Dados carregados do arquivo.")

        elif opcao == "6":
            salvar_dados(funcionarios) 
            print("Dados salvos no arquivo.")

        elif opcao == "7":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()
