# Lista para almacenar productos como diccionarios
productos = []
def cargar_datos():
    
    try:
        with open('producto.txt', 'r') as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                producto = {
                    "nombre": nombre, #entrada producto
                    "precio": float(precio), #entrada producto
                    "cantidad": int(cantidad) #cantidad a guardar
                }
                productos.append(producto)
    except FileNotFoundError:
        pass  # si no existe el archivo no se guarda

def guardar_datos():
    
    with open('producto.txt', 'w') as file: 
        for p in productos: 
            file.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

def añadir_producto():
   
    nombre = input("Escriba el nombre de su producto: ")
    precio = float(input("ingrse el precio del mismo: "))
    cantidad = int(input("Introduce la cantidad em stock: "))
    
    #almacenar los datos en un diccionario
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    
    productos.append(producto)
    print(f"Producto '{nombre}' añadido correctamente.")

def ver_productos():

    if not productos:
        print("No hay productos en stock.")
        return
    
    print("Productos en stock:")
    for p in productos:
        print(f"Nombre: {p['nombre']}, Precio: {p['precio']}, Cantidad: {p['cantidad']}")

def actualizar_producto():
  
    nombre = input("Ingrese el nombre del item que deseas renovar: ")
    for p in productos:
        if p['nombre'] == nombre:
            nuevo_nombre = input("Escriba el nuevo nombre del item: ")
            if nuevo_nombre:
                p['nombre'] = nuevo_nombre # sutituye el nombre
            nuevo_precio = input("Ingrese el nuevo precio: ")
            if nuevo_precio:
                p['precio'] = float(nuevo_precio) #sutituye el precio
            nueva_cantidad = input("Especifique la nueva cantidad: ")
            if nueva_cantidad:
                p['cantidad'] = int(nueva_cantidad) # sutituye la cantidad
            print(f"Producto '{nombre}' actualizado.")
            return
    
    print(f"Producto '{nombre}' sin stock.")

def eliminar_producto():
    
    nombre = input("Ingrese el nombre del articulo que deseas deshechar: ")
    global productos
    productos = [p for p in productos if p['nombre'] != nombre]
    
    print(f"Producto '{nombre}' deshechado." if len(productos) < len(productos) else f"Producto '{nombre}' eliminado.")

def menu():
  
    cargar_datos() 
    while True:
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            print("Info Guardada ")
            break
        else:
            print("Por favor, elija una opción correcta.")

menu()