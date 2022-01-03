import math


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiply(a, b):
    return a * b


def sqrt(a):
    result = math.sqrt(a)
    return result


def exp(a):
    return a ** 2


def sin(x):
    result = math.sin(x)
    return result


def cos(x):
    result = math.cos(x)
    return result


def tan(x):
    result = math.tan(x)
    return result


print("""
choose a number for the following operations
1 - Addition(x,y)
2 - Subtraction(x,y)
3 - Multiplication(x,y)
4 - Divide(x,y)
5 - Square(x)
6 - Square root(x)
7 - sin(x)
8 - cos(x)
9 - tan(x)
""")
# op = Operation
op = int(input('What Operation do you want to perform '))

while op < 10:
    if op == 1:
        print("Enter the Parameters")
        x1 = int(input("Enter x "))
        y1 = int(input("Enter y "))
        res1 = add(x1, y1)
        print("Addition: ", res1)
    elif op == 2:
        print("Enter the Parameters")
        x2 = int(input("Enter x "))
        y2 = int(input("Enter y "))
        res2 = subtract(x2, y2)
        print("Addition: ", res2)
    elif op == 3:
        print("Enter the Parameters")
        x3 = int(input("Enter x "))
        y3 = int(input("Enter y "))
        res3 = multiply(x3, y3)
        print("Addition: ", res3)
    elif op == 4:
        print("Enter the Parameters")
        x4 = int(input("Enter x "))
        y4 = int(input("Enter y "))
        res4 = divide(x4, y4)
        print("Addition: ", res4)
    elif op == 5:
        print("Enter the Parameters")
        x5 = int(input("Enter x "))
        res5 = sqrt(x5)
        print("Square: ", res5)
    elif op == 6:
        print("Enter the Parameters")
        x6 = int(input("Enter x "))
        res6 = exp(x6)
        print("Square Root: ", res6)
    elif op == 7:
        print("Enter the Parameters")
        x7 = int(input("Enter x "))
        res7 = sin(x7)
        print("Sine: ", res7)
    elif op == 8:
        print("Enter the Parameters")
        x8 = int(input("Enter x "))
        res8 = cos(x8)
        print("Cosine: ", res8)
    elif op == 9:
        print("Enter the Parameters")
        x9 = int(input("Enter x "))
        res9 = tan(x9)
        print("Tan: ", res9)
    else:
        print('Choose another Operation')

    new = int(input('Do you want to continue - (1 - Yes) or (0 - No): '))
    if new == 1:
        op = int(input("Enter Operation: "))
    elif new == 0:
        print("Thanks for using the Scientific Calculator")
        break
