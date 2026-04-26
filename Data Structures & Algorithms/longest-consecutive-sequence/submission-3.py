class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = []
        start = 0
        hash_set = set(nums)

        if len(nums) == 0:
            return 0
        for num in nums:
            if num - 1 not in hash_set:
                start = num
                length = 1
                while start + 1 in hash_set:
                    length += 1
                    start += 1
                
                max_length.append(length)
        print(max_length)
        return max(max_length)
        