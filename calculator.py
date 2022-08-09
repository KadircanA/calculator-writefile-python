import time
from unittest import result

def question ():
    pass

def question ():

    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    process=int(input("What kind of math operation would you like to do? (please enter a number): "))

    match process:
        case 1:
            Addition()
        case 2:
            pid=2
        case 3:
            pid=3
        case 4:
            pid=4
        case _:
            print("*-"*13)
            print("You entered a wrong number")
            print("*-"*13)
            question()
def Addition():
    x=float(input("plese enter first number:"))
    y=float(input("plese enter second number:"))
    result =(x+y)
    print(result)
def Subtraction():
    x=float(input("plese enter first number:"))
    y=float(input("plese enter second number:"))
    result =(x-y)
    print(result)
def Multiplication():
    x=float(input("plese enter first number:"))
    y=float(input("plese enter second number:"))
    result =(x/y)
    print(result)
def Subtraction():
    x=float(input("plese enter first number:"))
    y=float(input("plese enter second number:"))
    result =(x-y)
    print(result)


if __name__ == '__main__':
    
    question()

    pass