class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def daysTook(capacity):
            days = 1
            capacity_left = capacity
            weight_point = 0
            while weight_point < len(weights):
                if capacity_left >= weights[weight_point]:
                    capacity_left -= weights[weight_point]
                    weight_point+=1
                    continue

                days += 1
                capacity_left = capacity

            print(capacity, days)
            return days
        

        l = max(weights)
        r = sum(weights)
        result = r
        while l <=r:
            mid = l + (r-l)//2

            if daysTook(mid) > days:
                l = mid+1

            else:
                result = min(result, mid)
                r = mid-1

        return result