def multilples_of_3_5(number):
    number_list = []
    for num in range(number):
        if num % 3 == 0 or num % 5 == 0:
            number_list.append(num)
    return sum(number_list)

print(multilples_of_3_5(1000))
