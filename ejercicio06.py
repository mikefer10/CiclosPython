'''
Programa que pide números (se pide por teclado la cantidad de 
números a introducir). Informa cuántos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
'''
#Solicitamos al usuario con cuántos números vamos a trabajar
cantidad = int(input("¿Cuántos números deseas ingresar?: "))

#La variable aumantará en cada iteración vale inicialmente 1 porque primero pedimos el número 1, no el 0
contador = 1
#Variable que representará (cuántos números son mayores a 0)
may = 0
#Opuesto al enterior esta representará (cuántos números son menores a 0)
men = 0
#Esta representa cuántos son 0
cero = 0

#Ocupamos el ciclo (while), pero pudimos usar el (for), es a conveniencia
while contador <= cantidad: #Mientras el valor del contador sea menor al límite (cantidad), se ejecuta
    num = int(input(f"Número {contador} > ")) #Recibimos cada número y lo guardamos en (num)
    if num > 0: #Para determinar si es un número mayor a cero
        may += 1 #Aumentamos en 1
    elif num < 0: #Para determinar si un número es menor a cero
        men += 1 #Incrementamos en 1 
    elif num == 0: #Para saber si es igualm a cero
        cero += 1 #Sumamos 1 a lo que tenía la variable
    contador = contador + 1 #Este es el contador de (while), y si no lo aumentamos se hace infinito 

#Mostramos lo que se obtuvo de la ejecución (pudimos usar 3 líneas para este solo comentario)
print(f"Recibimos tus valores:\nMAYORES A CERO: {may}\nMENORES A CERO: {men}\nCEROS: {cero}")   