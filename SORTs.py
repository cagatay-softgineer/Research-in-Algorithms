import random
import util
import time
import threading


PRINT_RESULT = False
PRINT_DETAILS_ABOUT_ALGORITHMS = False
TIME_IT_ALGORITMS = False
TIME_IT_ALGORITMS_ITER_COUNT = 100

ARR_LEN = 30
MIN_VALUE = 1
MAX_VALUE = 100 

TEST_ARR = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(ARR_LEN)]

# Bubble SORT

def bubbleSort(arr):
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
    len_arr = len(arr)
    if len_arr <= 1:
        return arr
    middle = len_arr // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    left_arr = mergeSort(left_arr)
    right_arr = mergeSort(right_arr)
    return list(merge_halfs(left_arr,right_arr))

def merge_halfs(left_half,right_half):
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
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Shell SORT

def shellSort(arr):
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
    len_arr = len(arr)
    for i in range(len_arr):
        min_idx = i
        for j in range(i+1, len_arr):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx],arr[i]
    return arr


# Count SORT

def countSort(input_array):
    M = max(input_array)
    count_array = [0] * (M + 1)
    
    for num in input_array:
        count_array[num] += 1
        
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(input_array)
 
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
 
    return output_array


# Radix SORT

def countingSort(arr, exp1):

    n = len(arr)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max1 = max(arr)
    
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10
    return arr


# Bucket SORT

def bucketSort(arr):
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for num in arr:
        bi = int(n * num)
        
        # Ensure bi is within valid range
        if bi >= n:
            bi = n - 1
        
        buckets[bi].append(num)

    # Sort each bucket using insertion sort
    for i in range(n):
        insertionSort(buckets[i])

    # Concatenate sorted buckets back into arr
    index = 0
    for i in range(n):
        for num in buckets[i]:
            arr[index] = num
            index += 1

    return arr


# Bingo SORT

def bingoSort(arr):
    bingo = min(arr)

    largest = max(arr)
    nextBingo = largest
    nextPos = 0
    while bingo < nextBingo:

        startPos = nextPos
        for i in range(startPos, len(arr)):
            if arr[i] == bingo:
                arr[i], arr[nextPos] = arr[nextPos], arr[i]
                nextPos += 1

            elif arr[i] < nextBingo:
                nextBingo = arr[i]
        bingo = nextBingo
        nextBingo = largest

    return arr
            
            
# Pigeonhole SORT

def pigeonholeSort(arr):
    my_min = min(arr)
    my_max = max(arr)
    size = my_max - my_min + 1

    holes = [0] * size

    for x in arr:
        assert isinstance(x,int), "integers only please"
        holes[x - my_min] += 1

    i = 0
    for count in range(size):
        while holes[count] > 0:
            holes[count] -= 1
            arr[i] = count + my_min
            i += 1
            
    return arr


# Cycle SORT

def cycleSort(arr):
    writes = 0

    for cycleStart in range(0, len(arr) - 1):
      item = arr[cycleStart]

      pos = cycleStart
      for i in range(cycleStart + 1, len(arr)):
        if arr[i] < item:
          pos += 1

      if pos == cycleStart:
        continue

      while item == arr[pos]:
        pos += 1
      arr[pos], item = item, arr[pos]
      writes += 1

      while pos != cycleStart:

        pos = cycleStart
        for i in range(cycleStart + 1, len(arr)):
          if arr[i] < item:
            pos += 1

        while item == arr[pos]:
          pos += 1
        arr[pos], item = item, arr[pos]
        writes += 1
    
    return arr


# Cocktail SORT

def cocktailSort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped is True):
        swapped = False

        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                
        if (swapped is False):
            break
        swapped = False
        end = end-1

        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        start = start + 1
    return arr
    
    
# Strand SORT

def strandSort(arr):
    def merge_lists(list1, list2): 
        result = [] 
        while list1 and list2: 
            if list1[0] < list2[0]: 
                result.append(list1.pop(0)) 
            else: 
                result.append(list2.pop(0)) 
        result += list1 
        result += list2 
        return result 

    if len(arr) <= 1: 
        return arr 
    sublist = [arr.pop(0)] 
    i = 0
    
    while i < len(arr): 
        if arr[i] > sublist[-1]: 
            sublist.append(arr.pop(i)) 
        else: 
            i += 1
    sorted_sublist = sublist 
    remaining_list = strandSort(arr) 

    return merge_lists(sorted_sublist, remaining_list) 


# Bitonic SORT

def compAndSwap(arr, i, j, dire):
    if arr is None or len(arr) == 0:
        return
    
    if (dire == 1 and arr[i] > arr[j]) or (dire == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonicMerge(arr, low, cnt, dire):
    if cnt > 1:
        k = cnt//2
        for i in range(low , low+k):
            arr = compAndSwap(arr, i, i+k, dire)
        bitonicMerge(arr, low, k, dire)
        bitonicMerge(arr, low+k, k, dire)
 
def bitonicSort(arr,low = 0, cnt = None,dire = 1):
    if cnt is None:
        cnt = len(arr)
        
    if cnt > 1:
          k = cnt//2
          bitonicSort(arr, low, k, 1)
          bitonicSort(arr, low+k, k, 0)
          bitonicMerge(arr, low, cnt, dire)
    return arr


# Pancake SORT

def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
    return arr

def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi

def pancakeSort(arr):
    curr_size = len(arr)
    while curr_size > 1:
        mi = findMax(arr, curr_size)
        if mi != curr_size-1:
            arr = flip(arr, mi)
            arr = flip(arr, curr_size-1)
        curr_size -= 1
    return arr


# Bogo SORT

def bogoSort(arr):
    start_time = time.time()
    time_limit = min(len(arr) // 10,1)
    while (not is_sorted(arr)):
        if time.time() - start_time > time_limit:
            return ("Time limit exceeded")
        random.shuffle(arr)
    
    return arr

def is_sorted(arr):
    n = len(arr)
    for i in range(0, n-1):
        if (arr[i] > arr[i+1]):
            return False
    return True
 
def shuffle(arr):
    n = len(arr)
    for i in range(0, n):
        r = random.randint(0, n-1)
        arr[i], arr[r] = arr[r], arr[i]
        
        
# Gnome SORT

def gnomeSort(arr):
    n = len(arr)
    index = 0
    while index < n: 
        if index == 0: 
            index = index + 1
        if arr[index] >= arr[index - 1]: 
            index = index + 1
        else: 
            arr[index], arr[index-1] = arr[index-1], arr[index] 
            index = index - 1
  
    return arr 

# Sleep SORT

def routine(num, result_list):
    global start_time
    global time_limit
    time.sleep(num / 10.0)
    if time.time() - start_time > time_limit:
            return ("Time limit exceeded")
    result_list.append(num)

def sleepSort(arr):
    global start_time
    start_time = time.time()
    global time_limit
    time_limit = min(len(arr) // 10,1)
    threads = []
    result = []
    s_time = time.time()
    for num in arr:
        thread = threading.Thread(target=routine, args=(num, result))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        if time.time() - s_time > time_limit:
            return ("Time limit exceeded")
        thread.join()
        
    return result
        

# Stooge SORT

def stoogeSort(arr, l=0, h=None):  # noqa: E741
    if h is None:
        h = len(arr) - 1
    if l >= h: 
        return
    if arr[l]>arr[h]: 
        t = arr[l] 
        arr[l] = arr[h] 
        arr[h] = t 
    if h-l + 1 > 2: 
        t = (int)((h-l + 1)/3) 
        stoogeSort(arr, l, (h-t)) 
        stoogeSort(arr, l + t, (h)) 
        stoogeSort(arr, l, (h-t))
    return arr

# Odd Even SORT

def oddEvenSort(arr):
    n = len(arr)
    isSorted = 0
    while isSorted == 0:
        isSorted = 1
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
                 
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = 0
     
    return arr


# 3-Way Merge SORT

def merge(gArray, low, mid1, mid2, high, destArray):
    i = low
    j = mid1
    k = mid2
    l = low  # noqa: E741

    while ((i < mid1) and (j < mid2) and (k < high)):
        if(gArray[i] < gArray[j]):
            if(gArray[i] < gArray[k]):
                destArray[l] = gArray[i]
                l += 1  # noqa: E741
                i += 1
            else:
                destArray[l] = gArray[k]
                l += 1  # noqa: E741
                k += 1
        else:
            if(gArray[j] < gArray[k]):
                destArray[l] = gArray[j]
                l += 1  # noqa: E741
                j += 1
            else:
                destArray[l] = gArray[k]
                l += 1  # noqa: E741
                k += 1

    while ((i < mid1) and (j < mid2)):
        if(gArray[i] < gArray[j]):
            destArray[l] = gArray[i]
            l += 1  # noqa: E741
            i += 1
        else:
            destArray[l] = gArray[j]
            l += 1  # noqa: E741
            j += 1

    while ((j < mid2) and (k < high)):
        if(gArray[j] < gArray[k]):
            destArray[l] = gArray[j]
            l += 1  # noqa: E741
            j += 1
        else:
            destArray[l] = gArray[k]
            l += 1  # noqa: E741
            k += 1

    while ((i < mid1) and (k < high)):
        if(gArray[i] < gArray[k]):
            destArray[l] = gArray[i]
            l += 1  # noqa: E741
            i += 1
        else:
            destArray[l] = gArray[k]
            l += 1  # noqa: E741
            k += 1

    while (i < mid1):
        destArray[l] = gArray[i]
        l += 1  # noqa: E741
        i += 1
 
    while (j < mid2):
        destArray[l] = gArray[j]
        l += 1  # noqa: E741
        j += 1

    while (k < high):
        destArray[l] = gArray[k]
        l += 1  # noqa: E741
        k += 1
 
 
def mergeSort3WayRec(gArray, low, high, destArray):

    if (high - low < 2):
        return

    mid1 = low + ((high - low) // 3)
    mid2 = low + 2 * ((high - low) // 3) + 1

    mergeSort3WayRec(destArray, low, mid1, gArray)
    mergeSort3WayRec(destArray, mid1, mid2, gArray)
    mergeSort3WayRec(destArray, mid2, high, gArray)

    merge(destArray, low, mid1, mid2, high, gArray)
 
 
def mergeSort3Way(gArray):
    n = len(gArray)
    if (n == 0):
        return
    fArray = []
    fArray = gArray.copy()
    mergeSort3WayRec(fArray, 0, n, gArray)
    gArray = fArray.copy()

    return gArray

SORT_ALGORITHMS=[bubbleSort,mergeSort,insertionSort,shellSort
                     ,quickSort,selectionSort,countSort,radixSort,
                     bucketSort,bingoSort,pigeonholeSort,cycleSort,
                     cocktailSort,strandSort,bitonicSort,pancakeSort,
                     gnomeSort,oddEvenSort,mergeSort3Way,sleepSort,bogoSort]

def getAllSortsNames():
    S = ""
    for method in SORT_ALGORITHMS:
        method_name = method.__name__
        S += f"{method_name}, "
    return S[:-2]

def main():
    if TIME_IT_ALGORITMS:
        print("\n###############\n###  TIMEs  ###\n###############\n")
        for method in SORT_ALGORITHMS:
            method_name = method.__name__
            sort_index = method_name.find("Sort")
            print(f"{method_name[:sort_index].capitalize()} {method_name[sort_index:]} took {util.Calc_time(method,TEST_ARR.copy(),TIME_IT_ALGORITMS_ITER_COUNT)} seconds")
             
    if PRINT_RESULT:
        print("\n###############\n###  SORTs  ###\n###############\n")
        print(f"TEST ARRAY\n{TEST_ARR}\n\n")
        for method in SORT_ALGORITHMS:
            method_name = method.__name__
            sort_index = method_name.find("Sort")
            res = method(TEST_ARR.copy())
            print(f"{method_name[:sort_index].capitalize()} {method_name[sort_index:]} \n{res}")
            print(f"Is {method_name[:sort_index].capitalize()} {method_name[sort_index:]} Sorted : {is_sorted(res)}\n\n")

        print(f"TEST ARRAY\n{TEST_ARR}\n\n")
    
    if PRINT_DETAILS_ABOUT_ALGORITHMS:
        print("\n###############\n### DETAILS ###\n###############\n")
        print("-BUBBLE SORT-\nBest Case: 𝑂(𝑛) - when the array is already sorted.\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")
        print("-MERGE SORT-\nBest Case: 𝑂(𝑛 log 𝑛)\nAverage Case: 𝑂(𝑛 log 𝑛)\nWorst Case:: 𝑂(𝑛 log 𝑛)\n")
        print("-INSERTION SORT-\nBest Case: 𝑂(𝑛) - when the array is already sorted.\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")
        print("-SHELL SORT-\nBest Case: 𝑂(𝑛 log 𝑛) - depends on the gap sequence\nAverage Case: 𝑂(𝑛^(3/2)) - depends on the gap sequence, can be better with specific sequences\nWorst Case:: 𝑂(𝑛^2) - depends on the gap sequence\n")
        print("-QUICK SORT-\nBest Case: 𝑂(𝑛 log 𝑛)\nAverage Case: 𝑂(𝑛 log 𝑛)\nWorst Case:: 𝑂(𝑛^2) - when the pivot selection is poor (e.g., always picking the smallest or largest element as the pivot in a sorted or reverse sorted array)\n")
        print("-SELECTION SORT-\nBest Case: 𝑂(𝑛^2)\nAverage Case: 𝑂(𝑛^2)\nWorst Case:: 𝑂(𝑛^2)\n")
    
    
if __name__ == "__main__":
    main()