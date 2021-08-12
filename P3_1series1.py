#Find the 15th term of the series? (Ans 49)
#0,0,7,6,14,12,21,18, 28 (numbering starts from 1)
n = int(input("Enter the number: "))
if(n%2):
    print("The {} th number = {}".format(n,7*(n-1)/2))
else:
    print("The {} th number = {}".format(n,(n/2-1)*6))
