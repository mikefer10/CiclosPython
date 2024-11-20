'''
Programa que pide caracteres e imprima 'VOCAL' si son vocales y 'NO VOCAL' 
en caso contrario, el programa termina cuando se introduce un espacio.
'''
#Mensaje principal del programa
print("INGRESA UNA LETRA O UN ESPACIO PARA SALIR:")
#Esta variable la usaremos para continuar o parar con la ejecución del ciclo
seguir = True #Es verdadero, peri pudo ser (False)
while seguir == True: #Mientras sea verdadera la variable se ejecuta
    entrada = input("-> ") #El usuario va a ingresar aquí la latra
    entrada_int = entrada.isdigit() #Solo para determinar si la entrada es un número
    if len(entrada) > 1 and entrada_int == False: #Si la entrada es mayor a 1 carácter y no es un número
        print("Solo se permite una letra") #Mensaje
    else: #Si no
        if  entrada.lower() in "aeiou" and entrada.lower() != "": #Si la entrada en minúscula está en (a,e,i,o,u) y esta no es un (↲)
            print("VOCAL") #Se trata de una vocal
        elif entrada == " ": #Si no y si la entrada es un espacio
            print("¡GRACIAS POR USAR EL SISTEMA!") #Agradecemos al usuario
            seguir = False #Cambiamos el valor de la variable para que se interrumpa el ciclo
        elif entrada == "": #Si no y si la entrada si es un (↲)
            print("ERROR: Inténtalo de nuevo") #No se ingresó nada y se solicita intentar de nuevo
        elif entrada_int == True: #Si no y si la entrada si es un número 
            if len(entrada) >  1: #Si el número tiene más de un dígito
                print(f"ERROR: {len(entrada)} números ingresados") #Indica cuántos números se ingresaron
            else: #Si solo tiene un dígito
                print("No se permiten números") #Aún así no necesitamos números
        else: #Si no es vocal, no quiere terminar, no es uno o varios números y no es un (↲)
            print("No Vocal") #No hay de otra más que sea una consonante (no vocal)