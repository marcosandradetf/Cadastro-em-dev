import utils as ut
import random


def main(db):
    while True:
        print(
            "\n\tCADASTRO DE PESSOAS\
          \n\
          \n1 - CADASTRO\
          \n2 - IMPRIMIR BANCO DE DADOS\
          \n3 - GERAR CPF\
          \n0 - SAIR\
          \n"
        )
        opt = input("Digite a opcao desejada: ")
        if opt == "1" or opt == "2" or opt == "3":
            print(f"\nOPCAO {opt} SELECIONADA")

        if opt == "1":
            print(
                "\n\tCADASTRO\
          \n\
          \n1 - INICIAR CADASTRO\
          \n2 - VOLTAR\
          \n"
            )
            opt = input("Digite a opcao desejada: ")
            while True:
                if opt == "1":
                    data = ut.cadastro(len(db) + 1)
                    ut.imprime(data)
                    db.append(data)
                    ut.salvar(db)
                    ut.capturar_espaco(db)
                    break
                elif opt == "2":
                    break

        elif opt == "2":
            if len(db) > 0:
                while True:
                    print(
                        "\n\
                  \n\tEscolha a opcao\
                  \n1 - Exibir um registro especifico\
                  \n2 - Exibir todos os dados\
                  \n3 - Voltar ao menu anterior\
                  \n"
                    )
                    opt = input("Digite a opcao: ")

                    if opt == "1":
                        id = int(input("Digite o ID do registro: "))
                        if id <= len(db):
                            ut.imprime(db[id - 1])
                        input("Pressione <ENTER> para continuar...")
                    elif opt == "2":
                        print("/tTODOS OS DADOS")
                        for d in db:
                            ut.imprime(d)
                        input("Pressione <ENTER> para continuar...")
                    elif opt == "3":
                        break
                    else:
                        print("OPCAO INVALIDA")
            else:
                print(
                    "\n\tIMPRIMIR BANCO DE DADOS\
                \n\
                \nNENHUM REGISTRO ENCONTRADO!\
                \n"
                )
                input("Pressione <ENTER> para voltar...")
        elif opt == "3":
            print("\nCPF Gerado")
            cpf = ""
            for _ in range(9):
                digitos = random.randint(0, 9)
                cpf += str(digitos)
            gerado = ut.cpf_dv(cpf, return_dv=True)
            print(gerado + "\n")
            input("Pressione <ENTER> para voltar...")

        elif opt == "0":
            print("ENCERRANDO SISTEMA...")
            break
        else:
            print("\nOPCAO INVALIDA!")


dataset = []

if __name__ == "__main__":
    main(dataset)