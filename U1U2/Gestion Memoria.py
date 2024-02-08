class MemoriaEstatica:
    def main(self):
        calificaciones = [0] * 5

        for i in range(5):
            calificacion = int(input("Captura la calificación: "))
            calificaciones[i] = calificacion

        print("Calificaciones ingresadas:", calificaciones)


memoria_estatica = MemoriaEstatica()
memoria_estatica.main()
class MemoriaDinamica:
    def main(self):
        frutas = ["mango", "manzana", "banana", "uvas"]
        print(frutas)
        frutas.pop(0)
        frutas.remove("manzana")
        frutas.append("sandia")
        print(frutas)


memoria_dinamica = MemoriaDinamica()
memoria_dinamica.main()