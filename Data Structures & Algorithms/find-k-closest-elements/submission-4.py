class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # finding the closest number
        closest_index = 0

        for i in range(len(arr)):
            if abs(arr[i] - x) < abs(arr[closest_index] - x):
                closest_index = i

        # finding k closest 
        l = closest_index
        r = closest_index
        while r-l+1 != k:
            if l==0:
                r+=1
            
            elif r==len(arr)-1:
                l-=1

            elif abs(arr[l-1] - x) <= abs(arr[r+1] - x):
                l-=1

            else:
                r+=1

        return arr[l:r+1]