from sort import merge_sort

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def binary_search_recursive(arr, target, low, high):
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == target: return mid
    elif arr[mid] < target: return binary_search_recursive(arr, target, mid + 1, high)
    else: return binary_search_recursive(arr, target, low, mid - 1)

print("Linear search:")
arr= [64, 34, 25, 12, 22, 11, 90]
print(linear_search(arr, 22))

print("\nBinary search:")
arr= [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(binary_search_iterative(arr, 22))

print("\nBinary search:")
arr= [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)
print(binary_search_recursive(arr, 22, 0, len(arr) - 1))