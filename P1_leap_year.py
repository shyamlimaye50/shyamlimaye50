n = int(input("Enter the year you want to check if is leap year or not: "))
if(((n%4 == 0) and (n%100 !=0))or (n%400 == 0)):
    print("The year {} is a leap year".format(n))
else:
    print("The year {} is not a leap year".format(n))
