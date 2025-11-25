Algoritmo ClasificadorCompleto
	
    Definir numero Como Entero;
	
    Escribir " CLASIFICADOR COMPLETO DE NÚMEROS ";
    Escribir "Por favor, ingresa un número entero (positivo o negativo):";
    
    Leer numero;
	
    Si numero = 0 Entonces
        Escribir "El número ", numero, " es CERO (Par), pero no es Positivo ni Negativo.";
    SiNo
        Si numero > 0 Entonces
            Si numero MOD 2 = 0 Entonces
                Escribir "¡Clasificación: PAR POSITIVO!";
                Escribir "Detalle: Mayor que cero y divisible por 2.";
            SiNo
                Escribir "¡Clasificación: IMPAR POSITIVO!";
                Escribir "Detalle: Mayor que cero, con residuo al dividir por 2.";
            FinSi
        SiNo // El número debe ser negativo (numero < 0)
            Si Abs(numero) MOD 2 = 0 Entonces
                Escribir "¡Clasificación: PAR NEGATIVO!";
                Escribir "Detalle: Menor que cero y divisible por 2.";
            SiNo
                Escribir "¡Clasificación: IMPAR NEGATIVO!";
                Escribir "Detalle: Menor que cero, y no es divisible por 2.";
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo