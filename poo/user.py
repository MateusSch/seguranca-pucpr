import hashlib
import time
import sys


class User:

    def __init__(self, login, senha):
        self.__login = login
        self.__senha = senha

    @property
    def login(self):
        return self.__login

    @property
    def senha(self):
        return self.__senha

    @staticmethod
    def criar_conta():
        print("\n*** O usuário e a senha deve ter no máximo 4 caracteres ***\n")
        criar_login = input("Criar login: ")
        criar_senha = input("Criar senha: ")
        if len(criar_login) > 4 or len(criar_senha) > 4:
            print("\nTente criar novamente!")
            User.criar_conta()
        else:
            conta = User(criar_login, criar_senha)
            with open("dados.txt", "a") as arquivo:
                arquivo.write(f"{conta.login},{conta.senha}\n")
            arquivo.close()
            User.cria_hash()

    @staticmethod
    def entrar():
        arquivo = open("dados.txt", "r")
        usuarios = []
        for linha in arquivo:
            usuarios.append(linha.strip().split(','))
        arquivo.close()

        nameusers = []
        senhausers = []
        for i in usuarios:
            nameusers.append(i[0])
            senhausers.append(i[1])

        check = False
        tentativas = 0
        tempo = 31
        while True:
            entrar_login = input("\nDigite o login: ")
            entrar_senha = input("Digite a senha: ")
            try:
                k = 0
                while True:
                    if entrar_login == nameusers[k]:
                        try:
                            j = 0
                            while True:
                                if entrar_senha == senhausers[j]:
                                    print(f"\n*** Bem vindo {entrar_login.title()} ***")
                                    check = True
                                    break
                                else:
                                    j = j + 1
                        except IndexError:
                            print("\nLogin ou senha incorretos!")
                            tentativas = tentativas + 1
                        break
                    else:
                        k = k + 1
            except IndexError:
                print("\nLogin ou senha incorretos!")
                tentativas = tentativas + 1
            if check:
                break
            elif tentativas == 3:
                for t in range(0, tempo):
                    sys.stdout.write(f"\rTempo de espera: {t} seg")
                    sys.stdout.flush()
                    time.sleep(1)
                tentativas = 0
                tempo = tempo + 30

    @staticmethod
    def cria_hash():
        arquivo = open("dados.txt", "r")
        usuarios = []
        for linha in arquivo:
            usuarios.append(linha.strip().split(','))
        arquivo.close()

        senhausers = []
        for i in usuarios:
            senhausers.append(i[1])

        arquivo_hash = open("hash.txt", "a")
        k = 1
        for senha in senhausers:
            senha_bit = senha.encode()
            hash_senha = str(hashlib.md5(senha_bit).hexdigest())
            arquivo_hash.write(f"{k}:{hash_senha}\n")
            k = k + 1
        arquivo_hash.close()
