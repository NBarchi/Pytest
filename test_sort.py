import pytest
from sort import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

# Datos 
test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = sorted(test_array)  # [11, 12, 22, 25, 34, 64, 90]

@pytest.mark.parametrize("sort_function", [
    bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
])
def test_sorting_algorithms(sort_function):
    arr = test_array.copy()  # Copia 
    sorted_arr = sort_function(arr)
    assert sorted_arr == sorted_array
