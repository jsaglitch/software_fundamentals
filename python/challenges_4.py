import random
random.seed()   #Prepare random number generator

lanzamientos = 0
dado1 = 0
dado2 = 0
while dado1 != 6 or dado2 != 6:
    dado1 = int(random.random() * 6) + 1
    dado2 = int(random.random() * 6) + 1
    lanzamientos = lanzamientos + 1
    print("Lanzamiento " + str(lanzamientos) + " - Dado 1: " + str(dado1) + " | Dado 2: " + str(dado2))
print("¡PAR DE SEIS! Se necesitaron " + str(lanzamientos) + " lanzamientos")
