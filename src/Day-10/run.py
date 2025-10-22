from test_suite import smoke_test_suite

results = {"Pass": 0, "Fail": 0}

print("--- Running Smoke Suite ---")

for test_function in smoke_test_suite:
    result = test_function()
    print(f"Result: {result}\n")
    results[result] += 1

print("--- Test Run Summary ---")
print(f"Total Passed: {results['Pass']}")
print(f"Total Failed: {results['Fail']}")