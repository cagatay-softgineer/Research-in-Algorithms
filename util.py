import timeit
from functools import partial

def Calc_time(method,test_data,iter_num=1):
    """
    Calculate the execution time of a given method with the provided test data.

    Parameters:
    method (function): The sorting function or any function whose execution time is to be measured.
    test_data (list): The input data for the method.
    iter_num (int): The number of times to execute the method for averaging the time. Default is 1.

    Returns:
    str: The execution time formatted to 24 decimal places.
    """
    test_method = partial(method, test_data)

    time_method = timeit.timeit(test_method, number=iter_num)
    return f"{time_method:.24f}"