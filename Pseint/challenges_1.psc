Proceso challenges_1
	Definir dado Como Entero;
		
	Escribir "Lanzando el dado";
	dado <- Aleatorio(1, 6);
	Escribir "El dado muestra: ", dado;
		
	Si dado MOD 2 = 0 Entonces
		Escribir "El número es PAR";
	Sino
		Escribir "El número es IMPAR";
	FinSi
		
FinProceso
