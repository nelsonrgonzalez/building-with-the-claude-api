def greeting():
    print("Hi there")


def calculate_pi(digits=5):
    """
    Calculate pi to the specified number of decimal digits using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Args:
        digits: Number of decimal digits to calculate (default: 5)
    
    Returns:
        float: Value of pi rounded to the specified digits
    """
    def arctan(x, num_terms):
        """Calculate arctan using Taylor series expansion"""
        result = 0
        x_squared = x * x
        x_power = x
        for n in range(num_terms):
            sign = (-1) ** n
            result += sign * x_power / (2 * n + 1)
            x_power *= x_squared
        return result
    
    # Use more terms for higher precision
    num_terms = 500
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi_over_4 = 4 * arctan(1/5, num_terms) - arctan(1/239, num_terms)
    pi_value = 4 * pi_over_4
    
    # Round to specified digits
    return round(pi_value, digits)
