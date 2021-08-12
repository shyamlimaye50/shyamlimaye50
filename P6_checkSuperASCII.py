def checkSuperASCII(s):
    #Create a frequency table f having 1..26 buckets , initially all zeroes
    #Where f[1] = count of a's, f[2] = count of b's...(ASCII a = 97)
    f = [0 for i in range(27)]
    # Traverse the string to fill frequency table
    for i in range(len(s)):
        f[ord(s[i])-96] += 1 #Increment count for letter s[i]
    #Traverse the string again to check super condition
    for c in s:
        if f[ord(c)-96] != ord(c)-96:
            print('no')
            return
    print('yes')
    return

# Driver code
s = "bcbccadddd" #Given string
checkSuperASCII(s)