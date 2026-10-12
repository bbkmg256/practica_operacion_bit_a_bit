#!/bin/env python3

import sys
import re
import time

# Cifrado xor básico con repetición de clave #

# Pendiente: agregar cifrado de ficheros


def cifrar(clave, dato):
    print("Cifrando... ")
    time.sleep(2)
    
    bytes_cifrables = bytearray(dato, "utf-8")
    bytes_clave = bytearray(clave, "utf-8")

    # Repeticion de clave en la iteracion mediante modulo de división
    for i in range(len(bytes_cifrables)):
        bytes_cifrables[i] ^= bytes_clave[i % len(bytes_clave)]

    #print(bytes_cifrables)
    # print(bytes_cifrables.decode("utf-8"))
    print(f"[SALIDA] -> {bytes_cifrables.hex()}")


def decifrar(clave, dato):
    print("Decifrando... ")
    time.sleep(2)
    
    b_clave = bytearray(clave, "utf-8")
    
    # División del la cadena hexadecimal
    array_datos_divs = []
    for i in dato:
        array_datos_divs.append(i)

    # Conversión de cadena a enteros
    arreglo_enteros = []
    for i in array_datos_divs:
        if re.search("[0-9]", i):
            #print(f"{i} - Entero")
            arreglo_enteros.append(ord(i) - ord("0"))
        elif re.search("[a-f A-F]", i):
            #print(f"{i} - Letra")
            match i:
                case "a" | "A":
                    arreglo_enteros.append(10)
                case "b" | "B":
                    arreglo_enteros.append(11)
                case "c" | "C":
                    arreglo_enteros.append(12)
                case "d" | "D":
                    arreglo_enteros.append(13)
                case "e" | "E":
                    arreglo_enteros.append(14)
                case "f" | "F":
                    arreglo_enteros.append(15)
        else:
            print(f"[ERROR] {i} no es un valor hexadecimal!")
            sys.exit(1)

    # Empaquetado de los nibbles en bytes
    b_arr = bytearray()
    for i in range(0, len(arreglo_enteros)-1, 2):
        # Corrimiento de 4 bits a la derecha, mas empaquetado de los bits siguientes
        b_arr.append(arreglo_enteros[i] << 4 | arreglo_enteros[i+1])
        #print(f"[{arreglo_enteros[i]} {arreglo_enteros[i+1]}] - {b_arr.hex()}")
        #print(i)
        #time.sleep(2)

    # print(b_arr.hex())
    # xor inverso
    for i in range(len(b_arr)):
        b_arr[i] ^= b_clave[i % len(b_clave)]

    print(f"[SALIDA] -> {b_arr.decode('utf_8')}")


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
