print("Today is very hot")
print("Let's rest")

temperature = 30
if temperature >25:
    print("It's a hot day!")
elif temperature >=10:
    print("It's a cool day!")
else:
    print("It's a cold day!")
print("Done")  
 
# Print numbers 0 to 4
for i in range(5):
    print(i)
    
import sys
sys.stdout.reconfigure(encoding='utf-8')  # Force UTF-8 encoding

countdown = 5

while countdown > 0:
    print("Counting down:", countdown)
    countdown -= 1

print("Blast off! 🚀")  # The rocket emoji should now work


fruits = ["apple", "banana", "cherry"]

# Accessing elements
print(fruits[0])  # Outputs: apple

# Modifying an element
fruits[1] = "orange"
print(fruits)  # Outputs: ['apple', 'orange', 'cherry']

# Adding an element
fruits.append("grape")
print(fruits)  # Outputs: ['apple', 'orange', 'cherry', 'grape']
 
 
# Defining a function
def greet(name):
    print("Hello, " + name + "! 👋")

# Calling the function
greet("Alice")  # Outputs: Hello, Alice! 👋
greet("Bob")    # Outputs: Hello, Bob! 👋


def add_numbers(x, y):
    return x + y

result = add_numbers(10, 5)
print(result)  # Outputs: 15

import random

# Generate a random number between 1 and 6 (like rolling a die)
dice_roll = random.randint(1, 6)
print("You rolled a", dice_roll)