class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTaken(k):
            hours = 0
            for p in piles:
                hours+= -(-p//k)

            return hours
        
        l = 1
        r = max(piles)
        result = max(piles)
        while l<=r:
            mid = l +(r-l)//2

            if hoursTaken(mid) > h:
                l = mid+1

            elif hoursTaken(mid) <=h:
                result = min(result, mid)
                r = mid-1

        return result