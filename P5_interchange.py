# Interchange two variable without using temp
a=15
b=27
a = a^b
b = a^b  #b=a^b^b = a
a = a^b  #a=a^b^a = b
print('a=',a,'b=',b)


