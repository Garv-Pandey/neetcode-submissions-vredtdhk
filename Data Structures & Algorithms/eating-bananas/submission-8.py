class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def timeTaken(eating_rate):
            time_taken = 0

            for pile in piles:
                if pile < eating_rate == 0:
                    time_taken += 1

                else:
                    time_taken += -(-pile // eating_rate)

            return time_taken

        l = 1
        ans = r = max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            print(mid, timeTaken(mid))

            if timeTaken(mid) <= h:
                ans = min(mid, ans)
                r = mid - 1

            else:
                l = mid + 1

        return ans
