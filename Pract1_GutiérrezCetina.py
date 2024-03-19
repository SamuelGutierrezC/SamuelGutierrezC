class Pila:
    def __init__(self, capacidad_maxima):
        self.items = []
        self.capacidad_maxima = capacidad_maxima

    def esta_vacia(self):
        return len(self.items) == 0

    def esta_llena(self):
        return len(self.items) == self.capacidad_maxima

    def insertar(self, elemento):
        if not self.esta_llena():
            self.items.append(elemento)
            print(f"Insertar ({elemento})")
            print("Pila:", self.items)
            print("Tope:", len(self.items))
        else:
            print("Error: Desbordamiento")

    def eliminar(self):
        if not self.esta_vacia():
            elemento = self.items.pop()
            print(f"Eliminar ({elemento})")
            print("Pila:", self.items)
            print("Tope:", len(self.items))
        else:
            print("Error: Subdesbordamiento")


pila = Pila(8)
pila.insertar("X")  # a
pila.insertar("Y")  # b
pila.eliminar()     # c
pila.eliminar()     # d
pila.eliminar()     # e
pila.insertar("V")  # f
pila.insertar("W")  # g
pila.eliminar()     # h
pila.insertar("R")  # i

print("Elementos en la pila:", len(pila.items))
