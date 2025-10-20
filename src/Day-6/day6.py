# Functions group reusable code.
# This function defines a test step.
def setup_environment():
    print("INFO: Setting up test environment...")
    print("INFO: Browser opened.")
    print("INFO: Navigated to test URL.")

def run_login_test():
    print("TEST: Running login test...")
    print("TEST: Entered username.")
    print("TEST: Clicked login.")
    print("RESULT: Login successful.")

def tear_down():
    print("INFO: Tearing down environment...")
    print("INFO: Browser closed.")

setup_environment()
run_login_test()
tear_down()