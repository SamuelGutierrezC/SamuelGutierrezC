class BusquedaBinaria:
    def __init__(self, lista):
        self.lista = sorted(lista)

    def buscar(self, objetivo):
        inicio = 0
        fin = len(self.lista) - 1

        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.lista[medio] == objetivo:
                return medio
            elif self.lista[medio] < objetivo:
                inicio = medio + 1
            else:
                fin = medio - 1

        return -1


numeros = input("Ingrese los números separados por comas: ").split(",")
numeros = [int(numero.strip()) for numero in numeros]
numero_a_buscar = int(input("Ingrese el número a buscar: ").strip())
busqueda = BusquedaBinaria(numeros)
resultado = busqueda.buscar(numero_a_buscar)

if resultado != -1:
    print(f"{numero_a_buscar} encontrado en la posición {resultado}")
else:
    print(f"{numero_a_buscar} no se encuentra en la lista")
