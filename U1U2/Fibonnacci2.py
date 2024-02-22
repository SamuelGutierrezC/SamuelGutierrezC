def fibonacciI(n):
    n0 = 0
    n1 = 1
    fib = 0
    if n == 0 or n == 1:
        fib = n
    else:
        i = 2
        while i <= n:
            fib = n0 + n1
            n0 = n1
            n1 = fib
            i += 1
    return fib

def main():
    n = int(input("Ingresa un número para calcular la serie de Fibonacci: "))
    if n < 0:
        print("Por favor, ingresa un número no negativo.")
        return

    print("La serie de Fibonacci para el número ingresado es:")
    for i in range(n):
        print(fibonacciI(i), end=" ")

if __name__ == "__main__":
    main()
