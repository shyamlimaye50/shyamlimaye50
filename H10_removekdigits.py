class Solution:
    def removeKdigits(self, num, k):
        result = []
        #Scan the digits (d) from left to right
        for d in num:
            #remove all elements from stack that are > d
            while k and result and result[-1] > d:
                result.pop()
                k -= 1
            result.append(d)
            #return ''.join(result).lstrip('0')[:-k or None] or '0'
        if k != 0: result = result[:-k] #Remove right k digits
        ss = ''.join(result).lstrip('0')
        return ''.join(result).lstrip('0') or '0'
#Driver code
sol=Solution()
#num = "1432219"; k = 3 #Ans 1219
#num = "10200"; k = 1  #Ans 200
#num = "123"; k = 1  #Ans 12
#num = "9";k=1 #ans "0"
#num = "112";k=1 #ans "11"
num = "4321";k=2
print(sol.removeKdigits(num,k))