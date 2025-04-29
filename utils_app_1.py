from functools import reduce
import operator

def sum_all(array_numbers: list) -> int:
    return reduce(operator.add, array_numbers)

def multiply_all(array_numbers: list) -> int:
    return reduce(operator.mul, array_numbers)

def duplicated_numbers(array_numbers: list) -> list:
    return [number for number in array_numbers if array_numbers.count(number) > 1]

def get_odd_numbers(array_numbers: list) -> list:
    return [number for number in array_numbers if number % 2 != 0]

def get_even_numbers(array_numbers: list) -> list:
    return [number for number in array_numbers if number % 2 == 0]

def get_counsil_numbers(array_numbers: list) -> list:
    return [number for number in array_numbers if number % 3 == 0]
