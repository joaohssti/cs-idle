import math

def formatDataUnit(n:int) -> str:

    sufixos = ['byte', 'kb', 'Mb', 'Gb', 'Tb', 'Pb', 'Eb', 'Zb', 'Yb']

    if n < 1024:
        return f"{n} {sufixos[0]}"

    magnitude = int(math.floor(math.log10(n)) / 3)

    if magnitude >= len(sufixos):
        magnitude = len(sufixos) - 1

    n_escala = n / (1024 ** magnitude)

    return f"{n_escala:.2f} {sufixos[magnitude]}"

