import os

NOMBRE_ARCHIVO = "productos.txt"

def leer_productos(path):
    productos = []
    if not os.path.exists(path):
        open(path, "a", encoding="utf-8").close()
        return productos

    with open(path, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) != 3:
                continue
            nombre, precio_str, cantidad_str = partes
            try:
                precio = float(precio_str)
            except ValueError:
                continue
            try:
                cantidad = int(float(cantidad_str))
            except ValueError:
                continue
            producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
            productos.append(producto)
    return productos

def mostrar_productos(productos):
    if not productos:
        print("no hay productos para mostrar.")
        return
    for p in productos:
        print(f"producto: {p['nombre']} | precio: ${p['precio']} | cantidad: {p['cantidad']}")

def pedir_producto_por_teclado():
    nombre = input("nombre del producto: ").strip()
    if not nombre:
        print("nombre vacio. producto descartado.")
        return None
    while True:
        precio_in = input("precio (ej. 120.5): ").strip().replace("$","")
        try:
            precio = float(precio_in)
            break
        except ValueError:
            print("precio invalido. intenta de nuevo.")
    while True:
        cantidad_in = input("cantidad (ej. 30): ").strip()
        try:
            cantidad = int(float(cantidad_in))
            break
        except ValueError:
            print("cantidad invalida. intenta de nuevo.")
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def buscar_producto(productos, nombre_buscar):
    nombre_buscar = nombre_buscar.strip().lower()
    encontrados = [p for p in productos if p["nombre"].lower() == nombre_buscar]
    return encontrados

def guardar_productos(path, productos):
    # Sobrescribimos el archivo con todos los productos actuales
    with open(path, "w", encoding="utf-8") as f:
        for p in productos:
            linea = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
            f.write(linea)

def main():
    print("=== gestión de productos ===")
    productos = leer_productos(NOMBRE_ARCHIVO)
    print("\nproductos actuales:")
    mostrar_productos(productos)

    # Permitir agregar uno o varios productos
    while True:
        agregar = input("\nqueres agregar un producto? (s/n): ").strip().lower()
        if agregar in ("s","si"):
            nuevo = pedir_producto_por_teclado()
            if nuevo:
                productos.append(nuevo)
                print(f"producto '{nuevo['nombre']}' agregado en memoria.")
        elif agregar in ("n","no",""):
            break
        else:
            print("respuesta no valida. ingresa 's' o 'n'.")

    nombre_buscar = input("\ningresa el nombre de un producto para buscar (o ENTER para omitir): ").strip()
    if nombre_buscar:
        resultados = buscar_producto(productos, nombre_buscar)
        if resultados:
            print(f"\nse encontraron {len(resultados)} coincidencia(s):")
            for r in resultados:
                print(f"producto: {r['nombre']} | precio: ${r['precio']} | cantidad: {r['cantidad']}")
        else:
            print("el producto no existe en la lista.")

    guardar_productos(NOMBRE_ARCHIVO, productos)
    print(f"\nse guardaron {len(productos)} producto(s) en '{NOMBRE_ARCHIVO}'.")
    print("programa finalizado.")

if __name__ == "__main__":
    main()
