print("Exponent Calculator")
print("This calculator can:")
def exponentcalculator():
    print("1.Find the exponent's value")
    print("2.Find the square root or cube root of a number")
    while True:
        try:
            operation = (input("Enter the function number as mentioned above for the operation:"))
            operation = int(operation)
            break
        except ValueError:
            print("Error 3 - You have entered a unrecognizable value. Please enter only a function number.")
    while operation >= 3:
        while True:
            try:
                print("Error 3 - You have entered a unrecognizable value. Please enter only a function number.")
                operation = (input("Enter the operation number as mentioned above for the operation:"))
                operation = int(operation)
                break
            except ValueError:
                print("Error 3 - You have entered a unrecognizable value. Please enter only a function number.")
    if operation == 1:
        while True:
            try:
                base = (input("Enter the base:"))
                base = float(base)
                break
            except ValueError:
                print("Error 2b - You have entered a unrecognizable value. Please enter only an float value.")
        while True:
            try:
                power = (input("Enter the power:"))
                power = float(power)
                break
            except ValueError:
                print("Error 2b - You have entered a unrecognizable value. Please enter only an float value.")
        exponentvalue = base ** power
        exponent = round(exponentvalue,3)
        print("The value of the exponent, rounded to three decimal places, is", exponent)
    if operation == 2:
        while True:
            try:
                roottype = (str(input("Press 's' for square root and 'c' for cube root:")))
                import math
                if roottype in ("s","S"):
                    while True:
                        try:
                            square = (input("Enter the square:"))
                            square = float(square)
                            break
                        except ValueError:
                            print("Error 2b - You have entered a unrecognizable value. Please enter only an float value.")
                    squarerootvalue = math.sqrt(square)
                    squareroot = round(squarerootvalue, 3)
                    print("The square root of the number, rounded to three decimal places, is", squareroot)
                    break
                elif roottype in ("c","C"):
                    while True:
                        try:
                            cube = (input("Enter the cube:"))
                            cube = float(cube)
                            break
                        except ValueError:
                            print("Error 2b - You have entered a unrecognizable value. Please enter only an float value.")
                    cuberootvalue = cube ** (1 / 3)
                    cuberoot = round(cuberootvalue, 3)
                    print("The cube root of the number, rounded to three decimal places, is", cuberoot)
                    break
                else:
                    print("Error 5 - Invalid input. Please enter only 'c' or 's'.")
            except Exception:
                print("Error 1 - Unknown exception. A problem has occurred.")
exponentcalculator()
while True:
    try:
        rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        while rerun in ("yes","Yes"):
            exponentcalculator()
            rerun = (str(input("Do you want to rerun this calculator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using this calculator.")
            break
        else:
            print("Error 9a - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error 1 - Unknown exception. A problem has occurred.")