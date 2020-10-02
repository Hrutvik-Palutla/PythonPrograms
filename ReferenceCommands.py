# Rerun Command
# This is a reference command for rerunning a specific function
while True:
    try:
        rerun = (str(input("Do you want to rerun the /program name here/ ?(yes/no):")))
        while rerun in ("yes","Yes"):
            # function name()
            rerun = (str(input("Do you want to rerun the /program name here/ ?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the /program name here/ .")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")

# Change as required:
# This is a reference command for getting two numbers without any ValueErrors
def numbers():
    while True:
        try:
            num1 = (input("Enter first #required input:"))
            num1 = int(num1)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only #required input.")
    while True:
        try:
            num2 = (input("Enter second #required input:"))
            num2 = int(num2)
            break
        except ValueError:
            print("Error 19c - You have entered a unrecognizable value. Please enter only #required input.")
numbers()
