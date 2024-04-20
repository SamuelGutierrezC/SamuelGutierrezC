class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class Arbol:
    def __init__(self):
        self.raiz = None

    def agregar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._agregar_recursivo(self.raiz, dato)

    def _agregar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._agregar_recursivo(nodo.derecha, dato)

    def imprimir_inorden(self):
        self._imprimir_inorden_recursivo(self.raiz)
        print()

    def _imprimir_inorden_recursivo(self, nodo):
        if nodo is not None:
            self._imprimir_inorden_recursivo(nodo.izquierda)
            print(nodo.dato, end=' ')
            self._imprimir_inorden_recursivo(nodo.derecha)

    def obtener_raiz(self):
        if self.raiz:
            return self.raiz.dato
        else:
            return None

    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierda is None and nodo.derecha is None:
            return 1
        return self._contar_hojas_recursivo(nodo.izquierda) + self._contar_hojas_recursivo(nodo.derecha)

    def contar_niveles(self):
        return self._contar_niveles_recursivo(self.raiz)

    def _contar_niveles_recursivo(self, nodo):
        if nodo is None:
            return 0
        else:
            izquierda = self._contar_niveles_recursivo(nodo.izquierda)
            derecha = self._contar_niveles_recursivo(nodo.derecha)
            return max(izquierda, derecha) + 1

    def tipo_arbol(self):
        if self.raiz:
            return "Árbol binario"
        else:
            return "Árbol vacío"

if __name__ == "__main__":
    arbol = Arbol()
    while True:
        opcion = input("Ingrese 'a' para agregar un número al árbol, 'r' para obtener la raíz, 'h' para contar las hojas, 'n' para contar los niveles, 't' para obtener el tipo del árbol o 'q' para salir: ")
        if opcion == 'a':
            obj = int(input("Ingrese un número para agregar al árbol: "))
            arbol.agregar(obj)
        elif opcion == 'r':
            print("La raíz del árbol es:", arbol.obtener_raiz())
        elif opcion == 'h':
            print("El árbol tiene", arbol.contar_hojas(), "hojas.")
        elif opcion == 'n':
            print("El árbol tiene", arbol.contar_niveles(), "niveles.")
        elif opcion == 't':
            print("El tipo del árbol es:", arbol.tipo_arbol())
        elif opcion == 'q':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")


