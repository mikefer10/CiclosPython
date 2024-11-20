'''
Programa que dice si un número introducido por teclado es o no primo. 
'''
#Esta es una librería para usar operaciones matemáticas
import math

def es_primo(numero): #Creamos una función que recibe como parámetro un número
    if numero <= 1: #Si ese número es menor o igual a 1
        return False  #Todos esos números menores a 2 no son primos
    if numero <= 3: #Si el número es menor o igual a 3
        return True  #Tanto el 2 como el 3 son primos

    #Si el residuo del número entre 2 o 3 es 0, entonces no es primo
    if numero % 2 == 0 or numero % 3 == 0: #Con que se cumpla una es suficiente
        return False #Devolvemos un valor falso (no es primo)

    #Verificamos divisores desde 5 hasta la raíz cuadrada del número
    limite = int(math.sqrt(numero)) #Obtenemos la raíz cuadrada
    for i in range(5, limite + 1, 2):  #Incrementamos en 2 para saltar los pares
        if numero % i == 0: #Si el residuo de dividir el número entre el valor de la iteración actual es 0
            return False #Devolvemos un valor falso (no es primo)

    #Si ninguna de las condiciones anteriores se cumple está claro que es un número primo
    return True

#Programa principal
try: #Esto es lo que se espera recibir por parte del usuario (un valor de tipo int)
    numero = int(input("Introduce un número entero: ")) #Recibimos la entrada del usuario
    if es_primo(numero): #Si la función la llamamos, le pasamos el parámetro y nos devuelve True
        print(f"{numero} es un número primo.") #Entonces sabemos que es un número primo
    else: #Si no retorna True
        print(f"{numero} no es un número primo.") #Entonces no es un número primo
except ValueError: #En caso de que el valor decibido no sea (int), lo manejamos como error
    print("Por favor, introduce un número entero válido.") #Mensaje del error