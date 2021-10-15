import random
import time

start_time = time.time()

def matrixmult(mult1, mult2, prod):
    print()



# MATRIX GENERATION
a = []
b = []
c = []
n = 3

for i in range(n):
    a1 = []
    b1 = []
    c1 = []
    for j in range(n):
        a1.append(random.randint(0,10))
        b1.append(random.randint(0,10))
        c1.append(0)
    a.append(a1)
    b.append(b1)
    c.append(c1)

#print(a)
#print(b)
#print(c)

#print(arr)
matrixmult(a, b, c)
#print(arr)
print("Process finished --- %s seconds ---" % (time.time() - start_time))