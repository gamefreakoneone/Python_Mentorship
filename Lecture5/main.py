def addition(num1, num2):
    num1 += num2
    return num1


def subtraction(num1, num2):
    num1 -= num2
    return num1


def multiplication(num1, num2):
    num1 *= num2
    return num1


def division(num1, num2):
    num1 /= num2
    return num1


def remainder(num1, num2):
    num1 %= num2
    return num1


def default(num1, num2):
    return "We can't do shit!! "


switcher = {
    1: addition, 
    2: subtraction,
    3: multiplication,
    4: division,
    5: remainder
}

def switch(operation, num1, num2):
    return switcher.get(operation, default)(num1, num2)


print("GOOD DAY SIR!! THIS IS CALCULATOR PROGRAM USING SWITCH STATEMENTS!!")
while True:
    print('''Operations
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Remainder 
    6. Exit''')

    choice = int(input("Select from 1,2,3,4,5 or 6 : "))
    if choice == 6:
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(switch(choice, num1, num2))

print("OBAMA MADE MY FROGS GAY! GOOD DAY SIR!")
print("8====D~~")
print("ROCKETSHIP!!!")