#!/bin/env python3

import sys

# Cifrado xor básico con repetición de clave

def cifrar(clave, dato):
    bytes_cifrables = bytearray(dato, "utf-8")
    bytes_clave = bytearray(clave, "utf-8")

    # Repeticion de clave en la iteracion mediante modulo de división
    for i in range(len(bytes_cifrables)):
        bytes_cifrables[i] ^= bytes_clave[i % len(bytes_clave)]

    # print(bytes_cifrables.decode("utf-8"))
    print(f"[Texto cifrado] -> {bytes_cifrables.hex()}")


# Pendiente xd
def decifrar(clave, dato):
    print("Pendiente xd")
    pass


def main():
    operacion = sys.argv[1]
    clave_de_cifrado = str(sys.argv[2])
    dato_a_cifrar = str(sys.argv[3])

    match operacion:
        case "-c":
            cifrar(clave_de_cifrado, dato_a_cifrar)
        case "-d":
            decifrar(clave_de_cifrado, dato_a_cifrar)
        case _:
            print("Funcional, pero no hace nada xd")


if __name__ == "__main__":
    main()
