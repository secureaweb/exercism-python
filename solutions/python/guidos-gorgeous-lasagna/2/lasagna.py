"""Module providing a function printing python version."""

import sys

def print_python_version():

    print(sys.version)

EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate preparation time based on number of layers."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time (preparation + baking)."""
    return (number_of_layers * 2) + elapsed_bake_time
    