class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, nombre, precio):
        self.productos[nombre] = precio

    def buscar_producto(self, nombre):
        if nombre in self.productos:
            return self.productos[nombre]
        else:
            return None


inventario = Inventario()
while True:
    nombre = input("Ingrese el nombre del producto (o 'fin' para terminar): ").strip()
    if nombre.lower() == 'fin':
        break
    precio = float(input(f"Ingrese el precio de {nombre}: ").strip())
    inventario.agregar_producto(nombre, precio)
nombre_a_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
resultado = inventario.buscar_producto(nombre_a_buscar)

if resultado is not None:
    print(f"El precio de {nombre_a_buscar} es ${resultado}")
else:
    print(f"{nombre_a_buscar} no se encuentra en el inventario")
