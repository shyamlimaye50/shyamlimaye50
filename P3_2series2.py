#Find the 16th term of the series? (Ans 2187)
#1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, 64, 729, 128, 2187 …
n = int(input("Enter the number: "))
if(n%2):
    print("The {} th number = {}".format(n,2**((n-1)/2)))
else:
    print("The {} th number = {}".format(n,3**(n/2-1)))


