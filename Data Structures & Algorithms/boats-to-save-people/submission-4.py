class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        buckets = [0] * (m+1)
        for p in people:
            buckets[p] += 1

        people_point, bucket_point = 0, 1
        while people_point < len(people):
            while buckets[bucket_point] == 0:
                bucket_point += 1
            people[people_point] = bucket_point
            buckets[bucket_point] -= 1
            people_point += 1


        boat_count = 0 
        l, r = 0, len(people) - 1
        while l <= r:
            # loading the heaviest person left
            remain_weight = limit - people[r]
            r -= 1

            # checking if we have a person light enough to send in the boat
            if l <= r and remain_weight >= people[l]:
                l += 1
            
            # sending the boat
            boat_count += 1
        return boat_count