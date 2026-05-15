def decorator_function(original_function):

    def wrapper_function():
        print("Before")

        original_function()

        print("After")

    return wrapper_function


@decorator_function
def greet():
    print("Hello")

greet()
