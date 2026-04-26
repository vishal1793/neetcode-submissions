class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        newMax = -1
        for i in range(len(arr)-1, -1, -1):
            ans[i] = newMax
            if arr[i] > newMax:
                newMax = arr[i]
    
        return ans