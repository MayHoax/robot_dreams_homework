def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

while True:
    fib = fibonacci_generator()
    n = int(input("Enter a number: "))
    for i in range(n):
        next_fib = next(fib)
    print(next_fib)