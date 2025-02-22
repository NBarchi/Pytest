import pytest
from sort import linear_search, binary_search_iterative, binary_search_recursive

# Datos 
test_array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = sorted(test_array)  # [11, 12, 22, 25, 34, 64, 90]

@pytest.mark.parametrize("arr, target, expected", [
    (test_array, 22, test_array.index(22)),  
    (test_array, 90, test_array.index(90)),  
    (test_array, 100, -1),  
])
def test_linear_search(arr, target, expected):
    assert linear_search(arr, target) == expected


@pytest.mark.parametrize("arr, target, expected", [
    (sorted_array, 22, sorted_array.index(22)),  
    (sorted_array, 90, sorted_array.index(90)),  
    (sorted_array, 100, -1),  
])
def test_binary_search_iterative(arr, target, expected):
    assert binary_search_iterative(arr, target) == expected


@pytest.mark.parametrize("arr, target, expected", [
    (sorted_array, 22, sorted_array.index(22)),  
    (sorted_array, 90, sorted_array.index(90)),  
    (sorted_array, 100, -1),  
])
def test_binary_search_recursive(arr, target, expected):
    assert binary_search_recursive(arr, target, 0, len(arr) - 1) == expected
