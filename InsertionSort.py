def insertion_sort(arr):
    # Percorre o array começando do segundo elemento
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move os elementos maiores que a chave para uma posição à frente
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = key

# Exemplo de uso
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Array ordenado:", arr)
