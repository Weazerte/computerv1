from reduced_form import reduceFunct, printReduced


def test_polynomials():
    # Test degree 0
    print("\nTesting Degree 0 polynomials:")
    test_cases_0 = [
        "5 * X^0 = 3 * X^0",
        "-2 * X^0 = 3 * X^0",
        "4.5 * X^0 = 1.5 * X^0"
    ]
    
    # Test degree 1
    print("\nTesting Degree 1 polynomials:")
    test_cases_1 = [
        "5 * X^0 + 4 * X^1 = 0 * X^0",
        "-2 * X^0 + 4 * X^1 = -5 * X^0",
        "5 * X^1 = 5 * X^0"
    ]
    
    # Test degree 2
    print("\nTesting Degree 2 polynomials:")
    test_cases_2 = [
        "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
        "5 * X^0 + 4 * X^1 = X^2",
        "-2 * X^0 + 4 * X^1 - 2 * X^2 = 0 * X^0",
        "5 * X^2 = 5 * X^0"
    ]

    # Run all tests
    print("\n=== Degree 0 Tests ===")
    for test in test_cases_0:
        print(f"\nInput: {test}")
        reducedf = reduceFunct(test)
        printReduced(reducedf)

    print("\n=== Degree 1 Tests ===")
    for test in test_cases_1:
        print(f"\nInput: {test}")
        reducedf = reduceFunct(test)
        printReduced(reducedf)

    print("\n=== Degree 2 Tests ===")
    for test in test_cases_2:
        print(f"\nInput: {test}")
        reducedf = reduceFunct(test)
        printReduced(reducedf)


if __name__ == "__main__":
    test_polynomials()
