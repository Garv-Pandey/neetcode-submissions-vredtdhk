class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # finding the index of peak
        peak_index = None
        l = 0 
        r = mountainArr.length() - 1

        while l<=r:
            mid = l + (r-l)//2
            cur = mountainArr.get(mid)
            next = mountainArr.get(mid+1)
            prev = mountainArr.get(mid-1)

            if prev < cur and cur > next:
                peak_index = mid
                break

            elif prev < cur:
                l = mid+1

            else: 
                r = mid-1

        
        # finding in ascent
        l = 0
        r = peak_index
        
        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid) == target:
                return mid
            
            elif mountainArr.get(mid) < target:
                l = mid+1

            else:
                r = mid-1

        # finding in descent
        l = peak_index
        r = mountainArr.length() -1

        while l<=r:
            mid = l + (r-l)//2

            if mountainArr.get(mid) == target:
                return mid
            
            elif mountainArr.get(mid) < target:
                r = mid-1

            else:
                l = mid + 1

        return -1