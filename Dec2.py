# ARGS - Used to take and work on multiple values without changing the wrapper class again and again
# KWARGS - Used to work on keys-args functions such as dictionaries

def decorator_function(original_function):

    def wrapper_function(*args, **kwargs):

        print("Before")

        original_function(*args, **kwargs)

        print("After")

    return wrapper_function
