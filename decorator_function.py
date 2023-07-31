def upper_case(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@upper_case
def say_hi():
    return "hello there"

print(say_hi())
