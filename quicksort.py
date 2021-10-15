import random
import time

start_time = time.time()

def partition(low, high):
    #pivotpoint = low
    i = low + 1
    j = low
    pivotitem = arr[low]
    print("q")
    while i < high:
        print("j")
        if arr[i] < pivotitem:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]
    pivotpoint = high

def quicksort(low, high):
    #pivotpoint = low
    if low < high:
        partition(low, high)
        quicksort(low, pivotpoint-1)
        quicksort(pivotpoint+1, high) #idk

# TESTING
arr = [9, 2, 7, 8, 1]
pivotpoint = 0
print(arr)
quicksort(0, len(arr)-1)
print(arr)
'''
arr=[]

n = 50000000
print(n) # to show which number is tested

for i in range(n):
   arr.append(random.randint(0,100))

#print(arr)
quicksort(arr)
#print(arr)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
'''