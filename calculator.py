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
            subquestion()
        case 2:
            Subtraction()
            subquestion()
        case 3:
            Multiplication()
            subquestion()
        case 4:
            Subtraction()
            subquestion()
        case _:
            print("*-"*13)
            print("You entered a wrong number")
            print("*-"*13)
            question()

def subquestion():
    answer = input("Question? (yes or no)")
    if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
        question()   
    elif any(answer.lower() == f for f in ['no', 'n', '0']):
        print("BB")
        

def Addition():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    result =(x+y)
    print(result)
def Subtraction():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    result =(x-y)
    print(result)
def Multiplication():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    result =(x/y)
    print(result)
def Subtraction():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    result =(x-y)
    print(result)


if __name__ == '__main__':
    
    question()