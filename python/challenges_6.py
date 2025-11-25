import random
random.seed()   #Prepare random number generator

total = 0
suma = 0
pares = 0
impares = 0
respuesta = "si"
while respuesta == "si":
    dado = int(random.random() * 6) + 1
    total = total + 1
    suma = suma + dado
    print("Lanzamiento " + str(total) + ": " + str(dado))
    if dado % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    print("¿Deseas lanzar de nuevo? (si/no)")
    respuesta = input()
print("===== REPORTE FINAL =====")
print("Total de tiros efectuados: " + str(total))
print("Suma total de los tiros: " + str(suma))
print("Total de pares generados: " + str(pares))
print("Total de impares generados: " + str(impares))
