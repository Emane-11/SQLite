def square(number):
    if 1<= number <= 64:
        grains = 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")
    return grains
    


def total():
    return sum(2**i for i in range(64))
    
