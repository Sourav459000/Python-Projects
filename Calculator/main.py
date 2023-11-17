from replit import clear
from logo import a

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    print(a)
    num1 = float(input("What's the first number?:"))

    for sym in operations:
        print(sym)
    should_continue = True
    while should_continue:
        operations_sym = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?:"))
        calculation_function = operations[operations_sym]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operations_sym} {num2} = {answer}")
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator()

calculator()
