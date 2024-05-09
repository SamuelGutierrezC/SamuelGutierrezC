class Insercion:
    def ordenar(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            print("Paso", i, ": ", arr)


def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    insercion = Insercion()
    print("Arreglo original:", arr)
    insercion.ordenar(arr)
    print("Arreglo ordenado:", arr)


if __name__ == "__main__":
    main()
