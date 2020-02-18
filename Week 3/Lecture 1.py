#Finding the largest integer or something

nums = []

def promptNumber1():
    n1 = input('Input the first number: ')
    n1 = int(n1)
    nums.append(n1)

def promptNumber2():
    n2 = input('Input the second number: ')
    n2 = int(n2)
    nums.append(n2)

def promptNumber3():
    n3 = input('Input the third number: ')
    n3 = int(n3)
    nums.append(n3)

def findMax():
    if nums[0] >= nums[1] and nums[0] >= nums[2]:
        print(nums[0])
    # check if n2 is largest
    elif nums[1] >= nums[2]:
        print(nums[1])
    # check if n3 is largest
    else: 
        print(nums[2])

promptNumber1()
promptNumber2()
promptNumber3()
findMax()