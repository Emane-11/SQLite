def is_armstrong_number(number):
    num_str = str(number)
    length = len(num_str)
    sum_num = sum(int(digit) ** length for digit in num_str)
    return sum_num == number