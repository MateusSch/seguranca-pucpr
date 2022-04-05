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
        criar_login = input("Criar login: ")
        criar_senha = input("Criar senha: ")
        conta = User(criar_login, criar_senha)
        with open("dados.txt", "w") as arquivo:
            arquivo.write(f"{conta.login}\n")
            arquivo.write(f"{conta.senha}")
        arquivo.close()

    @staticmethod
    def entrar():
        arquivo = open("dados.txt", "r")
        usuario = []
        for linha in arquivo:
            linha = linha.strip()
            usuario.append(linha)
        arquivo.close()
        entrar_login = input("Digite o login: ")
        entrar_senha = input("Digite a senha: ")

        if entrar_login == usuario[0] and entrar_senha == usuario[1]:
            print(f"***Bem vindo {entrar_login.title()}***")
        else:
            print("Usuário ou senha incorretos, tente novamente")
            User.entrar()
