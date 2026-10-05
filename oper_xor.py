#!/bin/env python3

import sys

# Operación bit a bit XOR (Reversible) :)

# Apertura de un fichero de ejemplo en modo lectura binaria
with open("./fichero_ejemplo.txt", "rb") as buf_f:
    fichero_data = buf_f.read()
    #sys.exit()
    fichero_modificable = bytearray(fichero_data)

    valor_operable_xor = 0xAA # 10101010 = 170

    # Operación XOR iterativa sobre los bits del fichero,
    # respecto al valor operable anterior.
    for i in range(len(fichero_modificable)):
        fichero_modificable[i] ^= valor_operable_xor

# Apertura del mismo fichero de ejemplo en modo escritura binaria
with open("./fichero_ejemplo.txt", "wb") as buf_f:
    buf_f.write(fichero_modificable)
    print("Fichero modificado!")
