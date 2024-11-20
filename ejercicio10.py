'''
Programa que dados dos números, uno real (base) y un entero positivo 
(exponente), imprime en pantalla el resultado de la potencia. 
No se utiliza el operador de potencia.
'''
#Creamos una función para obtener la petencia sin  usar la operación de potencia (**)
def calcular_potencia(base, exponente): #Recibe como parámetros 2 variables (base y exponente)
    #Validamos que el exponente sea un entero positivo
    if exponente < 0: #Validamos que no lo sea para retornar un mensaje de error
        return "El exponente debe ser un entero positivo." #Retornamos un (str)
    
    #Inicializamos el resultado a 1 (la potencia de cualquier número elevado a 0 es 1)
    resultado = 1

    #Multiplicamos la base por sí misma exponente veces
    for _ in range(exponente): 
        resultado *= base
    
    return resultado #Esto es lo que vamos a esperar recibir al final

# Solicitar al usuario los valores de base y exponente
try: #Se esperan dos variables (una de tipo int y otra tipo float)
    base = float(input("Introduce la base (número real): ")) #Recibimos la base
    exponente = int(input("Introduce el exponente (entero positivo): ")) #Recibimos el exponente
    
    #Llamamos a la función al mismo tiempo que imprimimos lo que nos retorne, pasando como parámetros las 2 variables recibidas
    print(f"{base} elevado a la {exponente} es igual a: {calcular_potencia(base, exponente)}")
except ValueError: #Si las entradas no son del tipo que se esperaban, lo manejamos como error
    print("Por favor, introduce un número válido.") #Mensaje del error