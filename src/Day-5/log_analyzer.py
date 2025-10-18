# Day 5 Hands-On Project

error_count = 0

print("--- Reading app.log ---")
try:
    with open("app.log", "r") as file:
        for line in file:
            if "ERROR" in line:
                print(f"Checking for errors: {line.strip()}")
                error_count = error_count + 1
except FileNotFoundError:
    print("Error: app.log was not found!")

print("Total errors found:", error_count)

