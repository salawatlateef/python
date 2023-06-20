"""print("Welcome to the PyPassword Generator")
alphabets = ["a", "b", "c"]
letter = input("How many letters would you like in your password?")
symbols = ["!", "@", "#"]
sym = input("How many symbols would you like?")
numbers = ["1", "2", "3"]
num= input("How many numbers would you like?")
password = []
"""

"""student_heights = input("A list of student height.").split()
number_of_students = len("student_heights")
total = sum(f"student_heights")

average = total / number_of_students
print(average)"""

"""student_heights = input("Input a list of student heights").split()
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)"""

"""fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)"""

"""student_scores = input("Input a list of students scores").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print("The minimum score in th class is " + f"{min(student_scores)}")
"""

"""student_scores = [12, 23, 34]
highest_score = 0
for score in student_scores:
  if score > highest_score:
      highest_score = score
print(f"The highest score is {highest_score}")"""

# For loop with Range
"""total = 0
for number in range(1, 11):
    total += number
print(total)"""

# Sum of even numbers between 1 and 100
"""total = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Another method
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
     total2 += number
print(total2)
"""
for number in range(1, 20):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '&', '*', '+', '-', '~']

print("Welcome to PasswordPy Generator!")
password = ""
nr_letters = int(input("How many letters do you want in your password?\n"))
nr_numbers = int(input("How many numbers do you want in your password?\n"))
nr_symbols = int(input("How many symbols do you want in your password?\n"))
import random

for n in range(0, nr_letters + 1):
    password += random.choice(alphabet)
for n in range(0, nr_numbers + 1):
    password += random.choice(numbers)
for n in range(0, nr_symbols + 1):
    password += random.choice(symbols)
print(password)
