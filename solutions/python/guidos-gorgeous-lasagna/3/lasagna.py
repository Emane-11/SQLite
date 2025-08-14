
EXPECTED_BAKE_TIME = 40  
PREPARATION_TIME = 2     

number_of_layers = 5
elapsed_bake_time = 10


def bake_time_remaining(bake_time_so_far):
    """Calculate the bake time remaining.

    :param bake_time_so_far: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).
    """
    return EXPECTED_BAKE_TIME - bake_time_so_far


def preparation_time_in_minutes(layers):
    """Calculate preparation time based on the number of layers.

    :param layers: int - the number of lasagna layers.
    :return: int - total preparation time (in minutes).
    """
    return layers * PREPARATION_TIME


def elapsed_time_in_minutes(layers, bake_time_so_far):
    """Calculate total time elapsed in cooking the lasagna.

    :param layers: int - number of lasagna layers.
    :param bake_time_so_far: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).
    """
    return preparation_time_in_minutes(layers) + bake_time_so_far


# Example usage:
print(bake_time_remaining(elapsed_bake_time))              
print(preparation_time_in_minutes(number_of_layers))       
print(elapsed_time_in_minutes(number_of_layers, elapsed_bake_time))
