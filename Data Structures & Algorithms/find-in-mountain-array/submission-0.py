class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # finding the peak 
        l = 0
        r = mountainArr.length()-1
        peak = None
        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid-1) < mountainArr.get(mid) > mountainArr.get(mid+1):
                peak = mid
                break

            elif mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid + 1

            else:
                r = mid - 1

        
        # finding solution in ascent
        l = 0
        r = peak

        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid) > target:
                r = mid -1

            elif mountainArr.get(mid) < target:
                l = mid +1

            else: 
                return mid
            
        # finding solution in descent
        l = peak
        r = mountainArr.length()-1

        while l<=r:
            mid = l +(r-l)//2

            if mountainArr.get(mid) > target:
                l = mid + 1

            elif mountainArr.get(mid) < target:
                r = mid -1

            else:
                return mid
        
        return -1