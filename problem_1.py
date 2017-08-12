def multiples_of_3_5(number):
    result = 0
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result

print(multiples_of_3_5(1000))
