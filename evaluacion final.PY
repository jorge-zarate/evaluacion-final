productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']

}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [349990, 1],
    'FS1230HD': [249990, 0]
}


def stock_marca():
    marca = input("Ingrese marca a consultar: ").lower()
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            if modelo in stock:
                total += stock[modelo][1]
    print(f"El stock es: {total}")


def busqueda_precio():
    while True:
        try:
            minimo = int(input("Ingrese precio mínimo: "))
            maximo = int(input("Ingrese precio máximo: "))
            break
        except:
            print("Debe ingresar valores enteros!!")
    
    encontrados = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if cantidad > 0 and minimo <= precio <= maximo:
            marca = productos[modelo][0]
            encontrados.append(f"{marca}–{modelo}")
    
    if encontrados:
        encontrados.sort()
        print("Los notebooks entre los precios consultados son:", encontrados)
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio():
    modelo = input("Ingrese modelo a actualizar: ")
    if modelo in stock:
        try:
            nuevo_precio = int(input("Ingrese precio nuevo: "))
            stock[modelo][0] = nuevo_precio
            print("Precio actualizado!!")
        except:
            print("El precio debe ser un número entero!")
    else:
        print("El modelo no existe!!")


while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        stock_marca()
    
    elif opcion == "2":
        busqueda_precio()
    
    elif opcion == "3":
        while True:
            actualizar_precio()
            respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta != "s":
                break
    
    elif opcion == "4":
        print("Programa finalizado.")
        break
    
    else:
        print("Debe seleccionar una opción válida!!")


def stock_marca():
    marca = input("Ingrese marca a consultar: ").lower()
    total = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            if modelo in stock:
                total += stock[modelo][1]
    print(f"El stock es: {total}")


def busqueda_precio():
    while True:
        try:
            minimo = int(input("Ingrese precio mínimo: "))
            maximo = int(input("Ingrese precio máximo: "))
            break
        except:
            print("Debe ingresar valores enteros!!")
    
    encontrados = []
    for modelo, datos in stock.items():
        precio, cantidad = datos
        if cantidad > 0 and minimo <= precio <= maximo:
            marca = productos[modelo][0]
            encontrados.append(f"{marca}–{modelo}")
    
    if encontrados:
        encontrados.sort()
        print("Los notebooks entre los precios consultados son:", encontrados)
    else:
        print("No hay notebooks en ese rango de precios.")


def actualizar_precio():
    modelo = input("Ingrese modelo a actualizar: ")
    if modelo in stock:
        try:
            nuevo_precio = int(input("Ingrese precio nuevo: "))
            stock[modelo][0] = nuevo_precio
            print("Precio actualizado!!")
        except:
            print("El precio debe ser un número entero!")
    else:
        print("El modelo no existe!!")


while True:
    print("\n*** MENU PRINCIPAL ***")
    print("1. Stock marca.")
    print("2. Búsqueda por precio.")
    print("3. Actualizar precio.")
    print("4. Salir.")
    
    opcion = input("Ingrese opción: ")
    
    if opcion == "1":
        stock_marca()
    
    elif opcion == "2":
        busqueda_precio()
    
    elif opcion == "3":
        while True:
            actualizar_precio()
            respuesta = input("Desea actualizar otro precio (s/n)?: ").lower()
            if respuesta != "s":
                break
    
    elif opcion == "4":
        print("Programa finalizado.")
        break
    
    else:
        print("Debe seleccionar una opción válida!!")
