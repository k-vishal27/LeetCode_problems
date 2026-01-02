from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        while left < len(nums) - 1:
            for i in range(left + 1, len(nums)):
                if nums[left] + nums[i] == target:
                    return [left, i]
            left += 1


s = Solution()
print(s.twoSum([1, 2, 3, 4, 5], 8))