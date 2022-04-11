from itertools import product
import hashlib
import time

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]
chars = [chr(i) for i in range(32, 127)]  # Caracteres especiais


def bruteforce(caracteres, senha_hash):
    tentativa = 0
    lensenha = 1
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
    with open("principal/hash.txt", "r") as arquivo:
        start = time.process_time()
        hashs = []
        for linha in arquivo:
            hashs.append(linha.strip().split(':')[1])
        for h in hashs:
            print(bruteforce(chars, h))
        end = time.process_time()
        print(f'\nTempo de execução --> {int((end - start) // 60)}:{int((end - start) % 60)}')
    arquivo.close()


if __name__ == '__main__':
    startbruteforce()
