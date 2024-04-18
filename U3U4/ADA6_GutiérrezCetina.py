import networkx as nx
import matplotlib.pyplot as plt


class Estado:
    def __init__(self, nombre):
        self.nombre = nombre


class GrafoEstados:
    def __init__(self, estados):
        self.estados = estados
        self.num_estados = len(estados)
        self.matriz_costos = [[0] * self.num_estados for _ in range(self.num_estados)]

    def agregar_conexion(self, origen, destino, costo):
        origen_idx = self.estados.index(origen)
        destino_idx = self.estados.index(destino)
        self.matriz_costos[origen_idx][destino_idx] = costo
        self.matriz_costos[destino_idx][origen_idx] = costo

    def obtener_costo(self, recorrido):
        costo_total = 0
        for i in range(len(recorrido) - 1):
            origen = recorrido[i]
            destino = recorrido[i + 1]
            origen_idx = self.estados.index(origen)
            destino_idx = self.estados.index(destino)
            costo_total += self.matriz_costos[origen_idx][destino_idx]
        return costo_total

    def mostrar_relaciones(self):
        print("Matriz de Costos:")
        print("\t" + "\t".join([estado.nombre for estado in self.estados]))
        for i in range(self.num_estados):
            print(self.estados[i].nombre, end="\t")
            for j in range(self.num_estados):
                print("{:.1f}".format(self.matriz_costos[i][j]), end="\t")
            print()

    def mostrar_grafo(self):
        G = nx.Graph()
        for estado in self.estados:
            G.add_node(estado.nombre)
        for i in range(self.num_estados):
            for j in range(i + 1, self.num_estados):
                if self.matriz_costos[i][j] != 0:
                    G.add_edge(self.estados[i].nombre, self.estados[j].nombre, weight=self.matriz_costos[i][j])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold',
                arrowsize=20)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
        plt.show()


def ingresar_datos():
    estados = []
    for i in range(7):
        nombre = input(f"Ingrese el nombre del estado {i + 1}: ")
        estados.append(Estado(nombre))
    return estados

def ingresar_costos(estados):
    matriz_costos = [[0] * len(estados) for _ in range(len(estados))]
    for i in range(len(estados)):
        for j in range(i + 1, len(estados)):
            costo = float(input(f"Ingrese el costo de ir de {estados[i].nombre} a {estados[j].nombre}: "))
            matriz_costos[i][j] = costo
            matriz_costos[j][i] = costo
    return matriz_costos

estados = ingresar_datos()
matriz_costos = ingresar_costos(estados)
grafo = GrafoEstados(estados)
grafo.matriz_costos = matriz_costos

grafo.mostrar_relaciones()
grafo.mostrar_grafo()




