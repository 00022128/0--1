def fibonacci(n):
    fib_generator = [0, 1]
    while len(fib_generator) < n:
        fib_generator.append(fib_generator[-1] + fib_generator[-2])
    return fib_generator[:n]

n = int(input('Enter a number: '))
print(fibonacci(n))