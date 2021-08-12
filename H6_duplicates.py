#Contains duplicates?
nums = [1,5,2,3]

#nums = [int(item) for item in 
#     input("Enter the arrray(Comma separated) : ").split(',')] 
'''
#brute force: Test every pair in two nested loops
flag=0
for i in range(len(nums)):  
    for j in range(i+1,len(nums)):  
        if nums[i] == nums[j]:  
            print(True)
            flag=1
            break
if flag == 0:
    print(False)
'''
#Sorting
nums.sort()                 #Use built-in sort method
flag = 0  
for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:#Any consecutive elements equal?
        print(True)
        flag=1
        break
if flag == 0:
    print(False)
'''
#Set method
#set removes duplicates, so length will reduce
if len(set(nums)) < len(nums):
    print(True)
else:
    print(False)
'''

    
