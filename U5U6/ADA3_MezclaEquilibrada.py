def mezcla_equilibrada(lista):
    def dividir(lista):
        return (lista[:len(lista) // 2], lista[len(lista) // 2:])

    def mezclar(lista1, lista2):
        resultado = []
        while lista1 and lista2:
            if lista1[0] < lista2[0]:
                resultado.append(lista1.pop(0))
            else:
                resultado.append(lista2.pop(0))
        resultado.extend(lista1 if lista1 else lista2)
        return resultado

    if len(lista) <= 1:
        return lista

    izquierda, derecha = dividir(lista)
    izquierda = mezcla_equilibrada(izquierda)
    derecha = mezcla_equilibrada(derecha)

    return mezclar(izquierda, derecha)


lista = [38, 27, 43, 3, 9, 82, 10]
print(mezcla_equilibrada(lista))
