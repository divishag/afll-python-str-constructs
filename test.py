# test.py - Automated test script for the validator
from lexer import lexer
from parser import parser

# Test cases
test_cases = [
    # Valid cases
    ("myStr.upper()", True),
    ("text.lower()", True),
    ("word.capitalize()", True),
    ("data.strip()", True),
    ("sentence.split()", True),
    ("sentence.split(' ')", True),
    ("line.split(\" \", 5)", True),
    ("word.find('hello')", True),
    ("file.startswith('temp')", True),
    ("file.endswith('.txt')", True),
    ("data.count('a')", True),
    ("text.count('the', 5)", True),
    ("str.count('x', 0, 10)", True),
    ("word.replace('a', 'b')", True),
    ("text.replace('old', 'new', 3)", True),
    
    # Invalid cases
    ("myStr.upper(", False),
    ("replace('a', 'b')", False),
    ("myStr.uppercase()", False),
    ("upper()", False),
    ("myStr.", False),
]

def run_tests():
    print("=" * 70)
    print("PYTHON STRING METHOD SYNTAX VALIDATOR - TEST SUITE")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for i, (test_input, expected_valid) in enumerate(test_cases, 1):
        parser.success = True
        
        print(f"Test {i}: {test_input}")
        result = parser.parse(test_input, lexer=lexer)
        
        actual_valid = parser.success
        
        if expected_valid == actual_valid:
            print(f"  [OK] PASS - {'Valid' if expected_valid else 'Invalid'} as expected")
            passed += 1
        else:
            print(f"  [X] FAIL - Expected {'valid' if expected_valid else 'invalid'}, got {'valid' if actual_valid else 'invalid'}")
            failed += 1
        
        print()
    
    print("=" * 70)
    print(f"RESULTS: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print("=" * 70)

if __name__ == "__main__":
    run_tests()
