from math import fabs
print("=== CLASIFICADOR COMPLETO DE NÚMEROS ===")
print("Por favor, ingresa un número entero (positivo o negativo):")
numero = int(input())
if numero == 0:
    print("El número " + str(numero) + " es CERO (Par), pero no es Positivo ni Negativo.")
else:
    if numero > 0:
        if numero % 2 == 0:
            print("¡Clasificación: PAR POSITIVO!")
            print("Detalle: Mayor que cero y divisible por 2.")
        else:
            print("¡Clasificación: IMPAR POSITIVO!")
            print("Detalle: Mayor que cero, con residuo al dividir por 2.")
    else:
        if fabs(numero) % 2 == 0:
            print("¡Clasificación: PAR NEGATIVO!")
            print("Detalle: Menor que cero y divisible por 2.")
        else:
            print("¡Clasificación: IMPAR NEGATIVO!")
            print("Detalle: Menor que cero, y no es divisible por 2.")
