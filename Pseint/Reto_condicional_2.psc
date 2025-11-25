Algoritmo ValidadorParImpar
    Definir numero Como Entero;
	
    Escribir " VALIDADOR DE NÚMEROS PAR / IMPAR  ";
    Escribir "Por favor, ingresa un número entero (positivo o negativo):";
	
    Leer numero;
	
    Si Abs(numero) MOD 2 = 0 Entonces
        Escribir "¡El número ", numero, " es PAR!";
        Escribir "Detalle: Se puede dividir exactamente por 2.";
    SiNo
        Escribir "¡El número ", numero, " es IMPAR!";
        Escribir "Detalle: Al dividirlo por 2, sobra 1.";
    FinSi
	
FinAlgoritmo