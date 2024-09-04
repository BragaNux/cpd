def heapify(arr, n, i):
    # Inicializa o maior como raiz
    largest = i
    left = 2 * i + 1    # filho da esquerda
    right = 2 * i + 2   # filho da direita

    # Se o filho da esquerda for maior que a raiz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Se o filho da direita for maior que o maior até agora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior não for a raiz
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # faz a troca

        # Heapifica a sub-árvore afetada
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Constrói um heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai os elementos do heap um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # move a raiz atual para o final
        heapify(arr, i, 0)

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
print("Array ordenado:", arr)
