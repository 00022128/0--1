import math
from sympy import symbols, Eq, solve

def add():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f'{a}+{b} = {a+b}')
    except ValueError:
        print("Invalid input. Please enter numbers")

def subtract():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f'{a}-{b} = {a-b}')
    except ValueError:
        print("Invalid input. Please enter numbers")

def multiply():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print(f'{a}*{b} = {a*b}')
    except ValueError:
        print("Invalid input. Please enter numbers")

def divide():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Value cannot be divided by zero")
        else:
            print(f'{a}:{b} = {a/b}')
    except ValueError:
        print("Invalid input. Please enter numbers")

def sqrt():
    try:
        number = float(input("Enter a number: "))
        if number < 0:
            print("Error! Cannot compute the square root of a negative number.")
        else:
            sqrt_result = math.sqrt(number)
            print(f'//{number} = {sqrt_result}')

    except ValueError:
        print("Invalid input. Please enter numbers")

def power():
    try:
        number = float(input("Enter a number: "))
        power_level = int(input(""))
        print(f'{number}**{power_level} = {number ** power_level}')
    except ValueError:
        print("Invalid input. Please enter numbers")

def simple_equation():
    try:
        equation = input("Enter equation: ")

        # Define 'x' as a symbol for algebraic solving
        x = symbols("x")

        # Parse the equation and solve for x
        lhs, rhs = equation.split("=")
        eq = Eq(eval(lhs), eval(rhs))

        # Solve the equation symbolically
        solution = solve(eq, x)
        print(f'x = {solution[0]}')

    except Exception as e:
        print(f'Error solving equation: {e}')





def menu():
    print("Welcome to Greatest Calculator !")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Sqrt")
    print("6. Power")
    print("7. Simple Equation")
    print("8. Exit")
    while True:
        input_choice = input("Enter your choice: ")

        if input_choice == "1":
            add()
        elif input_choice == "2":
            subtract()
        elif input_choice == "3":
            multiply()
        elif input_choice == "4":
            divide()
        elif input_choice == "5":
            sqrt()
        elif input_choice == "6":
            power()
        elif input_choice == "7":
            simple_equation()
        elif input_choice == "8":
            print("Thank you for using Greatest Calculator!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
menu()






