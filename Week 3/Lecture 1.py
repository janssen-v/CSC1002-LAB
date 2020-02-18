#Finding the largest integer or something
n1 = input('Input the first number')
n2 = input('Input the second number')
n3 = input('Input the third number')

# check if n1 is largest
if n1 >= n2 and n1 >= n3:
    print(n1)
# check if n2 is largest
elif n2 >= n1 and n2 >= n3:
    print(n2)
# check if n3 is largest
else: 
    print(n3)