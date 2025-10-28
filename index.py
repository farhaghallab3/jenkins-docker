def sum(x,y):
    return x + y
def multiply(x, y):
    return x * y
def subtract(x, y):
    return x - y
def divide(x, y): 
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
print(sum(10, 5))
print(multiply(10, 5))
print(subtract(10, 5))
print(divide(10, 5))
print(divide(10, 0))  # This will raise an exception    