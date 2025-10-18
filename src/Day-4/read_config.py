# Day 4 Mini Project

print("--- Reading config ---")
try:
    with open("config.txt", "r") as file:
        for line in file:
            print(f"Checking config: {line.split("=")[1].strip()}")
except FileNotFoundError:
    print("Error: config.txt was not found!")