import math

def mergesort(a):
    n = len(a)
    if n > 1:
        p = n//2
        
        left = a[:p]
        right = a[p:]

        mergesort(left)
        mergesort(right)
        merge(left, right, a)

def merge(a1, a2, a):
    p1 = p2 = p = 0
    while p1 < len(a1) and  p2 < len(a2):
        if a1[p1] < a2[p2]:
            a[p] = a1[p1]
            p1 += 1
        else:
            a[p] = a2[p2]
            p2 += 1
        p += 1
    
    while p1 < len(a1):
        a[p] = a1[p1]
        p+=1
        p1+=1
    
    while p2 < len(a2):
        a[p] = a2[p2]
        p+=1
        p2+=1

arr = [6, 3, 7, 8, 0, 4]
print("Given array is", arr)
mergesort(arr)
print("Sorted array is: ", arr)
