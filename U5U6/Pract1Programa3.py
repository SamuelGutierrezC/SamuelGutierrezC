class Seleccion:
    def ordenar(self, arr):
        n = len(arr)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print("Paso", i+1, ": ", arr)


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    seleccion = Seleccion()
    print("Arreglo original:", arr)
    seleccion.ordenar(arr)
    print("Arreglo ordenado:", arr)


if __name__ == "__main__":
    main()
