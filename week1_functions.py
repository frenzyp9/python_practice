def greet(name):
    print("Hello,", name + "! Welcome to Python.")

def add(a, b):
    return a + b

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

greet("Prachi")
print("Sum:", add(10, 20))
print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))