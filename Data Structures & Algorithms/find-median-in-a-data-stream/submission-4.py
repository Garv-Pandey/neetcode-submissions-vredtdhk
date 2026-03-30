class MedianFinder:

    def __init__(self):
        self.minheap = []
        heapq.heapify(self.minheap)
        self.maxheap = []
        heapq.heapify(self.maxheap)

    def addNum(self, num: int) -> None:

        if not self.minheap and not self.maxheap:
            print(f"first push in minheap: {num}")
            heapq.heappush(self.minheap, num)
            return
            
        if num < self.minheap[0]:
            heapq.heappush(self.maxheap, -num)
        
        else:
            heapq.heappush(self.minheap, num)

        
        while abs(len(self.minheap) - len(self.maxheap)) > 1:
            if len(self.minheap) > len(self.maxheap):
                heapq.heappush(self.maxheap, -1*heapq.heappop(self.minheap))
            else:
                heapq.heappush(self.minheap, -1* heapq.heappop(self.maxheap))

        print(self.maxheap, self.minheap)

    def findMedian(self) -> float:
        if (len(self.minheap) + len(self.maxheap)) % 2 == 0:
            return (self.minheap[0] + -1*self.maxheap[0])/2
        
        elif len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        
        else:
            return -self.maxheap[0]

        
        