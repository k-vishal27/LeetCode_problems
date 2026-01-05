from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for i in range(len(nums))]
         
        pre, post = 1, 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
         
        return res

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))