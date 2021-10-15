import random
import time



def partition(low, high, arr):
    j = low
    pivotitem = arr[low]
    for i in range(low+1, high):
        if arr[i] < pivotitem:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
        i += 1
    pivotpoint = j
    arr[low], arr[pivotpoint] = arr[pivotpoint], arr[low]
    return j
    

def quicksort(low, high, arr):
    if low < high:
        ppoint =  partition(low, high, arr)
        quicksort(low, ppoint, arr)
        quicksort(ppoint + 1, high, arr)

'''
# TESTING
arr = [9, 2, 7, 8, 1]
pivotpoint = 0
print(arr)
quicksort(0, len(arr), arr)
print(arr)
'''
arr=[]

n = 90000
print(n) # to show which number is tested

for i in range(n):
   arr.append(random.randint(0,100))

start_time = time.time()
#print(arr)
pivotpoint = 0
quicksort(0, len(arr), arr)
#print(arr)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
