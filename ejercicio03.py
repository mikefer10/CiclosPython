'''
Programa que pide números hasta que se introduce un cero. Imprime 
la suma y la media de todos los números introducidos.
'''
#Esta variable es para guardar lo que llevamos de la suma de cada número introducido
suma = 0
#Este es el contador nos va a servir para saber cuantos números se ingresaron y calcular la media
contador = 0
"""
Este es el estado por defacto de (while), o sea que se cumple desde el principio, 
y va a recibir por lo menos un número, pues si es 0 se detendría
"""
i = True
print("Ingresa un número o sal con [0]")
while i == True: # Como ya mencionamos, se cumple para la primer vuelta
    entrada = int(input("-> ")) #Solicita un número
    if entrada != 0: #Evalúa si el número ingresado es diferente de 0, pues indica (seguir/continuar)
        suma = suma + entrada #Sumamos ese número a lo que ya llevamos (si es la primer ejecución se guarda ese valor)
    elif entrada == 0: #Aquí evalúa si el número es 0 porque indicaría (salir/parar)
        if contador == 1: #Si el 0 se ingresa desde la primer iteración pide ingresar al menos 2 números
            print("Ingresa al menos 2 números")
        elif contador >= 2: #Anteriormente ingresó al menos 2 números diferentes de 0            
            print(f"La suma total es de {suma}") #Esta es la suma todos los números ingresados
            print(f"La media es de {(suma / contador):.2f}") #Este es el promedio de esos números
        i = False #Ya que el usuario quizo salir, vamos a cambiar la varieble a 'False' para parar el programa
    contador = contador + 1 #En caso de no querer salir aumentamos el contador y regresamos
