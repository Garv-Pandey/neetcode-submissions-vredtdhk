class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1 :
            return 1
        
        l = 0
        r = x//2
        result = 0
        while l <= r:
            val = l + (r-l)//2
            if val*val > x:
                r = val-1

            elif val*val < x:
                result = max(result, val)
                l = val+1

            else:
                return val

        return result