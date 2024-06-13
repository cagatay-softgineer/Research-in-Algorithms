import random

ARR_LEN = 1000
MIN_VALUE = 1
MAX_VALUE = 10000 

TEST_ARR = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARR_LEN)]

# Bubble SORT

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for idx in range(i):
            if arr[idx] > arr[idx+1]:
                temp = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = temp
    return arr

# Merge SORT

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
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