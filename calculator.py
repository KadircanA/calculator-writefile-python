import time

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
            pid=1
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
    
    pass
if __name__ == '__main__':
    
    question()

    pass