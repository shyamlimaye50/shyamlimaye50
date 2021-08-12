'''
#Strategy 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        counts = [0 for i in range(26)]
        for i in range(len(s)):
            counts[ord(s[i])-ord('a')] +=1
            counts[ord(t[i])-ord('a')] -=1
        for c in counts:
            if c !=0:return False
        return True
'''
#Strategy 2
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)       

#Driver
sol = Solution()
print(sol.isAnagram("anagram","nagaram"))
