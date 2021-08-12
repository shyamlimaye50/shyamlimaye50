# Python3 Program to find maximum XOR value of a pair
# Utility function checkBit to count number of
# elements having set bit at position of pattern ...0001000...
# Pattern is 1 hot encoding of "bit" in range 31:0
def checkBit(pattern,arr,  n) :
    count = 0
    for i in range(0, n) :
        if ((pattern & arr[i]) == pattern) :
            count = count + 1
    return count
# Function for finding maximum and value pair
def maxAND (arr,  n) :
    res = 0    #Initialize result to 0 
    # iterate over total of 30 bits from msb to lsb
    for bit in range(31,-1,-1) :
        # find the count of elements having set  "bit"
        count = checkBit(res | (1 << bit), arr, n)
        # if count >= 2 set that bit in result
        if ( count >= 2 ) :
            res =res | (1 << bit)
    return res
# Driver function
arr = [4, 8, 6, 2]
n = len(arr)
print("Maximum AND Value = ", maxAND(arr, n))