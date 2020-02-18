#Finding the largest integer or something

nums = []

n1 = input('Input the first number: ')
n2 = input('Input the second number: ')
n3 = input('Input the third number: ')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

nums.append(n1)
nums.append(n2)
nums.append(n3)

# check if n1 is largest
if nums[0] >= nums[1] and nums[0] >= nums[2]:
    print(nums[0])
# check if n2 is largest
elif nums[1] >= nums[0] and nums[1] >= nums[2]:
    print(nums[1])
# check if n3 is largest
else: 
    print(nums[2])