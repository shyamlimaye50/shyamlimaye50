class Solution:
    def trailingZeroes(self, n: int) -> int:
    # Initialize result
        '''
        count = 0
        # Keep dividing n by 5 & update Count
        
        while(n >= 5):
            n //= 5
            count += n
        return count
        '''
        return n//5+n//25+n//625+n//125+n//3125
#Driver
sol = Solution()
print(sol.trailingZeroes(50))#ans 12
print(sol.trailingZeroes(987816469))#ans 246954111
        