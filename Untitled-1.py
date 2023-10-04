import time
import random
def insertion_sort(arr):
    # Percorre a lista a partir do segundo elemento até o final
    for i in range(1, len(arr)):
        key = arr[i]  # Elemento atual que será inserido na partição ordenada
        j = i - 1  # Índice do elemento anterior na partição ordenada

        # Move os elementos maiores para a direita até encontrar a posição correta para inserir o elemento atual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Desloca o elemento maior uma posição à direita
            j -= 1

        arr[j + 1] = key  # Insere o elemento atual na posição correta

    return arr
lista=[random.randrange(1,150000) for i in range(0,15000)]
#lista = random.randrange(1,100)
print("Lista original:", lista)
inicio = time.time()
lista_ordenada = insertion_sort(lista)
final = time.time()

print("Lista ordenada:", lista_ordenada)
print("tempo total:", final - inicio)