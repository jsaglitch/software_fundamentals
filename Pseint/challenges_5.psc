Proceso challenges_5
    Definir veces, dado, i, pares, impares Como Entero;
    
    pares <- 0;
    impares <- 0;
    
    Escribir "¿Cuántos lanzamientos quieres hacer?";
    Leer veces;
    
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        dado <- Aleatorio(1, 6);
        Escribir "Lanzamiento ", i, ": ", dado;
        
        Si dado MOD 2 = 0 Entonces
            pares <- pares + 1;
        Sino
            impares <- impares + 1;
        FinSi;
    FinPara;
    
    Escribir "--- RESULTADOS ---";
    Escribir "Tiros PARES: ", pares;
    Escribir "Tiros IMPARES: ", impares;
    
FinProceso
