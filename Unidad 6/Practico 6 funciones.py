#1)
def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()


#2)
# def saludar_usuario(nombre):
#     return f"Hola {nombre}!"

# nombre_usuario = input("\nIngrese su nombre: ")
# print(saludar_usuario(nombre_usuario))


#3)
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# nombre = input("\nNombre: ")
# apellido = input("Apellido: ")
# edad = input("Edad: ")
# residencia = input("Residencia: ")

# informacion_personal(nombre, apellido, edad, residencia)


#4)
# import math

# def calcular_area_circulo(radio):
#     return math.pi * radio ** 2

# def calcular_perimetro_circulo(radio):
#     return 2 * math.pi * radio

# radio = float(input("\nIngrese el radio del círculo: "))
# print(f"Área: {calcular_area_circulo(radio):.2f}")
# print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")


#5)
# def segundos_a_horas(segundos):
#     return segundos / 3600

# seg = int(input("\nIngrese la cantidad de segundos: "))
# print(f"Equivale a: {segundos_a_horas(seg):.2f} horas")


#6)
# def tabla_multiplicar(numero):
#     print(f"\nTabla de multiplicar del {numero}")
#     for i in range(1, 11):
#         print(f"{numero} x {i} = {numero * i}")

# num_tabla = int(input("\nIngrese un número para la tabla: "))
# tabla_multiplicar(num_tabla)


#7)
# def operaciones_basicas(a, b):
#     suma = a + b
#     resta = a - b
#     multiplicacion = a * b
#     division = a / b if b != 0 else "Indefinida"
#     return suma, resta, multiplicacion, division

# a = float(input("\nIngrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))

# resultados = operaciones_basicas(a, b)
# print(f"Suma: {resultados[0]}")
# print(f"Resta: {resultados[1]}")
# print(f"Multiplicación: {resultados[2]}")
# print(f"División: {resultados[3]}")


#8)
# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)

# peso = float(input("\nIngrese su peso (kg): "))
# altura = float(input("Ingrese su altura (m): "))

# print(f"Su IMC es: {calcular_imc(peso, altura):.2f}")


#9)
# def celsius_a_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# temp_c = float(input("\nIngrese temperatura en °C: "))
# print(f"{temp_c}°C equivalen a {celsius_a_fahrenheit(temp_c):.2f}°F")


#10)
# def calcular_promedio(a, b, c):
#     return (a + b + c) / 3

# a = float(input("\nIngrese el primer número: "))
# b = float(input("Ingrese el segundo número: "))
# c = float(input("Ingrese el tercer número: "))

# print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
