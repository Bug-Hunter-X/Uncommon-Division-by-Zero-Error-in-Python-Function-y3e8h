def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Correct handling of a == 0
    elif b == 0:
        return a
    else:
        result = a / b
        return result

# Uncommon error: Division by zero exception is only handled partially
# It correctly handles the case when the denominator is zero only when the numerator is not zero.
# This is not the case when both numerator and denominator are zeros, which leads to division by zero.

#Example showing the error:
print(function_with_uncommon_error(0,0))

# Example demonstrating the lack of handling for both zero cases.
print(function_with_uncommon_error(0, 0)) # ZeroDivisionError

# The function should have explicit checks for both the numerator and denominator to be 0 to fully handle division by zero exceptions.
