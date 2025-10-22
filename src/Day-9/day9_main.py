# Import the function from our other file
from utils import validate_email

email1 = "test@example.com"
email2 = "bad-email"

print(f"Checking {email1}: {validate_email(email1)}")
print(f"Checking {email2}: {validate_email(email2)}")