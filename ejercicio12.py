'''
Programa que determina cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, e informa cuánto lleva ahorrado cada mes.
'''
#Creamos una función que no recibe ningún valor como parámetro
def calcular_ahorros():
    total_anual = 0  #Variable para acumular cada mes, vale 0 porque inicialmente no estamos en ningún mes
    ahorros_mensuales = []  #Lista para almacenar los ahorros de cada mes

    #Este es el mensaje principal del programa, por lo que no recibe nada
    print("Ingresa la cantidad que deseas ahorrar al final de cada mes:")

    #Este es un ciclo que trabaja en función de los meses del año va a dar 11 ciclos
    for mes in range(1, 13): #En Python el último rango no se cuenta, en realidad va de 1-12
        while True: #Como este bucle anidado es verdadero se ejecuta al menos una vez
            try: #Se espera un valor de tipo (float)
                cantidad = float(input(f"Mes {mes}: ")) #Aquí se recibe y verifica
                if cantidad < 0: #Al tratarse de un incremento no podemos restar (not negativo)
                    print("La cantidad no puede ser negativa. Intenta de nuevo.") #Mensaje ´para el usuario
                else: #Si la cantidad es positiva
                    break #Salimos de (while), pero seguimos en (for)
            except ValueError: #Si el dato ingresado no es (float) lo menejamos como un error
                print("Por favor, introduce un número válido.") #Mensaje del error

        ahorros_mensuales.append(cantidad) #Dentro de (for) agregamos esa cantidad al final del diccionario
        total_anual += cantidad #Lo que llevemos hasta el momemto se le suma la nueva cantidad
        print(f"Total acumulado hasta el mes {mes}: {total_anual:.2f}") #Imprime la suma hasta el momento (con solo 2 decimales)

    #Cuando el programa llegue hasta aquí significa que ya ha llagado al mes 12
    print("\nResumen de ahorros:") #Vamos a mostrar los 12 meses y lo que se ahorró en cada uno
    '''
    Este (for) cambia un poco, pues como tal no hay un rango, pero si nos basamos de la lista
    tenemos 12 valores almacenados, asi que indicamos que que parta de 1, es decir (mes) va a 
    representar la posición del valor en la lista y que cada valor se almecene en (ahorro), esto
    se va a ejecutar hasta que se terminen los valores el la lista (de 1 a 12)
    '''
    for mes, ahorro in enumerate(ahorros_mensuales, start=1):
        print(f"Mes {mes}: {ahorro:.2f}") #Vamos a imprimir cada mes y cada valor

    print(f"\nTotal ahorrado en el año: {total_anual:.2f}") #Imprimimos la suma del ahorro anual

#Como todos los procesos están dentro de una función, es necesario mandar a llamarla
calcular_ahorros()