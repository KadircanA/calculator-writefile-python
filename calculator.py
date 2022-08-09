import time

def question ():
    pass

def question ():

    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    lang=int(input("What kind of math operation would you like to do? (please enter a number): "))

    match lang:
        case 1:
            print("You can become a web developer.")

        case 2:
            print("You can become a Data Scientist")

        case 3:
            print("You can become a backend developer")
    
        case 4:
            print("You can become a Blockchain developer")

        case _:
            print("*-"*13)
            print("You entered a wrong number")
            print("*-"*13)
            question()
if __name__ == '__main__':
    
    question()

    pass