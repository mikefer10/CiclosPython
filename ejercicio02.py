'''
Programa que permite adivinar un número. Se genera un número aleatorio del 
1 al 100. Luego va pidiendo números y va respondiendo si el número a adivinar 
es mayor o menor que el introducido, a demás de los intentos que te quedan 
(tienes 10 intentos para acertarlo). Termina cuando se acierta el número 
(además dice en cuantos intentos se acertó), si se supera el limite 
de intentos se muestra el número que había generado.
'''
#Sabemos que para generar un número aleatorio nos apoyamos de la librería 'random'
import random
#Esta línea elige un número de tipo 'int' aleatoriamente en un rango de 0-100
aleatorio = random.randint(0 , 100)
'''
variable (intentos) va a aumentar en función de las iteraciones,
y al mismo tiempo será el indicador para el usuario
'''
intentos = 1
#Es una variable es necesaria (nos premite parar la agecución cuando sea 'True') 
acertado = False

"""
Esta sentencia se basa en la vuelta en la que estamos (contador intentos) y se 
ejecuta siempre y cuando sea menor o y gual a 10, comenzando en este caso en 1
"""
while intentos <= 10:
    revision = int(input("¿Qué número crees que sea?: ")) #Solicitamos el número al usuario
    if revision > aleatorio: #Para indicar que el número es mayor al ingreado
        print(f"Es menos de {revision}")
    elif revision == aleatorio: #Para indicar que se ha acertado correctamente 
         print(f"✓ Has acertado, {revision} es el número\n• Lo has hecho en {intentos} intentos")
         acertado = True #Cambiamos el valor de la varieble de 'False' a 'True'
         break #Se detiene el programa (ya no pide más números)
    elif revision < aleatorio: #Para indicar que el número es menor al ingresado
        print(f"Es más de {revision}")
    intentos = intentos + 1 #Si no acertó, eumenta el contador en 1 y regresa al principio

#Nos apoyamos por si no acertó en ningúno de los 10 intentos se muestre cual era el número
if acertado == False:
        print(f"La respuesta correcta es {aleatorio}")