def is_armstrong_number(number):
    # Convert to string 
    num_str = str(number)
    length = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the length
    sum_num = sum(int(digit) ** length for digit in num_str)
    
    # Return True if the sum equals the original number, otherwise False
    return sum_num == number