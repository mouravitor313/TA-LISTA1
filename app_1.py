import typing
import utils_app_1 as utils

stop: int = 0
numbers: typing.List[int] = []

while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if stop != number:
        numbers.append(number)
    else:
        print(f"\n\nSum of numbers: {utils.sum_all(numbers)}")
        print(f"Product of numbers: {utils.multiply_all(numbers)}")
        print(f"Duplicated numbers: {utils.duplicated_numbers(numbers)}")
        print(f"Odd numbers: {utils.get_odd_numbers(numbers)}")
        print(f"Even numbers: {utils.get_even_numbers(numbers)}")
        print(f"Numbers divisible by 3: {utils.get_counsil_numbers(numbers)}")
        break
