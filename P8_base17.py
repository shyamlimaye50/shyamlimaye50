#naive method
def value(x):
    x = x.upper()
    if x >= 'A': v = ord(x) - ord('A') +10
    else:        v = ord(x) - ord('0') 
    return v
num = str(input())
n = len(num)
decnum = 0
for i in range(n):
    decnum += value(num[n-i-1])* 17**i
print(decnum)
# smart method
print(int(num,17))

