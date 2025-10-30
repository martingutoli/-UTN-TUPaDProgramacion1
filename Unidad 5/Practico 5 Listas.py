#1)
notas = [7, 5, 9, 10, 8, 6, 4, 9, 7, 8]

print("notas de los estudiantes: ")
for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print(f"\npromedio: {promedio:.2f}")
print("nota mas alta:", max(notas))
print("nota mas baja:", min(notas))

#2)
# productos = []
# for i in range(5):
#     prod = input(f"ingrese el producto {i+1}: ")
#     productos.append(prod)

# print("\nlista ordenada alfabeticamente:")
# lista_ordenada = sorted(productos)
# for p in lista_ordenada:
#     print(p)

# eliminar = input("\ningrese el producto a eliminar: ")
# if eliminar in productos:
#     productos.remove(eliminar)

# print("\nlista actualizada:")
# for p in productos:
#     print(p)

#3)
# import random

# numeros = []
# for _ in range(15):
#     numeros.append(random.randint(1, 100))

# pares = []
# impares = []

# for n in numeros:
#     if n % 2 == 0:
#         pares.append(n)
#     else:
#         impares.append(n)

# print("\ncantidad de pares:", len(pares))
# print("cantidad de impares:", len(impares))

#4)
# lista_repetidos = [1, 2, 3, 2, 5, 1, 6, 3, 2]
# sin_repetidos = []

# for x in lista_repetidos:
#     if x not in sin_repetidos:
#         sin_repetidos.append(x)

# print("\nlista sin repetidos:")
# for x in sin_repetidos:
#     print(x)

#5)
# estudiantes = ["ana", "luis", "marta", "diego", "sofía", "juan", "lara", "tomas"]

# opcion = input("\n¿desea agregar (A) o eliminar (E) un estudiante? ").upper()

# if opcion == "A":
#     nuevo = input("ingrese el nombre a agregar: ")
#     estudiantes.append(nuevo)
# elif opcion == "E":
#     borrar = input("ingrese el nombre a eliminar: ")
#     if borrar in estudiantes:
#         estudiantes.remove(borrar)

# print("\nlista actualizada:")
# for e in estudiantes:
#     print(e)

#6)
# lista_numeros = [1, 2, 3, 4, 5, 6, 7]
# ultimo = lista_numeros[-1]

# for i in range(len(lista_numeros) - 1, 0, -1):
#     lista_numeros[i] = lista_numeros[i - 1]
# lista_numeros[0] = ultimo

# print("\nlista rotada:")
# for n in lista_numeros:
#     print(n)

#7)
# temperaturas = [
#     [10, 20], [12, 22], [9, 19], [11, 25], [8, 18], [10, 21], [13, 24]
# ]

# suma_min = 0
# suma_max = 0
# mayor_amp = 0
# dia_mayor_amp = 0

# for i in range(7):
#     minima = temperaturas[i][0]
#     maxima = temperaturas[i][1]
#     suma_min += minima
#     suma_max += maxima
#     amplitud = maxima - minima
#     if amplitud > mayor_amp:
#         mayor_amp = amplitud
#         dia_mayor_amp = i + 1

# print(f"\npromedio minimas: {suma_min / 7:.2f}")
# print(f"promedio maximas: {suma_max / 7:.2f}")
# print("mayor amplitud termica en el dia:", dia_mayor_amp)

#8)
# notas_est = [
#     [7, 8, 6],
#     [5, 7, 9],
#     [10, 9, 8],
#     [6, 6, 7],
#     [9, 8, 10]
# ]

# print("\npromedio por estudiante:")
# for fila in notas_est:
#     print(sum(fila) / len(fila))

# print("\npromedio por materia:")
# for col in range(3):
#     suma = 0
#     for fila in range(5):
#         suma += notas_est[fila][col]
#     print(suma / 5)

#9)
# tablero = [["-", "-", "-"],
#            ["-", "-", "-"],
#            ["-", "-", "-"]]

# for turno in range(5):
#     print("\ntablero:")
#     for fila in tablero:
#         print(fila)

#     jugador = "X" if turno % 2 == 0 else "O"
#     f = int(input(f"ingrese fila (0-2) para {jugador}: "))
#     c = int(input(f"ingrese columna (0-2) para {jugador}: "))

#     tablero[f][c] = jugador


# print("\ntablero final:")
# for fila in tablero:
#     print(fila)

#10)
# ventas = [
#     [10, 12, 8, 9, 11, 7, 10],
#     [15, 14, 18, 20, 17, 16, 19],
#     [5, 7, 6, 8, 9, 4, 7],
#     [9, 10, 11, 12, 13, 14, 15]
# ]

# print("\ntotal vendido por producto:")
# totales_productos = []
# for fila in ventas:
#     total = sum(fila)
#     totales_productos.append(total)
#     print(total)

# print("\ndia con mayores ventas:")
# ventas_diarias = []
# for col in range(7):
#     suma = 0
#     for fila in range(4):
#         suma += ventas[fila][col]
#     ventas_diarias.append(suma)

# print("dia:", ventas_diarias.index(max(ventas_diarias)) + 1)

# print("\nproducto mas vendido en la semana:")
# print("producto:", totales_productos.index(max(totales_productos)) + 1)
