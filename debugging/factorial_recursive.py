#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
    This function calculates the factorial of a given integer `n` using recursion.
    
    Parameters:
    n (int): The integer for which the factorial will be calculated. It should be a non-negative integer.
    
    Returns:
    int: The factorial of the integer `n`. If `n` is 0, the function returns 1 as the base case of the recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Convert the first command-line argument to an integer and calculate the factorial
f = factorial(int(sys.argv[1]))

# Output the result to the console
print(f)
