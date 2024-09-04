def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializa o gap (dividindo o array ao meio)
    
    # Gap começa em n//2 e vai sendo reduzido até 1
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            
            # Faz a inserção de arr[i] nos elementos separados pelo gap
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            arr[j] = temp
        
        gap //= 2  # Reduz o gap

# Exemplo de uso
arr = [12, 34, 54, 2, 3]
shell_sort(arr)
print("Array ordenado:", arr)
