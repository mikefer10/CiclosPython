'''
Programa que pide 10 números e imprime el promedio de estos.
'''
#Este es nuestro contador
incremento = 1
#Este es nuestro acumulador (es 0 porque inicialmente no tenemos ningún valor)
suma = 0
print("A continuación ingresa 10 números: ")

for incremento in range(1,11): #Usamos (for) porque conocemos cuando debe parar
    recibe = int(input(f"{incremento}. -> ")) #Solicitamos un número al usuario
    suma = suma + recibe #El número ingresado lo agregamos a la suma global
    incremento = incremento + 1 #Aumentamos nuestro contador en 1 para que pueda llegar a 10 

#Una ves solicitados todos los números mostramos el promedio (la suma de todos los números entre 10)
print(f"Promedio: {(suma / (incremento - 1)):.2f}")