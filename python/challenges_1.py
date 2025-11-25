import random
random.seed()   #Prepare random number generator


# Lanzar el dado
dado = int(random.random() * 6) + 1
print("El dado muestra: " + str(dado))

# Verificar si es par o impar
if dado % 2 == 0:
    print("El número es PAR")
else:
    print("El número es IMPAR")
