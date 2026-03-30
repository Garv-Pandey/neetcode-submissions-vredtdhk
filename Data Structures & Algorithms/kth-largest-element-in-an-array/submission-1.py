class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = [num*-1 for num in nums]
        heapq.heapify(minheap)
        print(minheap)

        result = None
        for _ in range(k):
            result = heapq.heappop(minheap)
        
        return -1 * result
