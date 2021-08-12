# Given an array of equal-length strings arr[], the task 
#is to make all the strings of the array equal by replacing 
#any character of a string with any other character, 
#minimum number of times.For example, with 3 changes,
#{ “west”, “east”, “wait” } -> { “wast”, “wast”, “wast” } 
def minOperation(arr, N):
    cntMinOP = 0;# Stores minimum count of operations (answer)
    M = len(arr[0]);#M is length of each string
    #Value of a character (ord) is in range 0-255
    #hash[i][j]: Stores frequency of character j at i th place
    # arr[0] = a b c d      w e s t
    # arr[1] = b c d e      e a s t
    # arr[2] = c d e f      w a i t
    #a         1 0 0 0  w   2 0 0 0
    #b         1 1 0 0  e   1 1 0 0
    #c         1 1 1 0  a   0 2 0 0
    #d         0 1 1 1  s   0 0 2 0
    #e         0 0 1 1  i   0 0 1 0
    #f         0 0 0 1  t   0 0 0 3
   
    
    #Create a matrix named hash having M columns and 256 rows
    #List of 256 lists each having M elements(i= column, j= row)
    hash = [[0 for i in range(M)] for j in range(256)];
    # Traverse the array arr
    for i in range(N):
        # Iterate over characters of current String
        for j in range(M):
            # Update frequency of char value at  arr[i][j]
            ascii_val = ord(arr[i][j]);
            hash[ascii_val][j] += 1;
    # Hash is ready. Now Traverse the hash array
    #Find columnwise sum and max values(i= column, j= row)
    word = ''
    for i in range(M):
        Max = 0;#Initialize column max 0
        # Iterate over all possible characters
        for j in range(256):
            if Max < hash[j][i]:
               Max = hash[j][i] 
               char= chr(j)
            #Max = max(Max, hash[j][i]);# Update Max
        #Find char with maximum Count in a column. Keep that
        #and replace others.Number of replacements = N - max
        # Update cntMinOP
        word += char
        cntMinOP += (N - Max);
    print(word)
    return cntMinOP;
 
# Driver Code
#arr = ["abcd", "bcde", "cdef"];
arr = ["west", "east", "wait","rest"]
N = len(arr);
print(minOperation(arr, N));
 
