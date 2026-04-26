class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        result = []
        for ind, num in enumerate(nums):
            if ind > 0:
                result.append(result[ind - 1]*prefix)
            else:
                result.append(prefix)
            
            prefix = num
                
        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] = suffix * result[index]
            suffix = nums[index] * suffix

                
        return result
