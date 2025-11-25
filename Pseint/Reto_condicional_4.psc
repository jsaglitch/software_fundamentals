Algoritmo CalculadoraMenu
    Definir num1, num2, res Como Real;
    Definir opt Como Entero;
	
    num1 <- 0;
    num2 <- 0;
	
    Escribir "Enter value to number 1";
    Leer num1;
    
    Escribir "Enter value to number 2";
    Leer num2;
	
    Escribir "Math manu:[1].Add- [2].Subs - [3].Mult -[4].Div -[5].All";
    Escribir "Press any option[1 - 5]";
    Leer opt;
	
    Si opt = 1 Entonces
        res <- num1 + num2;
        Escribir "Addition:", res;
    SiNo
        Si opt = 2 Entonces
            res <- num1 - num2;
            Escribir "Substraction:", res;
        SiNo
            Si opt = 3 Entonces
                res <- num1 * num2;
                Escribir "Multiplication:", res;
            SiNo
                Si opt = 4 Entonces
                    Si num2 <> 0 Entonces
                        res <- num1 / num2;
                        Escribir "division:", res;
                    SiNo
                        Escribir "It is not possible to divide by zero";
                    FinSi
                SiNo
                    Si opt = 5 Entonces
                        Escribir "Add:", num1 + num2;
                        Escribir "Subs:", num1 - num2;
                        Escribir "Mult:", num1 * num2;
                        Si num2 <> 0 Entonces
                            Escribir "Div:", num1 / num2;
                        SiNo
                            Escribir "It is not possible to divide by zero";
                        FinSi
                    SiNo
                        Escribir "Invalid option";
                    FinSi
                FinSi
            FinSi
        FinSi
    FinSi
	
FinAlgoritmo