class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            minheap.append([dist, point[0], point[1]])
        print(minheap)

        heapq.heapify(minheap)

        result = []
        for _ in range(k):
            val = heapq.heappop(minheap)
            result.append([val[1], val[2]])
        
        return result