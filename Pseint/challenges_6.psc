Proceso challenges_6
	
    Definir dado, total, suma, pares, impares Como Entero;
    Definir respuesta Como Caracter;
    
    total <- 0;
    suma <- 0;
    pares <- 0;
    impares <- 0;
    respuesta <- "si";
    
    Mientras respuesta = "si" Hacer
        dado <- Aleatorio(1, 6);
        total <- total + 1;
        suma <- suma + dado;
        Escribir "Lanzamiento ", total, ": ", dado;
        
        Si dado MOD 2 = 0 Entonces
            pares <- pares + 1;
        Sino
            impares <- impares + 1;
        FinSi;
        
        Escribir "¿Deseas lanzar de nuevo? (si/no)";
        Leer respuesta;
    FinMientras;
    
    Escribir "===== REPORTE FINAL =====";
    Escribir "Total de tiros efectuados: ", total;
    Escribir "Suma total de los tiros: ", suma;
    Escribir "Total de pares generados: ", pares;
    Escribir "Total de impares generados: ", impares;
    
FinProceso