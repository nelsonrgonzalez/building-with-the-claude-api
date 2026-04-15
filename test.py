"""
Test file for pi calculation function
"""
import math
from main import calculate_pi


def test_calculate_pi():
    """Test the calculate_pi function"""
    
    # Calculate pi to 5 digits
    calculated_pi = calculate_pi(5)
    
    # The actual value of pi
    actual_pi = math.pi
    
    print("=" * 50)
    print("Testing Pi Calculation")
    print("=" * 50)
    print(f"Calculated pi (5 digits): {calculated_pi}")
    print(f"Actual pi value:          {actual_pi}")
    print(f"Rounded actual pi:        {round(actual_pi, 5)}")
    print(f"Difference:               {abs(calculated_pi - actual_pi):.10f}")
    print("=" * 50)
    
    # Test with different precision levels
    print("\nTesting different precision levels:")
    print("-" * 50)
    for digits in range(1, 11):
        calc_pi = calculate_pi(digits)
        expected = round(math.pi, digits)
        match = "✓" if calc_pi == expected else "✗"
        print(f"{digits} digits: {calc_pi} (expected: {expected}) {match}")
    print("=" * 50)
    
    # Assert the main test case
    assert calculated_pi == round(math.pi, 5), \
        f"Pi calculation failed: expected {round(math.pi, 5)}, got {calculated_pi}"
    
    print("\n✓ All tests passed!")


if __name__ == "__main__":
    test_calculate_pi()
