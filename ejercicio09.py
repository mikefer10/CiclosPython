'''
Programa que pide el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo vuelve a pedir.
A continuación se van introduciendo números hasta que se introduzca el 0. 
Cuando termina el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* Informa si hemos introducido algún número igual a los límites del intervalo.
'''
#Mensaje principal del programa
print("-- A continuación ingresa un intervalo --")

#Variable que representa (continuar solicitando números), es verdadero porque al menos se ejecuta una vez
pedir = True
while pedir == True: #Mientras (pedir) sea verdadero se ejecuta
    li = int(input("Entre: ")) #Recibe el número de partida
    ls = int(input("Y: ")) #Recibe el número a llegar
    if li < ls: #Si el número inicial es menor
        if li == 0 or ls == 0: #Si el inferior o el superior es cero
            print("No puedes usar el cero") #Pues ya está reservado para terminar con la ejecución
        else: #Si los dos son diferentes de cero
            pedir = False #No es necesario pedir otra vez el número
    else: #Si el número inicial es menor no podemos operar, así que lo pedimos de nuevo
        print("Inténtalo de nuevo...") #Mensaje

#Representa la suma de todos los números dentro del intervalo
suma = 0
#Representa la cantidad de números que hay fuera del intervalo 
fuera = 0
#Es para identificar los que son iguales al límite inferior
i_li = 0
#Contrario al enterior representa los que son igual al límite superior
i_ls = 0
#Esta variable represente si se quiere seguir o no (es verdadero porque se ejecuta el menos una vez)
seguir = True
#Ciclo
while seguir == True: #Mientras (seguir) sea verdadero se ejecuta 
    entrada = int(input("-> ")) #Recibimos cada número y lo almacenamos en (entrada)
    if entrada == 0: #Si la entrada es cero
        print("¡GRACIAS POR ACCEDER!") #Significa que se quiere terminar
        break #Salimos de (while)
    elif entrada == li: #Si no y si la entrada es igual al límite inferior
        i_li += 1 #Aumentamos los iguales al límite superior en 1
    elif entrada == ls: # Si no y si la entrada es igual al límite superior
        i_ls += 1 #Ahora aumentamos los iguales al límite superior en 1
    elif entrada in range(li, ls + 1): #Si no y si la entrada esta dentro del rango
        suma = suma + entrada #Podemos agregar este valor a la suma global
    else: #Si no es ninguna de las condiciones anteriores
        fuera += 1 #Entonces es que el número está fuera del rango

#Imprimimos en pantalla los resultados de la ejecución
print(f"Suma dentro del intervalo: {suma}\nNúmeros fuera del intervalo: {fuera}\nNúmeros iguales al intervalo: {i_li + i_ls}")
if i_li > 0 or i_ls > 0: #Esto implica que al menos se haya ingresado un número igual al límite inferior o superior
    print(f"({i_li} iguales a {li}; y {i_ls} iguales a {ls})") #Imprime cuántos son iguales que 