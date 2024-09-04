def selection_sort(arr):
    # Percorre toda a lista
    for i in range(len(arr)):
        # Encontra o menor elemento na parte não ordenada
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Troca o menor elemento encontrado com o primeiro elemento da parte não ordenada
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Array ordenado:", arr)
