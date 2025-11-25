"""
Jaider Arcos
Sebastian Cordoba
Samuel Martinez
Juan pablo Alvarez
"""

from datetime import datetime

empleados = [] 

def obtener_datos_empleado():
    """Solicita y valida los datos de un solo empleado."""
    print("\n--- Registro de Nuevo Empleado ---")
    
    nombres_completos = input("Ingrese Nombres Completos: ")
    
    while True:
        try:
            numero_movil = float(input("Ingrese Numero Movil: "))
            if numero_movil< 0:
                print("Entrada no valida.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número para el Numero Movil.")

    
    email = input("Ingrese Email: ")

    while True:
        try:
            salario = float(input("Ingrese Salario: "))
            if salario < 0:
                print("El salario no puede ser negativo. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número para el Salario.")

    while True:
        try:
            year_actual = datetime.now().year
            anio_nacimiento = int(input("Ingrese Año de Nacimiento [AAAA]: ")) 
        
            if anio_nacimiento > year_actual or anio_nacimiento < year_actual - 100:
                print(f"Año no válido. Debe estar entre {year_actual - 100} y {year_actual}.")
                continue
        
            edad = year_actual - anio_nacimiento

            if edad < 18:
                print("El empleado debe tener mínimo 18 años. Intente de nuevo.")
                continue

            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un año válido (ej: 1990).")

    while True:
        genero = input("Ingrese Género [M-F-O]: ").upper()
        if genero in ['M', 'F', 'O']:
            break
        else:
            print("Género no válido. Solo se acepta M, F u O. Intente de nuevo.")

    empleado = {
        "nombres": nombres_completos,
        "movil": numero_movil,
        "email": email,
        "salario": salario,
        "anio_nacimiento": anio_nacimiento,
        "genero": genero
    }
    return empleado

def agregar_otro_empleado():
    """Pregunta si el usuario desea registrar otro empleado con validación S/s/N/n."""
    while True:
        respuesta = input("\n¿Desea registrar otro empleado? [S/N]: ").upper()
        if respuesta == 'S':
            return True
        elif respuesta == 'N':
            return False
        else:
            print("Respuesta no válida. Solo se acepta S/s para Sí o N/n para No.")

while True:
    nuevo_empleado = obtener_datos_empleado()
    empleados.append(nuevo_empleado)
    if not agregar_otro_empleado():
        break

print("\n\n--- REGISTRO FINALIZADO ---")

total_empleados = len(empleados)

conteo_genero = {'M': 0, 'F': 0, 'O': 0}
total_salarios = 0
suma_edades = 0
year_actual = datetime.now().year

for emp in empleados:
    genero = emp['genero']
    salario = emp['salario']
    anio_nacimiento = emp['anio_nacimiento']
    
    if genero in conteo_genero:
        conteo_genero[genero] += 1
        
    total_salarios += salario
    
    edad = year_actual - anio_nacimiento
    suma_edades += edad

promedio_edades = suma_edades / total_empleados if total_empleados > 0 else 0

print("\n--- REPORTE DE EMPLEADOS ---")
print(f"1. ¿Cuántos empleados se registraron?: {total_empleados}")
print("\n2. Total por Género:")
print(f"  - Total de género M (Masculino): {conteo_genero['M']}")
print(f"  - Total de género F (Femenino): {conteo_genero['F']}")
print(f"  - Total de género O (Otro): {conteo_genero['O']}")
print(f"\n3. Total Salarios a Pagar: ${total_salarios:,.2f}")
print(f"\n4. Promedio de Edades: {promedio_edades:.2f} años")
