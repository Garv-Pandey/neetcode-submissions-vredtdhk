class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysTook(capacity):
            days = 1
            cap_left = capacity
            for w in weights:
                if cap_left >= w:
                    cap_left -= w
                    continue

                days += 1
                cap_left = capacity - w

            return days
        
        l = max(weights)
        r = sum(weights)
        answer = r
        while l <= r:
            mid = l + (r - l)//2

            if daysTook(mid) > days:
                l = mid+1

            else:
                answer = min(answer, mid)
                r = mid-1

        return answer