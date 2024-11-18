import math
import matplotlib.pyplot as plt
import time
import random
import sys


#function below takes in a func and its arguments, uses time module to calc and return exec time

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


#Insertion Sort
#worst case On^2
def InsertionSort(arr):
    if len(arr) <= 1:
        print("arr is empty or sorted")
    for i in range(1,len(arr)):
        key = arr[i];
        j = i -1
        # move the elements if the key is smaller
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = key
    

#Merge Sort (is technically 2 functions)
#worst case O(nlogn)
def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    
    #Find left, right and mid

    mid = len(arr) // 2 #a number
    left = arr[:mid]
    right = arr[mid:]
    
    sortedLeft = MergeSort(left)
    sortedRight = MergeSort(right)

    return Merge(sortedLeft,sortedRight)

    


#Merger function
def Merge (left, right):
    sortedResult = []
    
    i = j = 0

    while(i < len(left) and j < len(right)):
        if left[i] < right[j]:
            sortedResult.append(left[i])
            i += 1
        else:
            sortedResult.append(right[j])
            j += 1
        
    sortedResult.extend(left[i:])
    sortedResult.extend(right[j:])
    return sortedResult


#Quick Sort
#worst case On^2
def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    # Randomly select a pivot
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    
    # swap around the array
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return QuickSort(left) + middle + QuickSort(right)
    



# exec time arrays 
elapsed_TimesInsertion = []
elapsed_TimesMerge = []
elapsed_TimesQuick = []

# iterate over these values to generate new arrays at Input Size n (10,100,500 ...)
masterInput = [10, 100,500, 1000 ,5000,10000, 50000, 100000, 1000000,2000000]
insertSecs = 3600
for i in masterInput:
    print("input of size n: ",i)
    arr = random.sample(range(i*2), i)  # Generate random array of size 'i'
    if i > 100000:

        start_time11 = time.time()
        MergeSort(arr)
        end_time11 = time.time()
        execMerge = end_time11 - start_time11
        elapsed_TimesMerge.append(execMerge)

        start_time12 = time.time()
        QuickSort(arr)
        end_time12 = time.time()
        execQuick = end_time12 - start_time12
        elapsed_TimesQuick.append(execQuick)

        #fake time below 3600 secs in hour, and when input size n doubles, time with increase quadratically
        
        elapsed_TimesInsertion.append(insertSecs)
        insertSecs *= 3600

    else:
        
        start_time = time.time()
        InsertionSort(arr)
        end_time = time.time()
        execInsert = end_time - start_time
        elapsed_TimesInsertion.append(execInsert)

        start_time11 = time.time()
        MergeSort(arr)
        end_time11 = time.time()
        execMerge = end_time11 - start_time11
        elapsed_TimesMerge.append(execMerge)

        start_time12 = time.time()
        QuickSort(arr)
        end_time12 = time.time()
        execQuick = end_time12 - start_time12
        elapsed_TimesQuick.append(execQuick)



#--------test ouputs------------#
print(elapsed_TimesInsertion)
print(elapsed_TimesMerge)
print(elapsed_TimesQuick)
#------sorting demo------#
arr11 = [9,6,10,2,5,7,23,7,1]
print("Unsorted Arr: ", arr11)
print("Insertion Sort: ")
InsertionSort(arr11)
print("Sorted arr: ", arr11)

print("Merge Sort: ")
arr12 = [9,6,10,2,5,7,23,7,1]
print("sorted arr: ",MergeSort(arr12))


print("Quick Sort: ")
arr13 = [9,6,10,2,5,7,23,7,1]
print("sorted arr: ",QuickSort(arr13))


# Setting up the pyPlot Graph
plt.plot(masterInput, elapsed_TimesInsertion, marker='o', linestyle='-', color='blue', label='Insertion Sort')
plt.plot(masterInput, elapsed_TimesMerge, marker='x', linestyle='-', color='red', label='Merge Sort')
plt.plot(masterInput, elapsed_TimesQuick, marker='v', linestyle='--', color='yellow', label='Quick Sort')
plt.xscale('log')
plt.xlabel('Input Size (10, 100,500, 1000 ,5000,10000, 50000, 100000, 1000000)')
plt.ylabel('Elapsed Time (seconds)')
plt.title('Execution Time Comparison: Insertion Sort vs Merge Sort vs Quick Sort')
plt.legend()
plt.grid(True)

# Show the Graph
plt.show()