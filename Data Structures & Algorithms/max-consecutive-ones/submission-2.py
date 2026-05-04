class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        reset = False
        count = 0
        count_arr = []
        i = 0
        while i < len(nums):
            if nums[i] == 1 and reset == False:
                count += 1
                reset = False
                i += 1
            elif nums[i] == 1 and reset == True:
                count = 1
                reset = False
                i += 1
            else:
                reset = True
                count_arr.append(count)
                i += 1
        
        count_arr.append(count)

        return max(count_arr)
        