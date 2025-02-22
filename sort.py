def bubble_sort(arr):
    arr = arr[:]  # Copia
    n = len(arr)
    print("Array before sorting:", arr)
    for i in range(n):
        print("Pass", i + 1)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)
    return arr

def selection_sort(arr):
    arr = arr[:]  # Copia
    n = len(arr)
    print("Array before sorting:", arr)
    for i in range(n):
        min_index = i
        print("Pass", i + 1)
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr

def insertion_sort(arr):
    arr = arr[:]  # Copia 
    n = len(arr)
    print("Array before sorting:", arr)
    for i in range(1, n):
        print("Pass", i)
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        print("Left:", left)
        print("Right:", right)

        left_sorted = merge_sort(left)
        right_sorted = merge_sort(right)

        i = j = k = 0
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] < right_sorted[j]:
                arr[k] = left_sorted[i]
                i += 1
            else:
                arr[k] = right_sorted[j]
                j += 1
            k += 1

        while i < len(left_sorted):
            arr[k] = left_sorted[i]
            i += 1
            k += 1

        while j < len(right_sorted):
            arr[k] = right_sorted[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print("Pivot:", pivot, "Left:", left, "Middle:", middle, "Right:", right)
    
    return quick_sort(left) + middle + quick_sort(right)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Prueba de los algoritmos
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print("Bubble sort:", bubble_sort(test_array))
    print("\nSelection sort:", selection_sort(test_array))
    print("\nInsertion sort:", insertion_sort(test_array))
    print("\nMerge sort:", merge_sort(test_array))
    print("\nQuick sort:", quick_sort(test_array))
    
    search_array = [10, 20, 30, 40, 50]
    print("\nLinear search (looking for 30):", linear_search(search_array, 30))
    print("Binary search iterative (looking for 30):", binary_search_iterative(search_array, 30))
    print("Binary search recursive (looking for 30):", binary_search_recursive(search_array, 30))
