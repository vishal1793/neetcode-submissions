class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        start = 0
        end = len(heights) - 1
        while start < end:
            area = (end - start) * min(heights[start], heights[end])
            if area > result:
                result = area
            
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1
        
        return result

        