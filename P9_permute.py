def permute(aa,l=0): #l is left end of substring, initially 0
    a=list(aa)       #If aa is string, convert it to list
    print(aa,l)      #For debugging
    if l == len(a) : print('Permutation '+''.join(a)) #Exit from recursion
    else:
        for i in range(l,len(a)):  
            a[l],a[i] = a[i],a[l]#Interchange a[i] and a[l]
            permute(a, l+1)     #Recursively call permute for smaller substring
            a[l],a[i] = a[i],a[l]#Interchange a[i] and a[l]
#Driver 
permute('abc')  
