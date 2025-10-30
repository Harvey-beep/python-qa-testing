def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False
    
print(validate_email("test@example.com"))
print(validate_email("notanemail.com"))

def test_valid_email():
    assert validate_email("test@.com") == True

def test_invalid_email_no_at():
    assert validate_email("test.com") == False

def test_invalid_email_no_dot():
    assert validate_email("test@com") == False



