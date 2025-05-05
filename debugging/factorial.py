#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Décrémenter n pour éviter une boucle infinie
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        f = factorial(int(sys.argv[1]))
        print(f)
    except ValueError:
        print("Please enter a valid integer.")
        sys.exit(1)
