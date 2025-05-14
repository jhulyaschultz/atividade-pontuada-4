import os
from dataclasses import dataclass

os.system ("clear")

@dataclass
class Funcionario:
    nome: str
    cargo: str
    salario: str
    cpf: str

    def exibir_dados(self):
        print("\n--- Dados do Funcionário ---")
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario}")


def menu():
    funcionarios = []

    while True:
        print("\nMenu DENDÊ TECH:")
        print("1 - Cadastrar Funcionário")
        print("2 - Listar Funcionários")
        print("3 - Atualizar Funcionário")
        print("4 - Excluir Funcionário")
        print("5 - Sair")
    
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cpf = input("Digite o CPF do funcionário: ")
            funcionario_existe = False
            for funcionario in funcionarios:
                if funcionario.cpf == cpf:
                    funcionario_existe = True
                    break

            if funcionario_existe:
                print("Funcionário com esse CPF já existe.")
                continue

            nome = input("Nome: ")
            cargo = input("Cargo: ")
            salario = input("Salário: ")

            funcionario = Funcionario(nome, cargo, salario, cpf)
            funcionarios.append(funcionario)
            print("Funcionário cadastrado com sucesso!")

        elif opcao == "2":
            if funcionarios:
                for funcionario in funcionarios:
                    funcionario.exibir_dados()
            else:
                print("Nenhum funcionário cadastrado.")

        elif opcao == "3":
            cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
            for funcionario in funcionarios:
                if funcionario.cpf == cpf:
                    funcionario.nome = input(f"Novo nome: {funcionario.nome}): ") or funcionario.nome
                    funcionario.cargo = input(f"Novo cargo: {funcionario.cargo}): ") or funcionario.cargo
                    funcionario.salario = input(f"Novo salário: {funcionario.salario}): ") or funcionario.salario
                   
                    break
            else:
                print("Funcionário não encontrado.")

        elif opcao == "4":
            cpf = input("Digite o CPF do funcionário que deseja excluir: ")
            for funcionario in funcionarios:
                if funcionario.cpf == cpf:
                    funcionarios.remove(funcionario)
                    print("Funcionário excluído.")
                    break    

        elif opcao == "5":
                print("Encerrando o sistema.")
                break

        else:
                print("Opção inválida. Tente novamente.")

menu()

