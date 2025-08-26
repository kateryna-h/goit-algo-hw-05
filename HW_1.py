def caching_fibonacci(cache=None):
    if cache is None:
        cache = {} # створення порожнього словника для збереження значень

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in cache:
                return cache[n]
            #обчислення чисел Фібоначчі
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
        
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci() 
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(0)) 
print(fib(1))
print(fib(10))
print(fib(15))

