class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        potential_result = 0
        while l<=r:
            mid  = l + (r-l)//2

            if mid**2 > x:
                r = mid-1

            elif mid**2 < x:
                l = mid+1
                potential_result = mid

            else:
                return mid
            
        return potential_result