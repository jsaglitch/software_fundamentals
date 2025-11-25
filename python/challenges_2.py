import random
random.seed()   #Prepare random number generator

print("Reto: Lanzamiento mltiple de dado ")
print("Cuantas veces desea lanzar el dado?")
n = int(input())
suma = 0
i = 1
while i <= n:
    dado = int(random.random() * 6) + 1
    print("Lanzamiento " + str(i) + ": " + str(dado))
    suma = suma + dado
    i = i + 1
print("La suma total de los lanzamientos es: " + str(suma))
