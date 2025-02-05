from test_harness import TestHarness

def add_numbers(a: int, b: int) -> int:
    """Simple function to add two numbers."""
    return a + b

def calculate_grade(mark: int) -> str:
    """Convert a numerical mark to a letter grade."""
    if mark >= 70:
        return 'A'
    elif mark >= 60:
        return 'B'
    elif mark >= 50:
        return 'C'
    else:
        return 'F'

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius temperature to Fahrenheit."""
    return (celsius * 1.8) + 32

def count_vowels(text: str) -> int:
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

if __name__ == "__main__":
    # Create test harness
    harness = TestHarness()
    
    # Test add_numbers function
    print("Testing add_numbers function:")
    test_cases = [
        ([1, 2], 3, "Simple addition"),
        ([0, 0], 0, "Zero addition"),
        ([-1, 1], 0, "Negative number"),
        ([999, 1], 1000, "Large numbers")
    ]
    harness.run_test_suite(add_numbers, test_cases)
    
    # Test calculate_grade function
    print("\nTesting calculate_grade function:")
    test_cases = [
        ([75], 'A', "Testing A grade"),
        ([65], 'B', "Testing B grade"),
        ([55], 'C', "Testing C grade"),
        ([45], 'F', "Testing F grade")
    ]
    harness.run_test_suite(calculate_grade, test_cases)
    
    # Test celsius_to_fahrenheit function
    print("\nTesting celsius_to_fahrenheit function:")
    test_cases = [
        ([0], 32, "Water freezing point"),
        ([100], 212, "Water boiling point"),
        ([20], 68, "Room temperature")
    ]
    harness.run_test_suite(celsius_to_fahrenheit, test_cases)
    
    # Test count_vowels function
    print("\nTesting count_vowels function:")
    test_cases = [
        (["hello"], 2, "Simple word"),
        (["AEIOU"], 5, "All vowels"),
        (["BCDFG"], 0, "No vowels"),
        ([""], 0, "Empty string")
    ]
    harness.run_test_suite(count_vowels, test_cases)