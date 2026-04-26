class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set(nums)
        return True if len(nums) != len(result) else False
        