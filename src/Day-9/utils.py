def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False