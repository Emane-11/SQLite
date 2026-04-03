def square(number):
    if 1<= number <= 64:
        grains = 2**(number-1)
    else:
        raise ValueError("square must be between 1 and 64")
    return grains
    
    
def total():
    i=1
    total=0
    
    while i < 65:
        total += 2**(i-1)
        i+= 1
    return total
    
