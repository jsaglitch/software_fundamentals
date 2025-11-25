Algoritmo CalculoNomina
	
    Definir tipoID, nombres, apellidos, genero, direccion, telefono Como Caracter;
    Definir anioNacimiento Como Entero;
    Definir salarioActual, porcentajeAumento, aumentoMonto, salarioFinal Como Real;
	
    Escribir " INGRESO DE DATOS PERSONALES ";
    Escribir "Tipo de identificación (CC, PS, CE, CI):";
    Leer tipoID;
    Escribir "Nombres:";
    Leer nombres;
    Escribir "Apellidos:";
    Leer apellidos;
    Escribir "Género (M/F):";
    Leer genero;
    Escribir "Año de nacimiento:";
    Leer anioNacimiento;
    Escribir "Dirección:";
    Leer direccion;
    Escribir "Teléfono:";
    Leer telefono;
    Escribir "Salario actual:";
    Leer salarioActual;
	
    porcentajeAumento <- 0.0;
	
    // --- Lógica de Aumento de Salario ---
    Si salarioActual <= 1200000 Entonces
        // Rango 1: Salario <= 1200000
        Si genero = "F" O genero = "f" Entonces
            porcentajeAumento <- 0.1;
        SiNo
            Si genero = "M" O genero = "m" Entonces
                porcentajeAumento <- 0.08;
            SiNo
                Escribir "AVISO: Género no válido (Debe ser F, f, M o m). No hay aumento en Rango 1.";
            FinSi
        FinSi
    SiNo
        Si salarioActual < 2000000 Entonces
            // Rango 2: 1200000 < Salario < 2000000
            porcentajeAumento <- 0.05;
        SiNo 
            // Rango 3: Salario >= 2000000
            Si genero = "F" O genero = "f" Entonces
                porcentajeAumento <- 0.03;
            SiNo
                Si genero = "M" O genero = "m" Entonces
                    porcentajeAumento <- 0.025;
                SiNo
                    Escribir "AVISO: Género no válido (Debe ser F, f, M o m). No hay aumento en Rango 3.";
                FinSi
            FinSi
        FinSi
    FinSi
	
    aumentoMonto <- salarioActual * porcentajeAumento;
    salarioFinal <- salarioActual + aumentoMonto;
	
    Escribir ""; // Salto de línea
    Escribir "=== RESULTADO FINAL ===";
    Escribir "Empleado: ", nombres, " ", apellidos;
    Escribir "Salario Base: ", salarioActual;
    Escribir "Porcentaje de Incremento: ", porcentajeAumento * 100, "%";
    Escribir "Monto del Aumento: ", aumentoMonto;
    Escribir "SALARIO FINAL: ", salarioFinal;
	
FinAlgoritmo