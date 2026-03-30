class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        buckets = [0]*(limit+1)

        for p in people:
            buckets[p] += 1

        peiple_point = 0
        for i in range(len(buckets)):
            for _ in range(buckets[i]):
                people[peiple_point] = i
                peiple_point += 1

        l=0
        r=len(people)-1
        boat_count = 0
        while l<=r:
            r-=1
            boat_count+=1

            if people[l] <= limit - people[r+1]:
                l+=1

            continue

        return boat_count