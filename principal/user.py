import hashlib
import block


class User:
    def __init__(self, login, senha):  # Função construtura
        self.__login = login
        self.__senha = senha

    @property  # Get login
    def login(self):
        return self.__login

    @property  # Get senha
    def senha(self):
        return self.__senha

    @staticmethod
    def criar_conta():
        """
        Cria um usuário com até 4 caracteres no login e na senha, não aceita mais do que isso.
        Depois salva o login e a senha em um arquivo txt. E chama a função criar_hash, passando a senha como parâmetro.
        """
        print("\n*** O usuário e a senha deve ter no máximo 4 caracteres ***\n")
        criar_login = input("Criar login: ")
        criar_senha = input("Criar senha: ")
        if len(criar_login) > 4 or len(criar_senha) > 4:  # Verifica o tamanho do login e da senha
            print("\nTente criar novamente!")
            User.criar_conta()
        else:
            conta = User(criar_login, criar_senha)   # Chama a função construtora
            with open("dados.txt", "a") as arquivo:  # Salva os dados em um arquivo txt, separando eles por uma vírgula
                arquivo.write(f"{conta.login},{conta.senha}\n")
            arquivo.close()
            User.cria_hash(criar_senha)  # Chama a função de criar hash, passando somente a senha como parâmetro

    @staticmethod
    def separa_dados():
        """
        Cria duas listas, uma de logins e outra de senhas.

        :return: Uma tupla com as listas de logins e senhas
        """
        arquivo = open("dados.txt", "r")
        nameusers = []
        senhausers = []
        for linha in arquivo:
            nameusers.append(linha.strip().split(',')[0])
            senhausers.append(linha.strip().split(',')[1])
        arquivo.close()
        return nameusers, senhausers

    @staticmethod
    def entrar():
        """
        Chama a função separa_dados e salva em duas listas, e a partir disso faz a verificação.
        Se o input de login for compatível com algum da lista, ele vai verificar se o input da senha é compatível com o
        login. Senão existir o login ou a senha não for correta, conta como uma tentativa errada. Com 3 tentativas
        erradas chama a função bloquear, assim fica suspenso por um determinado tempo a possibilidade de entrar.
        Se errar mais 3 vez vai aumentando o tempo, só possível sair até acertar o login e senha.
        """
        nameusers = User.separa_dados()[0]  # Lista com usuários
        senhausers = User.separa_dados()[1]  # Lista com as senhas
        tentativas = 0
        tempo = 31
        check = False
        while True:
            entrar_login = input("\nDigite o login: ")
            entrar_senha = input("Digite a senha: ")
            try:
                k = 0
                while True:
                    if entrar_login == nameusers[k]:  # Verifica o login
                        try:
                            j = 0
                            while True:
                                if entrar_senha == senhausers[j]:  # Verifica a senha
                                    print(f"\n*** Bem vindo {entrar_login.title()} ***")
                                    check = True
                                    break
                                else:
                                    j = j + 1
                        except IndexError:  # Conta mais uma tentativa se estiver errada a senha
                            print("\nLogin ou senha incorretos!")
                            tentativas = tentativas + 1
                        break
                    else:
                        k = k + 1
            except IndexError:  # Conta mais uma tentativa se estiver errado o login
                print("\nLogin ou senha incorretos!")
                tentativas = tentativas + 1
            if check:
                break
            elif tentativas == 3:  # Chama a função bloquear, zera as tentativas e aumenta o tempo
                block.bloquear(tempo)
                tentativas = 0
                tempo = tempo + 30

    @staticmethod
    def cria_hash(senha):
        """
        Conta o número de hashs já criados e salva o novo hash na última linha com o número da contagem na frente.
        Separando o número da contagem e o hash por dois pontos. Criando uma lista numerada.

        :param str senha: Recebe a senha do usuário como parâmetro
        """
        arquivo = open("hash.txt", "r")
        senhausers = 0
        for linha in arquivo:  # Faz a contagem dos hashs
            senhausers = int(linha.strip().split(':')[0]) + 1
        arquivo.close()
        with open("hash.txt", "a") as arquivo_hash:  # Cria e salva um novo hash
            hash_senha = str(hashlib.md5(senha.encode()).hexdigest())
            arquivo_hash.writelines(f"{senhausers}:{hash_senha}\n")
        arquivo_hash.close()
