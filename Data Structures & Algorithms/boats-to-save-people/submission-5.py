class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        buckets = [0] * (limit+1)
        for p in people:
            buckets[p]+=1
        print(buckets)

        people_point = 0
        for bucket_point in range(len(buckets)):
            if people_point == len(people):
                break

            while buckets[bucket_point] > 0:
                people[people_point] = bucket_point
                people_point += 1
                buckets[bucket_point] -= 1

        l = 0
        r = len(people)-1
        boat_count = 0
        while l<=r:
            boat_count+=1
            limit_left = limit - people[r]
            r-=1

            if limit_left >= people[l]:
                l+=1
            
        return boat_count
