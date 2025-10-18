expected_result = 100
actual_result = 95

# Comparison
if actual_result == expected_result:
    print("Test PASSED")
elif actual_result > expected_result:
    print("Test FAILED: Result was higher than expected.")
else:
    print("Test FAILED: Result was lower than expected.")

# Logical operator 'and'
username = "admin"
password_length = 10

if username == "admin" and password_length > 8:
    print("Security check passed.")
else:
    print("Security check failed.")