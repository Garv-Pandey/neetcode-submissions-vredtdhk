class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone*-1 for stone in stones]
        
        minheap = stones
        heapq.heapify(minheap)

        while len(minheap)>1:
            a = heapq.heappop(minheap)
            b = heapq.heappop(minheap)

            result = abs(abs(a) - abs(b))

            heapq.heappush(minheap, -result)
        
        return abs(minheap[0]) if minheap else 0


