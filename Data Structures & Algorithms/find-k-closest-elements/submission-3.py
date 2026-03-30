class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        closest_index = None
        difference = float('inf')

        for i in range(len(arr)):
            if abs(arr[i] - x) < difference:
                difference = abs(arr[i] - x)
                closest_index = i 

        l = closest_index
        r = closest_index

        while r-l+1 != k:
            # 
            closest_smaller = None
            closest_larger = None
            if l>0:
                closest_smaller = arr[l-1]
            if r<len(arr)-1:
                closest_larger = arr[r+1]

            # if either r or l is at boundry
            if closest_smaller == None:
                r+=1
                continue
            elif closest_larger == None:
                l-=1
                continue

            # if both r and l are not at boundry
            if abs(closest_smaller - x) <= abs(closest_larger - x):
                l-=1
            elif abs(closest_smaller - x) > abs(closest_larger - x):
                r+=1
            
        return arr[l : r+1]


