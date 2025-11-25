import random
random.seed()   #Prepare random number generator

print("=== Simulador de Dados (Reto Condicional 1) ===")
dado1 = int(random.random() * 6) + 1
dado2 = int(random.random() * 6) + 1
print("Dado 1 generó: " + str(dado1))
print("Dado 2 generó: " + str(dado2))

if dado1 % 2 == 0:
    clasificacion1 = "PAR"
    print("El número " + str(dado1) + " es PAR. ¡Se puede dividir por 2 sin que sobre nada!")
else:
    clasificacion1 = "IMPAR"
    print("El número " + str(dado1) + " es IMPAR. ¡Al dividirlo por 2, sobra 1!")
if dado2 % 2 == 0:
    clasificacion2 = "PAR"
    print("El número " + str(dado2) + " es PAR. ¡Se puede dividir por 2 sin que sobre nada!")
else:
    clasificacion2 = "IMPAR"
    print("El número " + str(dado2) + " es IMPAR. ¡Al dividirlo por 2, sobra 1!")

if dado1 == dado2:
    print(" YOU WIN! ")
    print("¡El valor de los dados es EXACTAMENTE el mismo!")
else:
    print(" GAME OVER ")
    print("Los dados han caído en valores diferentes.")
