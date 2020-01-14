#Kinley Lab | Week 2 Class 1
st = "Test"
print(st)

import random
l = list(range(10))
random.shuffle(l)
print("before:", l)

for i in range(len(l)):
    print("hello world", i)
    for j in range(0, len(l)-i-1): #This function is called a bubble sort, because the large numbers bubble down
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]

print("after:", l)