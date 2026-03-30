class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTook(eatingRate):
            time = 0
            for p in piles:
                time += -(-p//eatingRate)

            return time
        
        l = 1
        r = max(piles) 
        answer = r
        while l <= r:
            mid = l + (r-l)//2

            if timeTook(mid) > h:
                l = mid+1

            else:
                answer = min(answer, mid)
                r = mid-1

        return answer