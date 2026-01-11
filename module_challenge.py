import random2
from module_callenge_code import module_opreations
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
operation = input("Enter operation (+, -, *, /, sqrt, pow, exp, random2): ")
if operation == '+':
    result = module_opreations.addition(a, b)
elif operation == '-':
    result = module_opreations.subtraction(a, b)
elif operation == '*':
    result = module_opreations.multiplication(a, b)
elif operation == '/':
        result = module_opreations.division(a, b)
elif operation == 'sqrt':
        result = module_opreations.square_root(a)
elif operation == 'pow':
        result = module_opreations.power(a, b)
elif operation == 'exp':
        result = module_opreations.exponents(a, b)
elif operation == 'random2':
        result = module_opreations.random2(a, b)
else:
    result = "Invalid operation."
print("The result is:", result)
