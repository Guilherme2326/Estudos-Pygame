import time
import random

def insertion_sort(arr):
    for i in range(1, 150000):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j+1] = key
    return arr

def main():
    lista = []
    for _ in range(0, 150000):
        lista.append(random.randrange(1, 150000))
    #lista = [random.randrange(1, 150000) for i in range(0, 150000)]
    print("Lista original:", lista)
    inicio = time.time()
    lista_ordenada = insertion_sort(lista)
    final = time.time()

    print("Lista ordenada:", lista_ordenada)
    print("tempo total:", final - inicio)

if __name__ == "__main__":
    main()