##
# boolean: True/False
# >, <, >=, <=, ==, != => True/False

"""
if
elif - else if
else
"""
age = int(input("age: "))

if not 0:
    print("beer")
print("chivas")
# if age > 10:
#     print("coca")
# else:
#     print("water")

##
name = input("Please enter your name: ")

if name:  # Checks the truth value of name by calling bool
    print(f"You entered {name}")
else:
    print("You didn't type anything")

##
a = [1, 2, 3]
b = [1, 2, 3]
a = b
print(a == b)
print(a is b)

##
numbers = [1, 2, 3, 4]
print(id(numbers))
numbers = numbers + [5]
print(id(numbers))

##
numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))

##
number = float(input())
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

##
work_hours = float(input("ur work hours: "))
hourly_wage = float(input("ur hourly wage: "))

total_amount = hourly_wage * work_hours

if work_hours > 40:
    total_amount = hourly_wage * (work_hours - 40) * 1.1 + hourly_wage * 40

print(f"You have earned ${total_amount:.2f}")

##
n = int(input())
if n >= 100:
    total =

if n <= 500:
    total = n * 50
elif n <= 1000:
    total = 500 * 50 + (n - 500) * 40
elif n <= 1500:
    total = 500 * 50 + 500 * 40 + (n - 1000) * 30
else:
    total = 500 * 50 + 500 * 40 + 500 * 30 + (n - 1500) * 20
# if total > 299000:
#     total = 299000
total = min(total, 299000)
print(total)

##
n = int(input())
if n <= 100:
    total = n * 550
elif n <= 150:
    total = 100 * 550 + (n - 100) * 900
elif n <= 200:
    total = 100 * 550 + 50 * 900 + (n - 150) * 1250
elif n <= 300:
    total = 100 * 550 + 50 * 900 + 50 * 1250 + (n - 200) * 1450
else:
    total = 100 * 550 + 50 * 900 + 50 * 1250 + 100 * 1450 + (n - 300) * 1700
total *= 1.1
print(int(total))
