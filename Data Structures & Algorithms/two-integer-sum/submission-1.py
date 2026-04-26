class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_hashmap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in result_hashmap.keys():
                return [result_hashmap.get(diff), index]
            else:
                result_hashmap[number] = index
        