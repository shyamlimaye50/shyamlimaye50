'''The program will recieve 3 English words inputs 
from STDIN. These three words will be read one at 
a time, in three separate line 
The first word should be changed like 
    all vowels should be replaced by %
The second word should be changed like 
    all consonants should be replaced by #
The third word should be changed like 
    all char should be converted to upper case
Then concatenate the three words and print them
'''
a= input("First word:")
b= input("Second word:")
c= input("Third word:")

al = list(a)
for i in range(len(al)):
    if al[i] in 'aeiou':al[i]='%'
a = "".join(al)

bl = list(b)
for i in range(len(bl)):
    if bl[i] not in 'aeiou':bl[i]='#'
b = "".join(bl)
c = c.upper()
print(a+b+c)  

'''
First word:shyamkant

Second word:shridhar

Third word:limaye
shy%mk%nt###i##a#LIMAYE
'''  