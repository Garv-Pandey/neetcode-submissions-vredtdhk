class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isRateValid(k):
            hours = 0

            for pile in piles:
                if pile<=k:
                    hours += 1

                else:
                    time = -(-pile//k)
                    hours += time

            print (hours)
            return hours <= h
        
        l = 1
        r = max(piles)
        answer = None
        while l<=r:
            mid = l + (r-l)//2

            print (mid, isRateValid(mid))
            if isRateValid(mid):
                answer = mid
                r = mid-1

            else:
                l = mid+1

        return answer