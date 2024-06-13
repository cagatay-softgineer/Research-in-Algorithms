import random

ARR_LEN = 1000
MIN_VALUE = 1
MAX_VALUE = 10000 

TEST_ARR = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARR_LEN)]

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for idx in range(i):
            if arr[idx] > arr[idx+1]:
                temp = arr[idx]
                arr[idx] = arr[idx+1]
                arr[idx+1] = temp
    return arr
            