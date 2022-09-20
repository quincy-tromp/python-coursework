# Practicing using Decorators
import time

def speed_calc_function(function):
    def calc_function():
        start_time = time.time()
        function()
        end_time = time.time()
        time_difference = end_time - start_time
        print(f"Calculation complete!\n\tThe {function.__name__} run speed: {time_difference}s.")
    return calc_function

@speed_calc_function
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_function
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()