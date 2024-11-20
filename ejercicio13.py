'''
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Programa que determina cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
'''
#Vale 10 inicialmente porque es el primer pago
primer_pago = 10
#Sabemos que el pago es a 20 meses
meses = 20

total_pagado = primer_pago * (2**meses - 1) // (2 - 1) # 2 * (2 ^ {20-1}) // 1 = 10,485,750

#Como es progresivo el pago, usamos la formula (Pn = 10×2^{n−1}) en un rango de 1-21, pues el último no cuenta
pagos_mensuales = [primer_pago * 2**(n - 1) for n in range(1, meses + 1)] #Cada pago se almacena en esta lista

#Mostramos en forma de lista los 20 meses con sus pagos correspondientes
print("-- TUS PAGOS --") #Mensaje principal
for mes, ahorro in enumerate(pagos_mensuales, start=1): #Desempaquetamos cada valor de la lista
    print(f"Mes {mes}: {ahorro:.2f}") #Imprimimos cada mes y cada pago
print("\nTotal pagado después de 20 meses:", total_pagado, "euros") #Mostramos lo que se pagó en 20 meses