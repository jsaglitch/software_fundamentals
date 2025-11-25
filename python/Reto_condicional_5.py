print(" INGRESO DE DATOS PERSONALES ")
print("Tipo de identificación (CC, PS, CE, CI):")
tipoID = input()
print("Nombres:")
nombres = input()
print("Apellidos:")
apellidos = input()
print("Género (M/F):")
genero = input()
print("Año de nacimiento:")
anioNacimiento = int(input())
print("Dirección:")
direccion = input()
print("Teléfono:")
telefono = input()
print("Salario actual:")
salarioActual = float(input())
porcentajeAumento = 0.0
if salarioActual <= 1200000:
    if genero == "F" or genero == "f":
        porcentajeAumento = 0.1
    else:
        if genero == "M" or genero == "m":
            porcentajeAumento = 0.08
        else:
            print("AVISO: Género no válido (Debe ser F, f, M o m). No hay aumento en Rango 1.")
else:
    if salarioActual < 2000000:
        porcentajeAumento = 0.05
    else:
        if salarioActual >= 2000000:
            if genero == "F" or genero == "f":
                porcentajeAumento = 0.03
            else:
                if genero == "M" or genero == "m":
                    porcentajeAumento = 0.025
                else:
                    print("AVISO: Género no válido (Debe ser F, f, M o m). No hay aumento en Rango 3.")
aumentoMonto = salarioActual * porcentajeAumento
salarioFinal = salarioActual + aumentoMonto
print("\\n=== RESULTADO FINAL ===")
print("Empleado: " + nombres + " " + apellidos)
print("Salario Base: " + str(salarioActual))
print("Porcentaje de Incremento: " + str(porcentajeAumento * 100) + "%")
print("Monto del Aumento: " + str(aumentoMonto))
print("SALARIO FINAL: " + str(salarioFinal))
