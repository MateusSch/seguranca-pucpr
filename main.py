from user import User


def menu():
    while True:
        entrada = int(input("Bem vindo!\n"
                            "1 - Criar usuário\n"
                            "2 - Entrar\n"
                            "3 - Para sair\n"
                            "Digite a opção: "))
        if entrada == 1:
            User.criar_conta()
        elif entrada == 2:
            User.entrar()
        elif entrada == 3:
            break


if __name__ == '__main__':
    menu()
