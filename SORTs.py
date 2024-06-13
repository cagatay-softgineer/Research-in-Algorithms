import random
from functools import partial
import timeit
import util


PRINT_RESULT = False
PRINT_DETAILS_ABOUT_ALGORITHMS = False
TIME_IT_ALGORITMS = True

ARR_LEN = 1000
MIN_VALUE = 1
MAX_VALUE = 10000 

TEST_ARR = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARR_LEN)]


# Bubble SORT

def bubbleSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    for i in range(len_arr-1,0,-1):
        for idx in range(i):
            if arr[idx] > arr[idx+1]:
                temp = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = temp
    return arr


# Merge SORT

def mergeSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    middle = len_arr // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)
    return list(merge(left_arr,right_arr))

def merge(left_half,right_half):
    res = []
    while len(left_half) > 0 and len(right_half) > 0:
        if left_half[0] < right_half[0]:
            res.append(left_half.pop(0))
        else:
            res.append(right_half.pop(0))
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


# Insertion SORT

def insertionSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    for i in range(1, len_arr):
        j = i - 1
        next_element = arr[i]
        
        while (arr[j] > next_element) and (j >= 0):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = next_element
    return arr 


# Shell SORT

def shellSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    gap = len_arr // 2
    while gap > 0:
        for i in range(gap, len_arr):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j = j - gap
            arr[j] = temp
        gap = gap // 2 
    return arr


# Quick SORT

def quickSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    pivot = arr[len_arr // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort(left) + middle + quickSort(right)


# Selection SORT

def selectionSort(arr):
    arr = arr.copy()
    len_arr = len(arr)
    for i in range(len_arr):
        min_idx = i
        for j in range(i+1, len_arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx],arr[i]
    return arr
            
if TIME_IT_ALGORITMS:
    print("\n###############\n###  TIMEs  ###\n###############\n")
    
    print(f"BUBBLE_SORT took {util.Calc_time(bubbleSort,TEST_ARR,100)} seconds")
    print(f"MERGE_SORT took {util.Calc_time(mergeSort,TEST_ARR,100)} seconds")
    print(f"INSERTION_SORT took {util.Calc_time(insertionSort,TEST_ARR,100)} seconds")
    print(f"SHELL_SORT took {util.Calc_time(shellSort,TEST_ARR,100)} seconds")
    print(f"QUICK_SORT took {util.Calc_time(quickSort,TEST_ARR,100)} seconds")
    print(f"SELECTION_SORT took {util.Calc_time(selectionSort,TEST_ARR,100)} seconds")


if PRINT_RESULT:
    print("\n###############\n###  SORTs  ###\n###############\n")
    print(f"TEST ARRAY\n{TEST_ARR}\n\n")
    print(f"BUBBLE SORT\n{bubbleSort(TEST_ARR)}\n\n")
    print(f"MERGE SORT\n{mergeSort(TEST_ARR)}\n\n")
    print(f"INSERTION SORT\n{insertionSort(TEST_ARR)}\n\n")
    print(f"SHELL SORT\n{shellSort(TEST_ARR)}\n\n")
    print(f"QUICK SORT\n{quickSort(TEST_ARR)}\n\n")
    print(f"SELECTION SORT\n{selectionSort(TEST_ARR)}\n\n") 
    
if PRINT_DETAILS_ABOUT_ALGORITHMS:
    print("\n###############\n### DETAILS ###\n###############\n")
    print("-BUBBLE SORT-\nBest Case: 𝑂(𝑛) - when the array is already sorted.\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")
    print("-MERGE SORT-\nBest Case: 𝑂(𝑛 log 𝑛)\nAverage Case: 𝑂(𝑛 log 𝑛)\nWorst Case:: 𝑂(𝑛 log 𝑛)\n")
    print("-INSERTION SORT-\nBest Case: 𝑂(𝑛) - when the array is already sorted.\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")
    print("-SHELL SORT-\nBest Case: 𝑂(𝑛 log 𝑛) - depends on the gap sequence\nAverage Case: 𝑂(𝑛^(3/2)) - depends on the gap sequence, can be better with specific sequences\nWorst Case:: 𝑂(𝑛^2) - depends on the gap sequence\n")
    print("-QUICK SORT-\nBest Case: 𝑂(𝑛 log 𝑛)\nAverage Case: 𝑂(𝑛 log 𝑛)\nWorst Case:: 𝑂(𝑛^2) - when the pivot selection is poor (e.g., always picking the smallest or largest element as the pivot in a sorted or reverse sorted array)\n")
    print("-SELECTION SORT-\nBest Case: 𝑂(𝑛^2)\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")