from utils_ex2 import pega_numero

while True:
    message: str = input("Enter a number: ")
    try:
        number: int= pega_numero(message, "Invalid input. Please enter a valid number.")
        print (number)
        break
    except ValueError as e:
        print(e)