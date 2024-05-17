def intercalacion(lista1, lista2):
    i, j = 0, 0
    lista_ordenada = []

    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            lista_ordenada.append(lista1[i])
            i += 1
        else:
            lista_ordenada.append(lista2[j])
            j += 1

    while i < len(lista1):
        lista_ordenada.append(lista1[i])
        i += 1

    while j < len(lista2):
        lista_ordenada.append(lista2[j])
        j += 1

    return lista_ordenada


lista1 = [1, 3, 5, 7]
lista2 = [2, 4, 6, 8]
print(intercalacion(lista1, lista2))
