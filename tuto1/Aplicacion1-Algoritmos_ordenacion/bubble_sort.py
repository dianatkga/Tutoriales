"""La ordenacion de burbuja, un algoritmo
    de ordenamiento.

Implementacion de la ordenacion burbuja sobre
una lista, retornando una lista ordenada
"""

def burbuja(seq):
    L = len(seq)
    for _ in range(L):
        for n in range(1,L):
            if seq[n] < seq[n-1]:
                seq[n-1], seq[n] = seq[n], seq[n-1]

    return seq

