# n should be received from main thread
def nth_fibonacci(n):
    return n < 2 if n else nth_fibonacci(n - 1) + nth_fibonacci(n - 2)


def send_result():
    # This function sends result of nth_fibonacci computations to main thread
    # Add Randomize worker execution timeout for a different results
    # Write your code here
    pass


send_result()
