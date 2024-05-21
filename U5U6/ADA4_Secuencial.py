class BusquedaSecuencial:
    def __init__(self, lista):
        self.lista = lista

    def buscar(self, objetivo):
        for i in range(len(self.lista)):
            if self.lista[i] == objetivo:
                return i
        return -1


nombres = input("Ingrese los nombres de los estudiantes separados por comas: ").split(",")
nombres = [nombre.strip() for nombre in nombres]
nombre_a_buscar = input("Ingrese el nombre a buscar: ").strip()
busqueda = BusquedaSecuencial(nombres)
resultado = busqueda.buscar(nombre_a_buscar)

if resultado != -1:
    print(f"{nombre_a_buscar} encontrado en la posición {resultado}")
else:
    print(f"{nombre_a_buscar} no se encuentra en la lista")
