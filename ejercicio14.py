'''
Muestra en pantalla los N primeros números primos. Pedimos por teclado la cantidad 
de números primos que queremos mostrar.
'''
'''
Nótese que a continuación las 3 funciones están de atrás para adelante, pues la primera depende
de la segunda y a su vez la segunda de la primera, y en la ejecución sería como:
1. Tercera Función; 2. Segunda Función; 3. Primera Función
'''
def es_primo(numero): #Recibe un número como parámetro (va a recibir los números de la segunda función)
    if numero < 2: #Si ese número es manor a 2
        return False #Retornamos falso como valor pues 2 es el primer número primo
    for i in range(2, int(numero ** 0.5) + 1): #
        if numero % i == 0: #Si el módulo del número entre la vuelta actual es 0
            return False #Nos indica que no es un número primo
    return True #Si  la condición actual no se cumple entoces si es un número primo

#Creamos una nueva función que recibe como parámetro el número ingresado por el usuario
def mostrar_primos(n):
    primos = [] #Este es una lista para ir guardando cada número primo
    numero = 2  #Este va a ser el contador (comenzamos desde el primer número primo)
    while len(primos) < n: #Lo vamos a ejecutar desde 2 hasta el número límite
        if es_primo(numero): #Llamamos a la primera función con su respactivo parámetro (numero) y si lo que nos retorna es True
            primos.append(numero) #Quiere decir que es primo y lo agregamos al final de la lista
        numero += 1 #Aumentamos el contador para que lo volvamos a comprobar y se epueda cumplir la condición
    #Cuando el (while) ya no se cumpla esta retornamos la lista de todos los números primos
    return primos

#Función encargada de recibir el número y comprobar que sea válido para lo que lo vamos a usar
def main(): #No esperamos recibir ningún valor (es una función independiente)
    try: #Esperamos recibir un número de tipo entero
        n = int(input("Ingrese la cantidad de números primos que desea mostrar: ")) #La entrada
        if n <= 0: #Si dicho número es menor o igual a cero no podremos trabajar con el
            print("Por favor, ingrese un número positivo.") #Mensaje de alerta
        else: #Si es mayor a cero entonces
            primos = mostrar_primos(n) #Llamamos a la segunda función que a su vez llama a la primera (funciones en cadena)
            print(f"Los primeros {n} números primos son: {primos}") #Impriminos los números primos que tenemos almacenados en la lista
    except ValueError: #Si por el contrario recibimos un valor diferente de (int), lo consideramos como un error
        print("Por favor, ingrese un número válido.") #Mensaje posterior al error

#Llamamos a la función principal, que en este caso es la tercera
if __name__ == "__main__": #Si el nombre de la función es (main)
    main() #Llamamos a la función, sin parámetro porque no lo necesita