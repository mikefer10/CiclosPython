'''
Programa que imprime todos los números pares entre dos números que 
se le pidan al usuario.
'''
print("-- RANGO --")
inicial = int(input("¿Desde que número?: ")) #Desde que número vamos a partir
final = int(input("¿Hasta qué número?: ")) #Cual es el límite al que hay que llegar

#Representa los números pares que hay
pares = 0
#Es el contador para el bucle (for)
i = 1
for i in range(inicial , final + 1): #Va a iterar en función del velor inicial al final más 1 porque el último no lo vale
    if i % 2 == 0: #Si el residio de dividir el valor de la iteración actual entre 2 es 0
        pares = pares + 1 #Indica que se trata de un número par
    i = i + 1 #Aumentamos el contador de (for) en 1 para que en algún momento la condición se cumpla

#Mostramos cuántos pares hay en ese rango
print(f"Hay {pares} números pares")