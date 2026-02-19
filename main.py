def add(a, b):
    return a + b

# INTENTIONAL BUG 1: Syntax Error (Missing colon)
def sub(a, b)
    return a - b

# INTENTIONAL BUG 2: Indentation Error
def mul(a, b):
return a * b

# INTENTIONAL BUG 3: Unused Import (Linting)
import os

if __name__ == "__main__":
    print(add(1, 2))
