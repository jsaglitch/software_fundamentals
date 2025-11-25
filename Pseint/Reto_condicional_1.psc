Algoritmo SimuladorDados
    Definir dado1, dado2 Como Entero;
    Definir clasificacion1, clasificacion2 Como Caracter;
	
    Escribir "=== Simulador de Dados (Reto Condicional 1) ===";
	
    dado1 <- azar(6) + 1;
    dado2 <- azar(6) + 1;
	
    Escribir "Dado 1 generó: ", dado1;
    Escribir "Dado 2 generó: ", dado2;
	
    Si dado1 MOD 2 = 0 Entonces
        clasificacion1 <- "PAR";
        Escribir "El número ", dado1, " es PAR. ¡Se puede dividir por 2 sin que sobre nada!";
    SiNo
        clasificacion1 <- "IMPAR";
        Escribir "El número ", dado1, " es IMPAR. ¡Al dividirlo por 2, sobra 1!";
    FinSi
	
    Si dado2 MOD 2 = 0 Entonces
        clasificacion2 <- "PAR";
        Escribir "El número ", dado2, " es PAR. ¡Se puede dividir por 2 sin que sobre nada!";
    SiNo
        clasificacion2 <- "IMPAR";
        Escribir "El número ", dado2, " es IMPAR. ¡Al dividirlo por 2, sobra 1!";
    FinSi
	
    Si dado1 = dado2 Entonces
        Escribir " YOU WIN! ";
        Escribir "¡El valor de los dados es EXACTAMENTE el mismo!";
    SiNo
        Escribir " GAME OVER ";
    FinSi
FinAlgoritmo