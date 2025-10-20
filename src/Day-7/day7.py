# This function takes two numbers and returns their sum
def add(num1, num2):
    return num1 + num2

# This function simulates a test and returns a status
def check_login(username, password):
    if username == "admin" and password == "secret_sauce":
        return "Pass"
    else:
        return "Fail"
    
sum_result = add(10, 5)
print(f"Sum is: {sum_result}")

test1_status = check_login("admin", "secret_sauce")
print(f"Test 1 (Valid): {test1_status}")

test2_status = check_login("admin", "wrong_pass")
print(f"Test 2 (Invalid): {test2_status}")

# Day 7 Mini Project
def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
print(validate_email("test@example.com"))
print(validate_email("notanemail.com"))