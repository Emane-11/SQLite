def steps(number: int):
    # Step 1: Guard clause against invalid inputs
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    i = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2  # Integer division
        else:
            number = (number * 3) + 1
        
        i += 1  # Incrementing the counter outside the if/else avoids repeating code!
        
    return i  # Return after the loop finishes
