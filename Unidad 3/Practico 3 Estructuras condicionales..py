# 1)
# edad= int(input("ingrese su edad: "))
# if edad>=18:
#     print("es mayor de edad")

# 2)
# nota = int(input("ingrese su nota: "))
# if nota>=6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

# 3)
# num = int(input("ingrese un numero par: "))
# if num%2==0:
#     print("Ha ingresado un número par")
# else:
#     print("Por favor, ingrese un número par")

# 4)
# edad = int(input("ingrese su edad: "))
# if edad<0:
#     print("No es una edad valida")
# elif edad<12:
#     print("Niño/a")
# elif edad>=12 and edad<=18:
#     print("Adolescente")
# elif edad>=18 and edad<=30:
#     print("Adulto/a joven")
# elif edad>=30:
#     print("Adulto/a")

# 5)
# contrasena = (input("ingrese una contraseña entre 8 y 14 caracteres: "))
# long_contrasena = int(len(contrasena))
# if long_contrasena>=8 and long_contrasena<=14:
#     print("Ha ingresado una contraseña correcta")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6)
# import random
# from statistics import mode, median, mean
# numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
# media = mean(numeros_aleatorios)
# moda = mode(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# print(numeros_aleatorios)
# print(media)
# print(moda)
# print(mediana)
# if media > mediana and mediana > moda:
#     print("Sesgo positivo o a la derecha")
# elif media < mediana and mediana < moda:
#     print("sesgo negativo o a la izquierda")
# elif media == mediana == moda:
#     print("sin sesgo")
# else:
#     print("no se cumple ninguna")

# 7)
# palabra = input("ingrese una palabra o frase: ")
# ultima_letra = palabra[-1]
# if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "u":
#     print(f"{palabra}!")
# else:
#     print(palabra)

# 8)
# nombre = input("ingrese su nombre: ")
# opcion = int(input("""elija la opcion para ver su nombre:" 
# "1: todo en mayuscula" \n
# "2: todo en minuscula" \n
# "3: primera letra en mayuscula y el resto en minuscula
#  """))
# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print (nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("la opcion no es correcta")

# 9)
# magnitud = float(input("ingrese la magnitud del terremoto: "))
# if magnitud<3:
#     print("Muy leve (imperceptible)")
# elif magnitud>=3 and magnitud<4:
#     print("Leve (ligeramente perceptible)")
# elif magnitud>=4 and magnitud<5:
#     print("Moderado (sentido por personas, pero generalmente no causa daños)")
# elif magnitud>=5 and magnitud<6:
#     print("Fuerte (puede causar daños en estructuras débiles)")
# elif magnitud>=6 and magnitud<7:
#     print("Muy Fuerte (puede causar daños significativos)")
# elif magnitud>=7:
#     print("Extremo (puede causar graves daños a gran escala)")

# 10)
# hemisferio = input("ingrese en que hemisferio se encuentra (n/s): ")
# mesAño = input("que mes es: ")
# dia = int(input("que dia es: "))
# if hemisferio=="n":
#     if (mesAño == "diciembre" and dia>=21 and dia<=31):
#         print("estas en invierno")
#     elif (mesAño == "enero" and dia>=1 and dia<=31):
#         print("estas en invierno")
#     elif (mesAño == "febrero" and dia>=1 and dia<=28):
#         print("estas en invierno")
#     elif (mesAño == "marzo" and dia>=1 and dia<=20):
#         print("estas en invierno")
#     elif (mesAño == "marzo" and dia>=21 and dia<=31):
#         print("estas en primavera")
#     elif (mesAño == "abril" and dia>=1 and dia<=31):
#         print("estas en primavera")
#     elif (mesAño == "mayo" and dia>=1 and dia<=31):
#         print("estas en primavera")
#     elif (mesAño == "junio" and dia>=1 and dia<=20):
#         print("estas en primavera")
#     elif (mesAño == "junio" and dia>=21 and dia<=30):
#         print("estas en verano")
#     elif (mesAño == "julio" and dia>=1 and dia<=31):
#         print("estas en verano")
#     elif (mesAño == "agosto" and dia>=1 and dia<=31):
#         print("estas en verano")
#     elif (mesAño == "septiembre" and dia>=1 and dia<=20):
#         print("estas en verano")
#     elif (mesAño == "septiembre" and dia>=21 and dia<=30):
#         print("estas en otoño")
#     elif (mesAño == "octubre" and dia>=1 and dia<=30):
#         print("estas en otoño")
#     elif (mesAño == "noviembre" and dia>=1 and dia<=31):
#         print("estas en otoño")
#     elif (mesAño == "diiembre" and dia>=1 and dia<=20):
#         print("estas en otoño")
# elif hemisferio=="s":
#     if (mesAño == "diciembre" and dia>=21 and dia<=31):
#         print("estas en verano")
#     elif (mesAño == "enero" and dia>=1 and dia<=31):
#         print("estas en verano")
#     elif (mesAño == "febrero" and dia>=1 and dia<=28):
#         print("estas en verano")
#     elif (mesAño == "marzo" and dia>=1 and dia<=20):
#         print("estas en verano")
#     elif (mesAño == "marzo" and dia>=21 and dia<=31):
#         print("estas en otoño")
#     elif (mesAño == "abril" and dia>=1 and dia<=31):
#         print("estas en otoño")
#     elif (mesAño == "mayo" and dia>=1 and dia<=31):
#         print("estas en otoño")
#     elif (mesAño == "junio" and dia>=1 and dia<=20):
#         print("estas en otoño")
#     elif (mesAño == "junio" and dia>=21 and dia<=30):
#         print("estas en invierno")
#     elif (mesAño == "julio" and dia>=1 and dia<=31):
#         print("estas en invierno")
#     elif (mesAño == "agosto" and dia>=1 and dia<=31):
#         print("estas en invierno")
#     elif (mesAño == "septiembre" and dia>=1 and dia<=20):
#         print("estas en invierno")
#     elif (mesAño == "septiembre" and dia>=21 and dia<=30):
#         print("estas en primavera")
#     elif (mesAño == "octubre" and dia>=1 and dia<=30):
#         print("estas en primavera")
#     elif (mesAño == "noviembre" and dia>=1 and dia<=31):
#         print("estas en primavera")
#     elif (mesAño == "diiembre" and dia>=1 and dia<=20):
#         print("estas en primavera")



