import hashlib
import block


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
            User.cria_hash(criar_senha)

    @staticmethod
    def entrar():
        arquivo = open("dados.txt", "r")
        nameusers = []
        senhausers = []
        for linha in arquivo:
            nameusers.append(linha.strip().split(',')[0])
            senhausers.append(linha.strip().split(',')[1])
        arquivo.close()
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
                block.bloquear(tempo)
                tentativas = 0
                tempo = tempo + 30

    @staticmethod
    def cria_hash(senha):
        arquivo = open("hash.txt", "r")
        senhausers = 0
        for linha in arquivo:
            senhausers = int(linha.strip().split(':')[0]) + 1
        arquivo.close()
        with open("hash.txt", "a") as arquivo_hash:
            hash_senha = str(hashlib.md5(senha.encode()).hexdigest())
            arquivo_hash.writelines(f"{senhausers}:{hash_senha}\n")
        arquivo_hash.close()
