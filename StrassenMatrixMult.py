import random
import time

def quarter(mat): # split matrix into quarters 
    a = mat
    b = mat
    c = mat
    d = mat
    while(len(a) > len(mat)/2):
        a = a[:len(a)//2]
        b = b[:len(b)//2]
        c = c[len(c)//2:]
        d = d[len(d)//2:]
    while(len(a[0]) > len(mat[0])/2):
        for i in range(len(a[0])//2):
            a[i] = a[i][:len(a[i])//2]
            b[i] = b[i][len(b[i])//2:]
            c[i] = c[i][:len(c[i])//2]
            d[i] = d[i][len(d[i])//2:]
    return a,b,c,d

def add(a, b):
    if type(a) == int:
        d = a + b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] + b[i][j])
            d.append(c)
    return d

def sub(a, b):
    if type(a) == int:
        d = a - b
    else:
        d = []
        for i in range(len(a)):
            c = []
            for j in range(len(a[0])):
                c.append(a[i][j] - b[i][j])
            d.append(c)
    return d


def strassen(a, b):
    # base case: 1x1 matrix
    if len(a) == 1:
        d = [[0]]
        d[0][0] = a[0][0] * b[0][0]
        return d
    else:
        #split matrices into quarters
        a11, a12, a21, a22 = quarter(a)
        b11, b12, b21, b22 = quarter(b)

        # p = (a11 + a22) * (b11 + b22)
        p = strassen(add(a11, a22), add(b11, b22))

        # q = (a21 + a22) * b11
        q = strassen(add(a21, a22), b11)

        # r = a11 * (b12 - b22)
        r = strassen(a11, sub(b12, b22))

        # s = a22 * (b21 - b11)
        s = strassen(a22, sub(b21, b11))

        # t = (a11 + a12) * b22
        t = strassen(add(a11, a12), b22)

        # u = (a21 - a11) * (b11 + b12)
        u = strassen(sub(a21, a11), add(b11, b12))

        # v = (a12 - a22) * (b21 + b22)
        v = strassen(sub(a12, a22), add(b21, b22))


        # c11 = p1 + p4 - p5 + p7
        c11 = add(sub(add(p, s), t), v)

        # c12 = p3 + p5
        c12 = add(r, t)

        # c21 = p2 + p4
        c21 = add(q, s)

        # c22 = p1 + p3 - p2 + p6
        c22 = add(sub(add(p, r), q), u)

        c = [[0 for row in range(len(c11)*2)] for col in range(len(c11)*2)]
        
        for i in range(len(c11)):
            for j in range(len(c11)):
                c[i][j]                   = c11[i][j]
                c[i][j+len(c11)]          = c12[i][j]
                c[i+len(c11)][j]          = c21[i][j]
                c[i+len(c11)][j+len(c11)] = c22[i][j]

        return c

a = []
b = []
n = 1024
print(n)

for i in range(n):
    a1 = []
    b1 = []
    c1 = []
    for j in range(n):
        a1.append(random.randint(0,10))
        b1.append(random.randint(0,10))
    a.append(a1)
    b.append(b1)



# CONTROLLED MATRIX GENERATION
#a = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
#b = [[1, 2, 1], [2, 4, 6], [7, 2, 5]]
#c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#c-> [[26,16,28],[56,40,64],[86,64,100]]

start_time = time.time()
strassen(a, b)
print("Process finished --- %s seconds ---" % (time.time() - start_time))