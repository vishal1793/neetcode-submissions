class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, i in enumerate(nums):
            if index > 0 and i == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                total = i + nums[left] + nums[right]
                if total == 0:
                    result.append([i, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
