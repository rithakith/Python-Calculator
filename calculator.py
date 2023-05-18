history = []  # List to store calculation history

def add(a, b):
    result = a + b
    print(f'{a} + {b} = {result}')
    history.append(f'{a} + {b} = {result}')  # Add the calculation to the history

def sub(a, b):
    result = a - b
    print(f'{a} - {b} = {result}')
    history.append(f'{a} - {b} = {result}')  # Add the calculation to the history

def div(a, b):
    if b == 0:
        print('Float division by zero')
        result = None
    else:
        result = a / b
    print(f'{a} / {b} = {result}')
    history.append(f'{a} / {b} = {result}')  # Add the calculation to the history

def mult(a, b):
    result = a * b
    print(f'{a} * {b} = {result}')
    history.append(f'{a} * {b} = {result}')  # Add the calculation to the history

def pow(a, b):
    a = int(a)
    b = int(b)
    result = a ** b
    print(f'{a} ^ {b} = {result}')
    history.append(f'{a} ^ {b} = {result}')  # Add the calculation to the history

def mod(a, b):
    result = a % b
    print(f'{a} % {b} = {result}')
    history.append(f'{a} % {b} = {result}')  # Add the calculation to the history

selected_op = ['+', '-', '/', '*', '^', '%', '#', '$', '?']

operator = ""
while True:
    print("Select operation.")
    print("1. Add        : +")
    print("2. Subtract   : -")
    print("3. Multiply   : *")
    print("4. Divide     : /")
    print("5. Power      : ^")
    print("6. Remainder  : %")
    print("7. Terminate  : #")
    print("8. Reset      : $")
    print("9. History    : ?")
    
    while True:
        operator = input("Enter choice (+, -, *, /, ^, %, #, $): ")
        if operator in selected_op:
            break

    if operator == '#':
        print('Done. Terminating')
        exit()

    if operator == '$':
        continue

    if operator == '?':
        if not history:
            print('No past events to show')
        for i in history:
            print(f'{i}')
        continue

    first = input("Enter first number: ")
    if '$' in first:
        continue

    second = input("Enter second number: ")
    if '$' in second:
        continue

    first = float(first)
    second = float(second)

    if operator == '+':
        add(first, second)
    elif operator == '-':
        sub(first, second)
    elif operator == '*':
        mult(first, second)
    elif operator == '/':
        div(first, second)
    elif operator == '^':
        pow(first, second)
    elif operator == '%':
        mod(first, second)
