def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left

    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)

def heap_sort_min(arr):
    n = len(arr)

    # Constrói o Min-Heap
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, n, i)

    # Extrai os elementos do heap um por um
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        min_heapify(arr, i, 0)

# Exemplo de uso
arr = [12, 11, 13, 5, 6, 7]
heap_sort_min(arr)
print("Array ordenado (Heap Mínimo):", arr)
