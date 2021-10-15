import random
import time

def mergesort(a):
    n = len(a)

    if n > 1:
        p = n//2
        
        # Divides array into left and right parts
        left = a[:p]
        right = a[p:]

        mergesort(left)
        mergesort(right)
        merge(left, right, a)

def merge(a1, a2, a):
    # a1 is left array (ordered)
    # a2 is right array (ordered)
    # a is whole array
    
    p1 = p2 = p = 0
    # p1 is "pointer" for index for a1
    # p2 is "pointer" for index for a2
    # p is "pointer" for index for a


    # iterates through both lists and adds smaller of either to a
    while p1 < len(a1) and  p2 < len(a2):
        if a1[p1] < a2[p2]:
            a[p] = a1[p1]
            p1 += 1
        else:
            a[p] = a2[p2]
            p2 += 1
        p += 1
    
    # if p2 is out of values, add p1's values to a
    while p1 < len(a1):
        a[p] = a1[p1]
        p+=1
        p1+=1
    
    # if p1 is out of values, add p2's values to a
    while p2 < len(a2):
        a[p] = a2[p2]
        p+=1
        p2+=1

'''
#TESTING
arr = [6, 3, 7, 8, 0, 4]
print(arr)
mergesort(arr)
print(arr)

'''


arr=[]

n = 90000
print(n) # to show which number is tested

for i in range(n):
   arr.append(random.randint(0,100))

start_time = time.time()
#print(arr)
mergesort(arr)
#print(arr)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
