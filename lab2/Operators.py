#small calculator with operators
while True:
    x = float(input())
    op = input()
    y = float(input())

    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        if y == 0:
            print("Error")
        else:
            print(x / y)
    else:
        print("Error")