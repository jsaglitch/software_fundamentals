Proceso challenges_4
    Definir dado1, dado2, lanzamientos Como Entero;
    
    lanzamientos <- 0;
    dado1 <- 0;
    dado2 <- 0;
    
    Mientras dado1 <> 6 O dado2 <> 6 Hacer
        dado1 <- Aleatorio(1, 6);
        dado2 <- Aleatorio(1, 6);
        lanzamientos <- lanzamientos + 1;
        Escribir "Lanzamiento ", lanzamientos, " - Dado 1: ", dado1, " | Dado 2: ", dado2;
    FinMientras;
    
    Escribir "¡PAR DE SEIS! Se necesitaron ", lanzamientos, " lanzamientos";
    
FinProceso
