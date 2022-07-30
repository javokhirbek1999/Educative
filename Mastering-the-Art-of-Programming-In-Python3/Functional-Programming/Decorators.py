import functools

def toggle(function):
    @functools.wraps(function) # Copies the meta data of the original function to the wrapper function
    def wrapper(name: str):
        result = function(name)
        result = result.swapcase()
        return result
    
    return wrapper

def decorator(function):
    @functools.wraps(function) # Copies the meta data of the original function to the wrapper function
    def wrapper(name: str):
        "It is decorating welcome message"
        result = function(name)
        result = result.upper()
        return result
    
    return wrapper

@toggle
@decorator
def welcome(name: str):
    "This is a welcome message"
    return f'Welcome to Educative, {name} !'

print(welcome("Javokhirbek"))
print(welcome.__name__) # Prints the function name
print(welcome.__doc__)  # Prints the docstring of the function
