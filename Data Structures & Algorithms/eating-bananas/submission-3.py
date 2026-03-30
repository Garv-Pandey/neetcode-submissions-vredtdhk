class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hoursTook(k):
            hours = 0
            for pile in piles:
                hours += -(-pile//k)

            return hours


        answer = max(piles)
        l, r = 1, max(piles)

        while l<=r:
            mid = l+ (r-l)//2

            hours_took = hoursTook(mid)
            if hours_took > h:
                l = mid + 1
            else:
                answer = mid  # Found a valid k, but look for smaller
                r = mid - 1

        return answer