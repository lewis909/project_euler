def even_last_number(func):
    limit = 4000000
    numbers = [0]
    for num in range(limit):
        result = func(num)
        if result % 2 == 0:
            numbers.append(result)
            if result > limit:
                numbers = numbers[:-1]
                break
    return sum(numbers)


@even_last_number
def fib(n):
    a, b = 0, 1
    for num in range(n):
        a, b = b, a + b
    return a

print(fib)
