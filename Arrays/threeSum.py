from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            left = a + 1
            right = len(nums) - 1
            target = -nums[a]
            
            while left < right:
                curr_sum = nums[left] + nums[right]
                
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.append([nums[a], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                    
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))