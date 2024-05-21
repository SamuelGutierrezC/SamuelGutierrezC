class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar_contacto(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        else:
            return None


agenda = Agenda()
while True:
    nombre = input("Ingrese el nombre del contacto (o 'fin' para terminar): ").strip()
    if nombre.lower() == 'fin':
        break
    telefono = input(f"Ingrese el número de teléfono de {nombre}: ").strip()
    agenda.agregar_contacto(nombre, telefono)
nombre_a_buscar = input("Ingrese el nombre del contacto a buscar: ").strip()
resultado = agenda.buscar_contacto(nombre_a_buscar)

if resultado:
    print(f"El número de teléfono de {nombre_a_buscar} es {resultado}")
else:
    print(f"{nombre_a_buscar} no se encuentra en la agenda")
