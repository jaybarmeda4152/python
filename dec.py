# def upper(text):
#     return text.upper()
 
# def lower(text):
#     return text.lower()
 
# def greet(func):
#     # storing the function in a variable
#     greeting = func("""Hi, I am created by a function passed as an argument.""")
#     print (greeting)
 
# greet(upper)
# greet(lower)

def create_adder(x):
    print(x)
    def adder(y):
        print(y)
        return x+y
 
    return adder
 
add_15 = create_adder(15)
 
print(add_15(10))