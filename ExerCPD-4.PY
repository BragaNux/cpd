def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Mesclar
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Comparar
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Adicionar
        sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

# Exemplo de uso:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Array ordenado:", sorted_arr)
