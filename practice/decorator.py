
# decorator example to include three functions that use the same decorator.

def log_function(func):
    def wrapper(*args):
        print(f"Calling {func.__name__} with arguments: {args}")
        result = func(*args)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

# Apply the decorator to multiple functions
@log_function
def add(a, b):
    return a + b

@log_function
def subtract(a, b):
    return a - b

@log_function
def multiply(a, b):
    return a * b

# Call the decorated functions
result_add = add(3, 5)
result_subtract = subtract(10, 4)
result_multiply = multiply(2, 7)
