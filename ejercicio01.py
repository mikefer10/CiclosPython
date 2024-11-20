'''
Programa que pide un número y calcula su factorial
'''
#Aquí pedimos por teclado que el usuario ingrese el número a factorar (por teclado)
c = int(input("¿Qué número quieres factorar?: "))

i = 1 #Inicilizamos la variable contador (i)
suma_fact = 1 #Inicializamos la variable que va a almacenar la sumatoria de cada multiplicación
#Como en el ciclo while nos permite saber cuando se detendrá el bucle, (c) va a ser nuestro indicador 
while i <= c: #Mientras el contador sea menor o igual al indicador se va a ejecutar lo de abajo
    #(suma_fact) inicialmente es 1 pero cada iteración va a aumentar con cada multiplicación, aumenta en razón de (c)
    suma_fact = suma_fact * i
    #Si queremos que en algún momento se cumpla la condición hay que incrementar (i + 1) cada vuelta 
    i = i + 1

#Por último mostramos el resultado de la factoración del número    
print(f"{c}! = {suma_fact}")