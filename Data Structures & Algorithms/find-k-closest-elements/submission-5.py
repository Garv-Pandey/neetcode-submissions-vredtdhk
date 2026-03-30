class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # finding the closes element's index
        closestIndex = 0
        for i in range(len(arr)):
            if abs(arr[i] - x) < abs(arr[closestIndex] -x):
                closestIndex = i

        r=l=closestIndex
        while r-l+1 != k:
            if r==len(arr)-1:
                l-=1
            
            elif l==0:
                r+=1

            elif abs(arr[l-1]-x) <= abs(arr[r+1]-x):
                l-=1
            
            else:
                r+=1

        return arr[l: r+1]