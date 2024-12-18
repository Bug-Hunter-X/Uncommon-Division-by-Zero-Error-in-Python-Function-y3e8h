# Uncommon Division by Zero Bug in Python

This repository demonstrates a subtle division-by-zero error in a Python function. The function partially handles division by zero but fails when both the numerator and denominator are zero. This is a less common type of division by zero error, highlighting the importance of robust error handling.

## Bug Description
The `function_with_uncommon_error` function correctly handles division by zero when the denominator is zero and the numerator is not. However, it fails to handle the case where both are zero, resulting in a `ZeroDivisionError`.

## Solution
The solution involves adding an explicit check to handle cases where both numerator and denominator are zero before performing the division operation. This ensures that no errors are thrown in any scenario and the function works as intended.  See bugSolution.py for a fix.
