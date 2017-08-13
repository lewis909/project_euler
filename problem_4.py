def palindrome(range_start, range_limit):
    palindromic_numbers = []
    for number in range(range_start, range_limit):
        for m in range(range_start, range_limit):
            three_digit_num = number * m
            if str(three_digit_num) == str(three_digit_num)[::-1]:
                palindromic_numbers.append(three_digit_num)
    return max(palindromic_numbers)

print(palindrome(900, 1000))
