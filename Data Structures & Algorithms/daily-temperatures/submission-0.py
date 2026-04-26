class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] #[val, ind]

        for ind, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                result[stackInd] = ind - stackInd
            stack.append([temp, ind])
        
        return result