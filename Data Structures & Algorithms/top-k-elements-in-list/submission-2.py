class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        frequency = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        
        for key,value in hashmap.items():
            frequency[value].append(key)
        
        result = []
        for freq in range(len(frequency) - 1, 0, -1):
            for num in frequency[freq]:
                result.append(num)

                if len(result) == k:
                    return result
        
        return []