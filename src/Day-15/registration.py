def validate_registration(username, password, email):
    """
    Validates user registration data.
    Returns a list of error messages.
    If the list is empty, validation passed.
    """
    errors = []
    if len(username) < 5:
        errors.append("Username must be at least 5 characters.")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters.")
    if "@" not in email or "." not in email:
        errors.append("Invalid email format.")
    
    return errors