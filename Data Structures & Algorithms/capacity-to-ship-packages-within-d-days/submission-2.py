class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def isValidCapacity(w):
            days_calc = 1
            capacity = w
            for weight in weights:
                if capacity < weight:
                    days_calc += 1
                    capacity = w - weight

                else:
                    capacity -= weight

            print (w, days_calc)

            return days_calc<=days
        
        l = max(weights)
        r = sum(weights)
        answer = None
        while l<=r:
            mid = l + (r-l)//2

            if isValidCapacity(mid):
                answer = mid
                r = mid-1

            else:
                l = mid+1

        return answer