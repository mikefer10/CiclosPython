'''
Programa que muestra la tabla de multiplicar de los números 1,2,3,4 y 5.
'''
#Este es el contador de la tabla de multiplicar en la que estamos (va de 1-5)
num = 1
#Este es el contador dentro de cada tabla (va de 1-10)
i_while = 1

#Como conocemos que solo son tablas del 1-5 
#Rango  1  2  3  4  5  6
#Valor  0  1  2  3  4  5
for num in range(1, 6): #El primer valor en el rango no lo cuenta, realmente va del rango (2-6)
    print(f"TABLA DEL {num}") #Indica que tabla de multiplicar va a imprimir
    while i_while <= 10: #Mientras que el contador de while sea menor o igual a 10
        print(f"{num} x {i_while} = {num*i_while}") #Se opera el numero de la tabla actual con el contador de while
        i_while = i_while + 1 #Aumentamos en 1 al contador de while para poder llegara a 10
        if i_while == 11: #Si se cumple significa que ya se han iterado las 10 veces
            print("") #Este es solo un espacio de separación entre tabla y tabla
    num = num + 1 #Aumentamos el valor de la tabla en 1 para poder llegar hasta la tabla del 5
    i_while = 1 #Como (i_while) hasta ahora seguía valiendo 11 la cambiemos a 1 y que pueda operar con normalidad para la siguiente tabla