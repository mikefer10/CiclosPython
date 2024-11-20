'''
Programa que pide al usuario un número entero y muestra el mismo número en binario.
'''
#Función para hacer la conversión de decimal a binario
def convertir_a_binario_con_ciclo(numero): #Recibimos el número que la segunda función nos proporciona
    if numero == 0: #Si el número es cero
        return "0" #Inmediatamente retornamos 0 en forma de string (pues 0 en sí ya es un binario)
    binario = "" #Aquí se van a almacenar los ceros y unos
    while numero > 0: #Si el número si es mayor a cero
        residuo = numero % 2 #Dividimos ese número entre 2 y obtenemos el residuo
        binario = str(residuo) + binario  #Añadimos el residuo obtenido al inicio del string
        #El objetivo es dividir en cada iteración para llegar a cero y que while deje de cumplirse
        numero = numero // 2  #Dividimos entre 2 (cada ciclo va a valer la mitd de lo que valía)
    return binario #Retornamos como valor la cadena (str) que los almacena

#Función que recibe el valor del usuario y evalúa si nos es útil
def main(): #Como es la función principal no requerimos de un parámetro
    try: #Esperamos recibir un número de tipo (int)
        numero = int(input("Ingrese un número entero: ")) #Entrada
        if numero < 0: #Si el número es menor a cero
            print("Por favor, ingrese un número positivo.") #No nos sirve, y notificamos al usuario
        else: #Si es mayor a cero
            binario = convertir_a_binario_con_ciclo(numero) #Tomará el valor del string que almacena los binarios
            print(f"El número {numero} en binario es: {binario}") #Imprimimos los decimales
    except ValueError: #Si no se recibe un número entero lo tomamos como un error
        print("Por favor, ingrese un número entero válido.") #Mensaje del error

if __name__ == "__main__": #Si al nombre de la función es (main)
    main() #Llamamos a la función principal