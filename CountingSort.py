def counting_sort(arr):
    # Encontra o valor máximo para definir o tamanho do array auxiliar
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # Conta as ocorrências de cada elemento
    for num in arr:
        count[num] += 1

    # Calcula os índices acumulados no array de contagem
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Preenche o array de saída com os elementos ordenados
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1

    return output

# Exemplo de uso
arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(arr)
print("Array ordenado (Counting Sort):", sorted_arr)
