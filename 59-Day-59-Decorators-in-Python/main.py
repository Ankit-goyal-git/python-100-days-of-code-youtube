
# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good Morning")
#     fx(*args, **kwargs)
#     print("Thanks for using this function")
#   return mfx

# @greet
# def hello():
#   print("Hello world")

# @greet
# def add(a, b,c):
#   print(a+b+c)
  
# # greet(hello)()
# hello()
# # greet(add)(1, 2)
# add(1, 2,3)

import logging

def log_function_call(func):
    def decorated(*args):
        logging.info(f"Calling {func.__name__} with args={args}")
        print(f"Calling {func.__name__} with args={args}, ")
        result = func(*args)
        logging.info(f"{func.__name__} returned {result}")
        print(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

print(my_function(2,5))