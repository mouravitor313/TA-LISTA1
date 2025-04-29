import pytest
import utils_app_1 as utils

def test_sum_all():
    test_numbers = [1, 2, 3, 4, 5]
    assert utils.sum_all(test_numbers) == 15

def test_multiply_all():
    test_numbers = [1, 2, 3, 4, 5]
    assert utils.multiply_all(test_numbers) == 120

def test_duplicated_numbers():
    test_numbers = [1, 2, 2, 3, 4, 4, 5]
    assert utils.duplicated_numbers(test_numbers) == [2, 2, 4, 4]

def test_get_odd_numbers():
    test_numbers = [1, 2, 3, 4, 5, 6, 7]
    assert utils.get_odd_numbers(test_numbers) == [1, 3, 5, 7]

def test_get_even_numbers():
    test_numbers = [1, 2, 3, 4, 5, 6, 7]
    assert utils.get_even_numbers(test_numbers) == [2, 4, 6]

def test_get_multiples_of_3():
    test_numbers = [1, 2, 3, 6, 9, 12, 15]
    assert utils.get_counsil_numbers(test_numbers) == [3, 6, 9, 12, 15]
