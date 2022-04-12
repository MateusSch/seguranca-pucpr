from user import User


def menu():
    while True:  # Volta sempre pro menu
        try:
            entrada = int(input("\nBem vindo!\n"
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
        except ValueError:
            print("\nNão é um número inteiro o que você digitou, tente novamente!")


if __name__ == '__main__':
    menu()
