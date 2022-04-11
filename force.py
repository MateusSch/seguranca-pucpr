from itertools import product

chars = [chr(i) for i in range(97, 123)]
chars += [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(48, 58)]
chars = [chr(i) for i in range(32, 127)]  # Caracteres especiais


def bruteforce(caracteres, senha):
    tentativa = 0
    lensenha = 1
    check = True
    while True:
        for i in product(caracteres, repeat=lensenha):
            combina = ''.join(i)
            tentativa += 1
            if senha == combina:
                return f'\nA senha é "{combina}", foi descoberta após {tentativa} tentativas.'
            else:
                check = False
        if not check:
            lensenha += 1  # Incrementa mais um caractere na combinação


print(bruteforce(chars, '1234'))
