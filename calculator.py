from datetime import datetime

def question ():

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    process=int(input("What kind of math operation would you like to do? (please enter a number): "))

    match process:
        case 1:
            Addition()

        case 2:
            Subtraction()

        case 3:
            Multiplication()

        case 4:
            divide()

        case _:
            print("*-"*13)
            print("You entered a wrong number")
            print("*-"*13)
            question()

def subquestion():
    answer = input("New prosses? (yes or no)")
    if any(answer.lower() == f for f in ["yes", 'y', '1', 'ye']):
        question()   
    elif any(answer.lower() == f for f in ['no', 'n', '0']):
        print("BB")
        

def Addition():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    id="addition"
    result =(x+y)
    print(f"result:{result}")
    Record(id,result)
def Subtraction():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    id="subtraction"
    result =(x-y)
    print(f"result:{result}")
    Record(id,result)
def Multiplication():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    id="multiplication"
    result =(x*y)
    print(f"result:{result}")
    Record(id,result)
def divide():
    x=float(input("Please enter first number:"))
    y=float(input("Please enter second number:"))
    id="divide"
    result =(x/y)
    print(f"result:{result}")
    Record(id,result)

def Record(pid,r):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(f"{dt_string}--> Result of {pid} prosses is {r}  ")
    subquestion()
    ths = open("Record_file.txt", "a")
    ths.write(f"\n{dt_string}--> Result of {pid} prosses is {r}  ")
    ths.close()

if __name__ == '__main__':
    
    question()