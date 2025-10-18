# Looping through a list
test_list = ["Login", "Logout", "AddToCart"]
print("--- Test Cases ---")
for test in test_list:
    print(f"Running test: {test}") # f-string is a nice way to format

# Reading from a file
print("\n--- Usernames from file ---")
try:
    with open("test_data.txt", "r") as file:
        for line in file:
            # .strip() removes whitespaces/newlines
            print(f"Checking user: {line.strip()}")
except FileNotFoundError:
    print("Error: test_data.txt was not found!")
