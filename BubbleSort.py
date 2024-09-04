def bubble_sort(arr):
    n = len(arr)
    # Percorre todos os elementos da lista
    for i in range(n):
        # A cada iteração, os maiores elementos vão "subindo" até o final da lista
        for j in range(0, n-i-1):
            # Troca se o elemento atual for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Array ordenado:", arr)
