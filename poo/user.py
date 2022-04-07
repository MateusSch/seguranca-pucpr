import hashlib


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
            with open("dados.txt", "w") as arquivo:
                arquivo.write(f"{conta.login}\n")
                arquivo.write(f"{conta.senha}")
            arquivo.close()
            User.cria_hash()

    @staticmethod
    def entrar():
        arquivo = open("dados.txt", "r")
        usuario = []
        for linha in arquivo:
            linha = linha.strip()
            usuario.append(linha)
        arquivo.close()
        entrar_login = input("\nDigite o login: ")
        entrar_senha = input("Digite a senha: ")

        if entrar_login == usuario[0] and entrar_senha == usuario[1]:
            print(f"\n*** Bem vindo {entrar_login.title()} ***")
        else:
            print("\nUsuário ou senha incorretos, tente novamente!")
            User.entrar()

    @staticmethod
    def cria_hash():
        arquivo = open("dados.txt", "r")
        usuario = []
        for linha in arquivo:
            linha = linha.strip()
            usuario.append(linha)
        arquivo.close()
        senha_bit = usuario[1].encode()
        arquivo_hash = open("hash.txt", "w")
        hash_senha = str(hashlib.md5(senha_bit).hexdigest())
        arquivo_hash.writelines(hash_senha)
        arquivo_hash.close()
