import time

start_time = time.time()

def TowerOfHanoi(discs, moveFrom, moveTo, other):
    if discs==1:
        print("Move disk", discs, "from peg", moveFrom, "to peg", moveTo)
        return
    else:
        TowerOfHanoi(discs-1, moveFrom, other, moveTo)
        print("Move disk", discs, "from peg", moveFrom, "to peg", moveTo)
        TowerOfHanoi(discs-1, other, moveTo, moveFrom)

         
n = 32
print(n) # to show which number is tested
TowerOfHanoi(n, 'a', 'b', 'c')
print("Process finished --- %s seconds ---" % (time.time() - start_time))