class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key= lambda x: x[1])
        
        index = 0
        # distance = trips[0][1]
        # passangers = trips[0][0]
        distance = 0
        passengers = 0

        minheap = []
        heapq.heapify(minheap) # (drop_dist, [passenger_count, pickup_dist, drop_dist])

        while index < len(trips):
            pickup_dist = trips[index][1]
            drop_dist = float("+inf")

            if minheap:
                drop_dist = minheap[0][0]
            
            distance = min(pickup_dist, drop_dist)
            print(f"distnace {distance}")

            if drop_dist <= distance:
                _, drop_tour = heapq.heappop(minheap)
                print(f"{drop_tour[0]} passengers dropped")
                passengers -= drop_tour[0] 
            
            if pickup_dist <= distance:
                passengers += trips[index][0]
                print(f"{trips[index][0]} passengers picked")
                if passengers > capacity:
                    return False
                
                heapq.heappush(minheap, (trips[index][2], trips[index]))
                index += 1

        return True
