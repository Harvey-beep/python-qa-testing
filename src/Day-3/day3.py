# Lists are ordered, accessed by index (starts at 0)
browsers_to_test = ["chrome", "firefox", "safari"]
print("First browser:", browsers_to_test[0])

browsers_to_test.append("edge") # Add an item
print("All browsers:", browsers_to_test)

# Dictionaries store key-value pairs
test_environment = {
    "url": "https://myapp.com",
    "username": "qa_user",
    "api_version": 2.1
}

print("Testing URL:", test_environment["url"])

# Add a new key-value pair
test_environment["browser"] = "chrome"
print("Full config:", test_environment)