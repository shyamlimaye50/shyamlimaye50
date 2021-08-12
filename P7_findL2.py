#Find lowest two numbers of an array
def findL2(a):
    min1 = min(a[0],a[1])
    min2 = max(a[0],a[1])
    n= len(a)
    for i in range(2,n):
        if a[i] < min1:
            min2 = min1
            min1 = a[i]
        elif a[i] < min2:
            min2 = a[i]
    return(min1,min2)
#Driver
print(findL2([44, 85, 41, 95, 70, 81, 77, 70, 16, 52]))
print(findL2([1,2,3,4,5]))