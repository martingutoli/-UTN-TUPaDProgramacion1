# 1) 
# for i in range(100):
#     print(i+1)

# 2) 
# n=(input("ingrese un numero: "))
# cantiDigit=0
# for digito in n:
#     cantiDigit+= 1
# print(f"el numero {n} tiene {cantiDigit} digitos")

# 3)
# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))
# if num1 > num2:
#     num1, num2 = num2, num1
# suma = 0
# for i in range(num1 + 1, num2):
#     suma += i
# print(f"La suma de los números entre {num1} y {num2} es: {suma}")

# 4)
# suma_total = 0
# numero = int(input("ingrese un numero entero (ingrese 0 para terminar): "))

# while numero != 0:
#     suma_total += numero
#     numero = int(input("ingrese otro numero entero (ingrese 0 para terminar): "))

# print(f"la suma total acumulada es: {suma_total}")

# 5)
# import random

# numero_aleatorio = random.randint(0, 9)
# intentos = 0
# adivinado = False

# print("adivina el numero entre 0 y 9")

# while not adivinado:
#   try:
#     intento_usuario = int(input("Ingresa un número: "))
#     intentos += 1

#     if intento_usuario == numero_aleatorio:
#       adivinado = True
#       print(f"muy bien! adivinaste el numero en {intentos} intentos")
#     elif intento_usuario < numero_aleatorio:
#       print("demasiado bajo. intenta de nuevo.")
#     else:
#       print("demasiado alto. intenta de nuevo.")
#   except ValueError:
#     print("por favor, ingresa un numero valido.")

# 6)
# for i in range (0,101):
#     print(101-i-1)

# 7)
# num=int(input("ingrese un numero: "))
# suma= 0
# for i in range(0,num+1):
#     suma+=i
# print(f"la suma de los numeros hasta el valor ingresado es: {suma}")

# 8)
# num_par=0
# num_impar=0
# mayor0=0
# menor0=0
# cantidad=100
# for i in range(cantidad):
#     num=int(input("ingrese otro numero: "))
    
#     if num%2==0:
#         num_par+=1
#     else:
#         num_impar+=1
#     if num>0:
#         mayor0+=1
#     else:
#         menor0+=1
# print(f"hay {num_par} pares, {num_impar} impares, {mayor0} mayores a 0, {menor0} menores a 0")

# 9)
# cantidad=6
# acum=0
# for i in range(cantidad):
#     num=int(input("ingrese un numero:"))
#     media= (num+acum)/6
#     acum+=num
# print(f"la media es {media}")

# 10)
# numero = input("Ingresa un número: ")
# numero_invertido = ""

# for digito in numero:
#   numero_invertido = digito + numero_invertido

# print("El número invertido es:", numero_invertido)