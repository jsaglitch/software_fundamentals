Proceso challenges_2
    Definir veces, dado, suma, i Como Entero;
    
    suma <- 0;
    
    Escribir "¿Cuántas veces quieres lanzar el dado?";
    Leer veces;
    
    Para i <- 1 Hasta veces Con Paso 1 Hacer
        dado <- Aleatorio(1, 6);
        Escribir "Lanzamiento ", i, ": ", dado;
        suma <- suma + dado;
    FinPara;
    
    Escribir "Suma total de todos los lanzamientos: ", suma;
    
FinProceso
