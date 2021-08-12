#Rotate an array in-place by k places
from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
         k %= len(nums)
         nums[k:], nums[:k] = nums[:-k], nums[-k:]
#Driver code
sol = Solution()
nums = [i for i in range(10)]
sol.rotate(nums,2)
print(nums)


