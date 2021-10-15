import random
import time

def matrixmult(mult1, mult2, prod):
    n = len(mult1)
    for i in range(n):
        for j in range(n):
            #prod[i][j] = 0
            for k in range(n):
                prod[i][j] = prod[i][j] + mult1[i][k] * mult2[k][j]



# MATRIX GENERATION
a = []
b = []
c = []
n = 1024

print(n)
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

# CONTROLLED MATRIX GENERATION
#a = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
#b = [[1, 2, 1], [2, 4, 6], [7, 2, 5]]
#c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#c-> [[26,16,28],[56,40,64],[86,64,100]]

start_time = time.time()
#print(c)
matrixmult(a, b, c)
#print(c)
print("Process finished --- %s seconds ---" % (time.time() - start_time))