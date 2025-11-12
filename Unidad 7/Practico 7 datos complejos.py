# 1)
# precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450}

# precios_frutas['naranja'] = 1200
# precios_frutas['manzana'] = 1500
# precios_frutas['pera'] = 2300

# print(precios_frutas)

# 2)
# precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450, 'naranja': 1200, 'manzana': 1500, 'pera': 2300 }
# precios_frutas['banana'] = 1330
# precios_frutas['manzana'] = 1700
# precios_frutas['melon'] = 2800

# print(precios_frutas)

# 3)
# precios_frutas = {'banana': 1200, 'anana': 2500, 'melon': 3000, 'uva': 1450, 'naranja': 1200, 'manzana': 1500, 'pera': 2300 }
# lista_frutas = list(precios_frutas.keys())
# print(lista_frutas)

# 4)
# agenda = {}

# for _ in range(5):
#     nombre = input("ingrese nombre del contacto: ")
#     telefono = input("ingrese telefono: ")
#     agenda[nombre] = telefono

# consulta = input("ingrese el nombre a consultar: ")

# if consulta in agenda:
#     print("telefono:", agenda[consulta])
# else:
#     print("no se encontro el contacto.")

# 5)
# frase = input("ingrese una frase: ").lower()

# palabras = frase.split()
# unicas = set(palabras)

# contador = {}
# for palabra in palabras:
#     contador[palabra] = contador.get(palabra, 0) + 1

# print("palabras unicas:", unicas)
# print("frecuencia de palabras:", contador)

# 6)
# alumnos = {}

# for _ in range(3):
#     nombre = input("nmbre del alumno: ")
#     n1 = float(input("nota 1: "))
#     n2 = float(input("nota 2: "))
#     n3 = float(input("nota 3: "))
#     alumnos[nombre] = (n1, n2, n3)

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / 3
#     print(f"{nombre} - promedio: {promedio:.2f}")

# 7)
# parcial1 = {1, 2, 3, 4, 5}
# parcial2 = {4, 5, 6, 7}

# ambos = parcial1 & parcial2
# solo_uno = parcial1 ^ parcial2
# al_menos_uno = parcial1 | parcial2

# print("aprobaron ambos:", ambos)
# print("aprobaron solo uno:", solo_uno)
# print("aprobaron al menos uno:", al_menos_uno)

# 8)
# stock = {"arroz": 10, "fideos": 5, "azucar": 3}

# producto = input("ingrese producto a consultar/agregar: ")

# if producto in stock:
#     agregar = int(input("cuantas unidades agregar?: "))
#     stock[producto] += agregar
# else:
#     nuevo_stock = int(input("no existe. ingrese stock inicial: "))
#     stock[producto] = nuevo_stock

# print(stock)

# 9)
# agenda = {
#     (1, "10:00"): "dentista",
#     (3, "15:00"): "reunion",
#     (5, "09:30"): "gimnasio"
# }

# dia = int(input("ingrese dia: "))
# hora = input("ingrese hora (HH:MM): ")

# clave = (dia, hora)

# if clave in agenda:
#     print("actividad:", agenda[clave])
# else:
#     print("no hay actividad programada.")

# 10)
# paises = {
#     "argentina": "buenos aires",
#     "chile": "santiago",
#     "uruguay": "montevideo"
# }

# capitales = {capital: pais for pais, capital in paises.items()}

# print(capitales)


