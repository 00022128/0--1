#. Syntax & Structure
# Python code is designed to be easy to read. Unlike some other languages,Python uses indentation (whitespace) to define code blocks, like loops and functions.
# Example:
if 5 > 2:
    print("Five is greater than two!")

#2. Variables & Data Types
# You can store data in variables without explicitly defining their type. Python automatically handles it.
x = 5        # Integer
y = 3.14     # Float
name = "Alice"  # String
is_active = True  # Boolean

#3. Data Structures
# Python has built-in data structures like lists, dictionaries, tuples, and sets.
# List: An ordered, changeable collection of items
fruits = ["apple", "banana", "cherry"]
# Tuple: An ordered, unchangeable collection.
point = (4, 5)
# Dictionary: A collection of key-value pairs.
person = {"name": "John", "age": 30}
# Set: An unordered collection of unique items.
unique_numbers = {1, 2, 3}

# 4. Control Flow
# Python has standard control flow statements like loops and conditionals.
# If statement:
a = int(input(""))
if a > 10:
    print("a is greater than 10")
elif a == 10:
    print("a is 10")
else:
    print("a is less than 10")
# For loop:
for fruit in fruits:
    print(fruit)
# While loop:
count = 0
while count < 5:
    print(count)
    count += 1
# 5. Functions
# Functions allow you to encapsulate code that can be reused.
def greet(name):
    print(f"Hello, {name}!")

# 6. Libraries & Modules
# Python has a rich standard library and a wide range of third-party packages. You can import libraries to use additional functionality.
# Example:

import math

print(math.sqrt(16))  # Outputs: 4.0

# 8. Error Handling
# You can use try-except blocks to handle errors and exceptions.

try:
    b = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")

# 9. Object-Oriented Programming
# Python supports OOP with classes and objects.

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

dog1 = Dog("Buddy", 3)
dog1.bark()  # Outputs: Buddy says woof!

# 10. File Handling
# Python allows you to work with files easily.

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

