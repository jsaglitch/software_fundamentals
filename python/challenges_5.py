import random
random.seed()   #Prepare random number generator

pares = 0
impares = 0
print("¿Cuántos lanzamientos quieres hacer?")
veces = int(input())
i = 1
while i <= veces:
    dado = int(random.random() * 6) + 1
    print("Lanzamiento " + str(i) + ": " + str(dado))
    if dado % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    i = i + 1
print("--- RESULTADOS ---")
print("Tiros PARES: " + str(pares))
print("Tiros IMPARES: " + str(impares))
