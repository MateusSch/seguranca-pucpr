import time
import sys


def bloquear(tempo):
    for t in range(0, tempo):
        sys.stdout.write(f"\rTempo de espera: {t} seg")
        sys.stdout.flush()
        time.sleep(1)


if __name__ == '__main__':
    bloquear(10)
