from itertools import product
import hashlib
import time

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]
chars = [chr(i) for i in range(32, 127)]  # Caracteres especiais


def bruteforce(caracteres, senha_hash):
    """
    Faz todas as combinações possíveis, criando um hash para cada combinação. Se o hash da combinação for igual ao
    parâmetro passado, o senha_hash, ele imprime a senha descoberta e com quantas tentativas foram necessárias.
    Senão ele aumenta mais um caractere na combinação, até achar a senha.

    :param caracteres: Listas com os caracteres
    :param senha_hash: Código hash
    :return: A senha compatível com o hash
    """
    tentativa = 0
    lensenha = 1  # Começa um caractere
    check = True
    while True:
        for i in product(caracteres, repeat=lensenha):
            combina = ''.join(i)
            hash_combina = str(hashlib.md5(combina.encode()).hexdigest())
            tentativa += 1
            if senha_hash == hash_combina:
                return f'\nA senha encontrada no hash "{hash_combina}" é: "{combina}", foi descoberta após ' \
                    f'{tentativa} tentativas.'
            else:
                check = False
        if not check:
            lensenha += 1  # Incrementa mais um caractere na combinação


def startbruteforce():
    """
    Cria uma lista com todos os hashs no arquivo txt, e passa um por um como parâmetro. E conta o tempo que levou para
    descobrir todas as senhas.

    :return: Retorna as mensagens da função bruteforce e imprime o tempo no final
    """
    with open("principal/hash.txt", "r") as arquivo:
        start = time.process_time()  # Inicia o time
        hashs = []
        for linha in arquivo:
            hashs.append(linha.strip().split(':')[1])
        for h in hashs:  # Chama a função bruteforce para cada hash
            print(bruteforce(chars, h))
        end = time.process_time()  # Finaliza o time
        print(f'\nTempo de execução --> {int((end - start) // 60)}min e {int((end - start) % 60)}seg')
    arquivo.close()


if __name__ == '__main__':  # Roda o código inteiro
    startbruteforce()
