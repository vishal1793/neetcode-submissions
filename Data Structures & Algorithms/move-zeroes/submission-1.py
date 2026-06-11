class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, 1
        while end < len(nums):
            if nums[start] == 0 and nums[end] == 0:
                end += 1
            elif nums[start] == 0 and nums[end] !=0:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
            else:
                start += 1
                end += 1