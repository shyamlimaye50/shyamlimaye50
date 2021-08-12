from typing import List
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] ^ nums[j] > max:
                    max = nums[i] ^ nums[j]
        return max
#Driver
sol = Solution()
print(sol.findMaximumXOR([3,10,5,25,2,8]))