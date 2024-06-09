from ctypes import c_float, c_int32, cast, byref, POINTER
import numpy as np
import timeit
from functools import partial

def ctypes_isqrt(number):
    """
    Calculate the inverse square root of a number using bit-level manipulation with ctypes.
    
    Args:
        number (float): The number to calculate the inverse square root for.
        
    Returns:
        float: The inverse square root of the input number.
    """
    threehalfs = 1.5
    x2 = float(number) * 0.5
    y = c_float(number)

    # Bit-level manipulation to estimate the inverse square root
    i = cast(byref(y), POINTER(c_int32)).contents.value
    i = c_int32(0x5f3759df - (i >> 1))
    y = cast(byref(i), POINTER(c_float)).contents.value

    # Perform one iteration of Newton's method to refine the estimate
    y = y * (threehalfs - (x2 * y * y))
    return y

def numpy_isqrt(number):
    """
    Calculate the inverse square root of a number using bit-level manipulation with numpy.
    
    Args:
        number (float): The number to calculate the inverse square root for.
        
    Returns:
        float: The inverse square root of the input number.
    """
    threehalfs = 1.5
    x2 = float(number) * 0.5
    y = np.float32(number)
    
    # Bit-level manipulation to estimate the inverse square root
    i = y.view(np.int32)
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    y = i.view(np.float32)
    
    # Perform one iteration of Newton's method to refine the estimate
    y = y * (threehalfs - (x2 * y * y))
    return float(y)

def normal_isqrt(number):
    """
    Calculate the inverse square root of a number using the standard power operator.
    
    Args:
        number (float): The number to calculate the inverse square root for.
        
    Returns:
        float: The inverse square root of the input number.
    """
    return float(number) ** -0.5

def apply_ctypes_isqrt(numbers):
    """
    Apply the ctypes_isqrt function to a list of numbers.
    
    Args:
        numbers (list of float): The list of numbers to process.
        
    Returns:
        list of float: The inverse square roots of the input numbers.
    """
    return [ctypes_isqrt(num) for num in numbers]

def apply_numpy_isqrt(numbers):
    """
    Apply the numpy_isqrt function to a list of numbers.
    
    Args:
        numbers (list of float): The list of numbers to process.
        
    Returns:
        list of float: The inverse square roots of the input numbers.
    """
    return [numpy_isqrt(num) for num in numbers]

def apply_normal_isqrt(numbers):
    """
    Apply the normal_isqrt function to a list of numbers.
    
    Args:
        numbers (list of float): The list of numbers to process.
        
    Returns:
        list of float: The inverse square roots of the input numbers.
    """
    return [normal_isqrt(num) for num in numbers]

# Generate a list of floating-point numbers from 1 to 100,000
float_numbers_list = [float(i) for i in range(1, 10001)]

# Create partial functions that will apply the respective sqrt function to float_numbers_list
Ctypes_INVSQRT = partial(apply_ctypes_isqrt, float_numbers_list)
Np_INVSQRT = partial(apply_numpy_isqrt, float_numbers_list)
Normal_INVSQRT = partial(apply_normal_isqrt, float_numbers_list)

# Time the execution of apply_ctypes_isqrt
time_method1 = timeit.timeit(Ctypes_INVSQRT, number=100)
print(f"Ctypes_INVSQRT took {time_method1:.24f} seconds")

# Time the execution of apply_numpy_isqrt
time_method2 = timeit.timeit(Np_INVSQRT, number=100)
print(f"Np_INVSQRT took {time_method2:.24f} seconds")

# Time the execution of apply_normal_isqrt
time_method3 = timeit.timeit(Normal_INVSQRT, number=100)
print(f"Normal_INVSQRT took {time_method3:.24f} seconds")