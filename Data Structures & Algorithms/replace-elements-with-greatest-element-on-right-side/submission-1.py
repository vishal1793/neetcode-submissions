class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        greatest = 0
        for i in range(0,len(arr)):
            greatest = 0
            if i == len(arr)-1:
                break
            for j in range(i+1, len(arr)):
                if arr[j] > greatest:
                    greatest = arr[j]
                    
            ans.append(greatest)

        ans.append(-1)
    
        return ans