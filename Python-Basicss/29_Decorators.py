import time

##wrapper function
def time_counter(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__ + " took " + str((end_time - start_time)*1000) + " milliseconds")
        return result
    return wrapper

@time_counter
def cal_square(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result

@time_counter
def cal_cube(numbers):
    result = []
    for n in numbers:
        result.append(n*n*n)
    return result

numbers = range(1, 1000000)

cal_square(numbers)
cal_cube(numbers)
