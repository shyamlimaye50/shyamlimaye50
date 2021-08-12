#Missing coins
#Default for split is whitespace
#coins = [int(item) for item in 
#         input("Enter the coins(Comma separated) : ").split(',')] 
coins = [5,7,2,7,5,2,5]
for c in coins:         #Scan all coins in array
    k = coins.count(c)  #Find count of the value  
    if c%2:             #If count is odd, this is the culprit
        print(c)
        break
    