import random
random.seed()   

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
print("¿Cuántas veces quieres lanzar el dado?")
veces = int(input())
i = 1
while i <= veces:
    dado = int(random.random() * 6) + 1
    print("Lanzamiento " + str(i) + ": " + str(dado))
    if dado == 1:
        c1 = c1 + 1
    else:
        if dado == 2:
            c2 = c2 + 1
        else:
            if dado == 3:
                c3 = c3 + 1
            else:
                if dado == 4:
                    c4 = c4 + 1
                else:
                    if dado == 5:
                        c5 = c5 + 1
                    else:
                        c6 = c6 + 1
    i = i + 1
print(" RESULTADOS ")
print("Número 1: " + str(c1) + " veces")
print("Número 2: " + str(c2) + " veces")
print("Número 3: " + str(c3) + " veces")
print("Número 4: " + str(c4) + " veces")
print("Número 5: " + str(c5) + " veces")
print("Número 6: " + str(c6) + " veces")
