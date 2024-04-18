import networkx as nx
import matplotlib.pyplot as plt


class Estado:
    def __init__(self, nombre):
        self.nombre = nombre


class Conexion:
    def __init__(self, origen, destino, costo):
        self.origen = origen
        self.destino = destino
        self.costo = costo


class GrafoEstados:
    def __init__(self):
        self.grafo = nx.DiGraph()

    def agregar_estado(self, estado):
        self.grafo.add_node(estado.nombre)

    def agregar_conexion(self, conexion):
        self.grafo.add_edge(conexion.origen.nombre, conexion.destino.nombre, costo=conexion.costo)

    def obtener_costo(self, recorrido):
        costo_total = 0
        for i in range(len(recorrido) - 1):
            origen = recorrido[i]
            destino = recorrido[i + 1]
            costo_total += self.grafo.edges[origen, destino]['costo']
        return costo_total

    def mostrar_grafo(self):
        nx.draw(self.grafo, with_labels=True, node_size=1500, node_color='skyblue', font_size=10, font_weight='bold',
                arrowsize=20)
        labels = nx.get_edge_attributes(self.grafo, 'costo')
        nx.draw_networkx_edge_labels(self.grafo, pos=nx.spring_layout(self.grafo), edge_labels=labels)
        plt.show()


def ingresar_datos():
    estados = []
    for i in range(7):
        nombre = input(f"Ingrese el nombre del estado {i + 1}: ")
        estados.append(Estado(nombre))

    conexiones = []
    for i in range(7):
        for j in range(i + 1, 7):
            costo = float(input(f"Ingrese el costo de ir de {estados[i].nombre} a {estados[j].nombre}: "))
            conexiones.append(Conexion(estados[i], estados[j], costo))
            conexiones.append(Conexion(estados[j], estados[i], costo))

    return estados, conexiones


def recorrido_sin_repetir(grafo):
    recorrido = list(nx.topological_sort(grafo.grafo))
    costo = grafo.obtener_costo(recorrido)
    return recorrido, costo


def recorrido_con_repeticion(grafo):
    recorrido = list(nx.simple_cycles(grafo.grafo))[0]
    costo = grafo.obtener_costo(recorrido)
    return recorrido, costo


estados, conexiones = ingresar_datos()
grafo = GrafoEstados()
for estado in estados:
    grafo.agregar_estado(estado)

for conexion in conexiones:
    grafo.agregar_conexion(conexion)
grafo.mostrar_grafo()
print("Recorrido sin repetir estados:")
recorrido_sin_rep, costo_sin_rep = recorrido_sin_repetir(grafo)
print("Recorrido:", recorrido_sin_rep)
print("Costo total:", costo_sin_rep)

print("\nRecorrido con repetición de al menos un estado:")
recorrido_con_rep, costo_con_rep = recorrido_con_repeticion(grafo)
print("Recorrido:", recorrido_con_rep)
print("Costo total:", costo_con_rep)


