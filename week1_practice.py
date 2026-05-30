numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n * n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]

print("Squares:", squares)
print("Even numbers:", evens)

def divide(a, b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

divide(10, 2)
divide(5, 0)