import msvcrt


def cadastro(id):
    print("\n\tCRIAR CADASTRO\n")

    id = id
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")

    while True:
        cpf = input("Digite o CPF (apenas numeros): ")
        if cpf == "X":
            cpf = ""
            break

        if check_cpf(cpf):
            break
    return [id, nome, idade, email, cpf]


def check_cpf(cpf):
    if not cpf.isnumeric():
        print("CPF Invalido")
        return False

    if not len(cpf) == 11:
        print("CPF Invalido")
        return False

    return cpf_dv(cpf)


def cpf_dv(cpf, return_dv=False):
    cont = 10
    cpf_9d = cpf[0:9]
    sum = 0

    for d in cpf_9d:
        sum = sum + int(d) * cont
        cont = cont - 1

    dv_1 = 11 - sum % 11

    def cpf_dv_1():
        if dv_1 >= 10:
            return "0"
        else:
            return str(dv_1)

    cont = 11
    cpf_10d = cpf_9d + str(cpf_dv_1())
    sum = 0

    for d in cpf_10d:
        sum = sum + int(d) * cont
        cont = cont - 1

    dv_2 = 11 - sum % 11

    def cpf_dv_2():
        if dv_2 >= 10:
            return "0"
        else:
            return str(dv_2)

    if return_dv:
        return cpf + cpf_dv_1() + cpf_dv_2()

    if cpf[9] == cpf_dv_1() and cpf[10] == cpf_dv_2():
        print("CPF Valido")
        return front_cpf(cpf)
    else:
        print("CPF Invalido")
        return False


def front_cpf(cpf):
    if cpf != "":
        cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
        return cpf
    else:
        return cpf


def imprime(data):
    print(
        f"\n\t DADOS CADASTRADOS\
          \n\
          \nID: {data[0]}\
          \nNome: {data[1]}\
          \nIdade: {data[2]}\
          \nEmail: {data[3]}\
          \nCPF: {data[4]}\
          \n"
    )


def capturar_espaco(db):
    print("Pressione <ESPACO> para cadastrar outro dado ou <ENTER> para continuar...")
    while True:
        tecla = msvcrt.getch().decode("utf-8")
        if tecla == " ":
            data = cadastro(len(db) + 1)
            imprime(data)
            db.append(data)
            salvar(db)
            print("Pressione <ESPACO> para cadastrar outro dado ou <ENTER> para continuar...")
        else:
            # main.main(db)
            return False
        
def salvar(db):
    salvar = input('\nCONFIRMAR CADASTRO:\
                   \n\
                   \n\t1 - Sim\
                   \n\t2 - Cancelar\
                   \n')
    
    if salvar == '1':
        salvarDados(db)
        print("\nDADOS CADASTRADOS COM SUCESSO!")
    else:
        print('CADASTRO CANCELADO PELO USUARIO!')

def salvarDados(db):
    arquivo = open('banco_dados.csv', 'a')
    for l in db:
        banco = f"{l[0]},{l[1]},{l[2]},{l[3]},{l[4]}\n"
    arquivo.write(banco)