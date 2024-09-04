import time
import random

# Implementação dos algoritmos de ordenação

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Função para medir o tempo de execução de um algoritmo de ordenação
def time_sorting_algorithm(algorithm, arr):
    start_time = time.time()
    algorithm(arr.copy())  # Usamos arr.copy() para não alterar a lista original
    return time.time() - start_time

# Gerar as listas conforme solicitado

def generate_lists(size):
    sorted_list = list(range(size))
    reversed_list = list(range(size, 0, -1))
    repeated_list = [random.choice([1, 2, 3, 4, 5]) for _ in range(size)]
    random_list = [random.randint(1, 10000) for _ in range(size)]
    return sorted_list, reversed_list, repeated_list, random_list

# Testar o tempo de execução dos algoritmos em diferentes tipos de listas

def test_sorting_algorithms(size):
    sorted_list, reversed_list, repeated_list, random_list = generate_lists(size)
    algorithms = [insertion_sort, selection_sort, bubble_sort, merge_sort, quicksort, shell_sort]
    algorithm_names = ["InsertionSort", "SelectionSort", "BubbleSort", "MergeSort", "QuickSort", "ShellSort"]
    
    # Testar em todos os algoritmos para cada tipo de lista
    for algorithm, name in zip(algorithms, algorithm_names):
        print(f"--- {name} ---")
        
        print(f"Lista já ordenada: {time_sorting_algorithm(algorithm, sorted_list):.5f} segundos")
        print(f"Lista ordenada de maneira inversa: {time_sorting_algorithm(algorithm, reversed_list):.5f} segundos")
        print(f"Lista com dados repetidos: {time_sorting_algorithm(algorithm, repeated_list):.5f} segundos")
        print(f"Lista com dados aleatórios: {time_sorting_algorithm(algorithm, random_list):.5f} segundos")
        print()

# Definir o tamanho das listas e rodar o teste
list_size = 1000
test_sorting_algorithms(list_size)
