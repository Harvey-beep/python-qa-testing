from test_functions import *

smoke_test_suite = [
    test_login_valid,
    test_login_invalid_password
]

full_regression_suite = [
    test_login_valid,
    test_login_invalid_password,
    test_checkout_as_guest
]