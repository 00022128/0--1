# Task 1: Basic Operations and Data Types
def task1(num1, num2):
    operations = {"Sum":(num1 + num2),
                  "Difference":(num1 - num2),
                  "Product":(num1 * num2),
                  "Quotient":(num1 / num2),
                  }
    try:
        return operations
    except ZeroDivisionError:
        print("Can not be devided by zero")

input1 = int(input("Enter a number: "))
input2 = int(input("Enter another number:"))
print(task1(input1, input2))

# Task 2: List and Dictionary Manipulation (Fail)

# Task 3: Control Flow and Error Handling
nums = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9
}
from_10_19 = {
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19
}
from_20_1000000000 = {
    "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
    "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100,
    "thousand": 1000, "million": 1000000
}

def converter():
    try:
        user_input = input("Enter a number: ").lower().split()
        result = 0
        temp_sum = 0

        for word in user_input:
            if word in nums:
                temp_sum += nums[word]
            elif word in from_10_19:
                temp_sum += from_10_19[word]
            elif word in from_20_1000000000:
                multiplier = from_20_1000000000[word]
                if multiplier >= 100:
                    temp_sum *= multiplier
                else:
                    temp_sum += multiplier
            else:
                print("Invalid input")
                return None

        result += temp_sum
        print("Converted Number:", result)
    except ValueError:
        print("Invalid input")

converter()




