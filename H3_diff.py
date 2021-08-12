#Difference of pair = target
'''
n = input('Number of elements')
k = input('Target diference')
a = [int(item) for item in 
        input("Enter the numbers(Comma separated) : ").split(',')] 
'''
n=5
k=2
#a=[1,5,3,4,2]
a=[1,5,3,4,2,9,8,11,15,20,17]
#Brute force method
count = 0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j]) == k:
            count += 1
            print(a[i],a[j])
print('count(brute)=',count)
#Hash table method
count = 0
s = set(a) #Convert list into a set
for num in s:
    if (num+k in s):
        print(num, num+k)
        count += 1
print('count(hash)=',count)