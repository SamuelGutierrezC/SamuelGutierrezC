class Burbuja:
    def ordenar(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    print("Paso", i+1, ": ", arr)

def main():
    arr = [64, 34, 25, 12, 22, 11, 90]
    burbuja = Burbuja()
    print("Arreglo original:", arr)
    burbuja.ordenar(arr)
    print("Arreglo ordenado:", arr)


if __name__ == "__main__":
    main()
