import random
import time

start_time = time.time()

def towerofhanoi():
    print()


arr=[]

n = 50000000
print(n) # to show which number is tested

for i in range(n):
   arr.append(random.randint(0,100))

#print(arr)
towerofhanoi(arr)
#print(arr)
print("Process finished --- %s seconds ---" % (time.time() - start_time))