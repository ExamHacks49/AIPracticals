def factorial_iterative(n):
    """
    Calculates the factorial of a given number using iteration.
    """
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculates the factorial of a given number using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number: "));
print(f'Factorial by recursion: {factorial_recursive(number)}')
print(f'Factorial by iteration: {factorial_iterative(number)}')