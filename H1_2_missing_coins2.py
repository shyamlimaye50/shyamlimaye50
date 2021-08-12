#Missing coins
#Default for split is whitespace
#coins = [int(item) for item in 
#         input("Enter the coins(Comma separated) : ").split(',')] 
coins = [5,7,2,7,5,2,5]
xor = 0
for c in coins:
    xor ^= c
print(xor)
    