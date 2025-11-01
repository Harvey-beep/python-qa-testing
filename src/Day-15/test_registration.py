import pytest
from registration import validate_registration

def test_valid_registration():
    # A valid registration should return an empty list.
    errors = validate_registration("valid_user", "ValidPass123", "test@example.com")
    assert len(errors) == 0

def test_invalid_username_too_short():
    errors = validate_registration("user", "ValidPass123", "test@example.com")
    # We expect ONE error
    assert len(errors) == 1
    # We check if the specific error message is in the list.
    assert "Username must be at least 5 characters." in errors

@pytest.mark.smoke
def test_invalid_password_too_short():
    errors = validate_registration("valid_user", "valid", "test@example.com")
    assert len(errors) > 0 # A simple check
    assert "Password must be at least 8 characters." in errors

def test_all_fields_invalid():
    errors = validate_registration("user", "valid", "testexample.com")
    assert len(errors) == 3
    assert "Invalid email format." in errors
