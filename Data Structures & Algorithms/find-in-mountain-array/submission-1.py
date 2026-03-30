class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # finding the peak
        peak_index = None
        l = 0
        r = mountainArr.length()
        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid) < mountainArr.get(mid+1):
                l = mid+1
                
            elif mountainArr.get(mid-1) > mountainArr.get(mid):
                r = mid-1

            else:
                peak_index = mid
                break

        # searching in ascent
        l = 0
        r = peak_index
        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid) > target:
                r = mid-1

            elif mountainArr.get(mid) < target:
                l = mid+1

            else:
                return mid
        
        # searching in descent
        l = peak_index
        r = mountainArr.length()
        while l<=r:
            mid = l + (r-l)//2
            if mountainArr.get(mid) > target:
                l = mid+1

            elif mountainArr.get(mid) < target:
                r = mid-1

            else:
                return mid
            
        # if target index isnt found
        return -1