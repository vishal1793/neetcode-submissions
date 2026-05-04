class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        count_arr = []
        i = 0
        while i < len(nums):
            if nums[i] == 1:
                count += 1
                i += 1
            else:
                count_arr.append(count)
                i += 1
                count = 0
        
        count_arr.append(count)

        return max(count_arr)
        