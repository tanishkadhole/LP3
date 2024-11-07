def fibonacci(n):
    """Recursive Fibonacci function."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_iteration(n):
    """Iterative Fibonacci function."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]


def step_count_recursion(n):
    """Count steps for the recursive Fibonacci function."""
    if n <= 1:
        return 1
    return step_count_recursion(n - 1) + step_count_recursion(n - 2)


def step_count_iteration(n):
    """Count steps for the iterative Fibonacci function."""
    count = 0
    if n > 0:
        count += 1  # Count for the fib[1]
    if n > 1:
        count += 1  # Count for the fib[2]
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
        count += 1
    return count


if __name__ == "__main__":
    n = int(input("Enter the number of Fibonacci numbers to calculate: "))
    
    # Calculate Fibonacci numbers
    fib_recursion = fibonacci(n)
    steps_recursion = step_count_recursion(n)
    
    fib_iteration = fibonacci_iteration(n)
    steps_iteration = step_count_iteration(n)
    
    # Output results
    print("Fibonacci Recursion Number:", fib_recursion)
    print("Fibonacci Recursion Steps:", steps_recursion)
    print("Fibonacci Iteration Number:", fib_iteration)
    print("Fibonacci Iteration Steps:", steps_iteration)
