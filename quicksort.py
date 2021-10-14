import random
import time

start_time = time.time()

def quicksort(low, high):
    pivotpoint = 0
    if low < high:
        partition(low, high, pivotpoint)
        quicksort(low, pivotpoint-1)
        quicksort(pivotpoint + 1, high)

def partition(low, high, ppoint):
    i = low + 1
    j = low
    pivotitem = arr[low]
    while i <= high:
        if arr[i] < pivotitem:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]

# TESTING
arr = [9, 2, 7, 8, 1]
print()
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