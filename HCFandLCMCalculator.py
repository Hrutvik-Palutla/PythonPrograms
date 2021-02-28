print("HCF and LCM Calculator")
print("This calculator calculates the HCF and LCM of any two numbers you enter.")
print("Note: Enter only positive integers (natural numbers; not including zero) for this calculator to work.")
number1 = 0
number2 = 0
hcf = 0
def lcm_hcf_calculator():
    while True: #For first number
        try:
            global number1
            number1 = input("Enter the first number:")
            number1 = int(number1)
            while number1 <= 0:
                print("Error - Please enter only a natural number, and not a float value, zero or negative integer.")
                number1 = input("Enter the first number:")
                number1 = int(number1)
            break
        except ValueError:
            print("Error - You have entered an unrecognizable value. Please enter only a natural number.")
    while True: #For second number
        try:
            global number2
            number2 = input("Enter the second number:")
            number2 = int(number2)
            while number2 <= 0:
                print("Error - Please enter only a natural number, and not a float value, zero or negative integer.")
                number2 = input("Enter the second number:")
                number2 = int(number2)
            break
        except ValueError:
            print("Error - You have entered an unrecognizable value. Please enter only a natural number.")
    print("Processing...")
    from time import sleep
    sleep(0.5)
    def hcf_processor(): #For processing HCF
        global hcf
        if number1 == number2: #If the two numbers are equal to each other
            print("The HCF of the two numbers", number1, "and", number2, "is", str(number1) + ".")
            hcf = number1
        elif number1 > number2: #If number1 is greater than number2
            for try_number in range(number2 , 0, -1):
                if number1 % try_number == 0 and number2 % try_number == 0:
                    print("The HCF of the two numbers", number1, "and", number2, "is", str(try_number) + ".")
                    hcf = try_number
                    break
        elif number1 < number2: #If number2 is greater than number1
            for try_number in range(number1 , 0, -1):
                if number1 % try_number == 0 and number2 % try_number == 0:
                    print("The HCF of the two numbers", number1, "and", number2, "is", str(try_number) + ".")
                    hcf = try_number
                    break
        else: #If the computer has lost its mind
            print("Error - Unknown exception. A problem has occurred.")
    hcf_processor()
    def lcm_processor(): #For processing LCM
        lcm = (number1 * number2)/hcf
        print("The LCM of the two numbers", number1, "and", number2, "is", str(lcm) + ".")
    lcm_processor()
lcm_hcf_calculator()
while True: #Rerun command
    try:
        rerun = (str(input("Do you want to rerun the calculator?(yes/no):")))
        while rerun in ("yes","Yes"):
            lcm_hcf_calculator()
            rerun = (str(input("Do you want to rerun the calculator?(yes/no):")))
        if rerun in ("no","No"):
            print("Thank you for using the calculator.")
            break
        else:
            print("Error - Invalid input. Please enter only yes or no.")
    except Exception:
        print("Error - Unknown exception. A problem has occurred.")

