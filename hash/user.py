import hashlib


def cria_user():
    print('Usuário e senha só pode até 4 caracteres')
    nome = input('Digite o usuário: ')
    senha = input("Digite a senha: ")
    if len(nome) > 4 or len(senha) > 4:
        print('Tente novamente')
        cria_user()
    senha_bit = senha.encode()
    arquivo = open('texto.txt', 'w')
    hash_senha = str(hashlib.md5(senha_bit).hexdigest())
    arquivo.writelines(hash_senha)
    arquivo.close()


if __name__ == '__main__':
    cria_user()
