from test_harness import TestHarness

# Create a function to test
def add_numbers(a, b):
    return a + b

# Create test harness with default settings
harness = TestHarness()

# Or create with specific settings
harness = TestHarness(
    show_hints=True,    # Show helpful hints for failed tests
    use_colours=True    # Use coloured output in terminal
)

# Define test cases
test_cases = [
    ([1, 2], 3, "Simple addition"),
    ([0, 0], 0, "Zero addition"),
    ([-1, 1], 0, "Negative numbers")
]

# Run the tests
harness.run_test_suite(add_numbers, test_cases)