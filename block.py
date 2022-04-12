import time
import sys


def bloquear(tempo):
    """
    Faz uma contagem na mesma linha com range definido pelo parâmetro. Bloqueando qualquer ação até a contagem acabar.

    :param int tempo: Número que define o range do for
    """
    for t in range(0, tempo):
        sys.stdout.write(f"\rTempo de espera: {t} seg")
        sys.stdout.flush()
        time.sleep(1)


if __name__ == '__main__':  # Apenas para teste
    bloquear(11)  # Faz a contagem até 10 segundos
