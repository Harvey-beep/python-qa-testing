# This code will CRASH
# age = int("ten") # This raises a ValueError

# This code will NOT crash
try:
    age_input = input("Enter your age: ") # Try typing "ten"
    age = int(age_input)
    print(f"Next year you will be {age + 1}.")
except ValueError:
    print("Error: That was not a valid number!")

# Simulating a bug
test_data = {
    "id": "TC-003",
    "title": "Check profile"
    # "user" key is missing! This is a bug in the test data.
}

try:
    print(f"Running test for user: {test_data["user"]}")
except KeyError:
    print("BUG FOUND: 'user' key is missing from test data.")
    print(f"Test data was: {test_data}")

print("Script continues...")

# Day 8 Mini Project
def divide(a, b):
    return a / b

print(f"The result is {divide(10, 2)}.")

try:
    print(f"The result is {divide(10, 0)}.")
except ZeroDivisionError:
    print("Error: Cannot be divided by zero.")
