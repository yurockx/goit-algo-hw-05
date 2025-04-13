def caching_fibonacci():
    cache = {}    
    def fibonacci(n):
        if n < 1000: #to avoid crashing with large numbers
            if n in cache:
                return cache[n]
            elif n <= 0:
                return 0
            elif n == 1:
                return 1
            else:
                cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
                return cache[n]
        else:
            return f"{n} should be less than 1000"
    return fibonacci

# getting fibonacci func
# fib = caching_fibonacci()

# using fibonacci func to get F numbers
# print(fib(10))  # Виведе 55
# print(fib(100000))
# print(fib(15))  # Виведе 610
