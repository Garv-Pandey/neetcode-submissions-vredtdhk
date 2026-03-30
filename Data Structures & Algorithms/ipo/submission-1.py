class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minheap = [] # (captial, profit)
        maxheap = [] # (-profit, capital)

        for i in range(len(profits)):
            minheap.append((capital[i], profits[i]))
        
        heapq.heapify(maxheap)
        heapq.heapify(minheap)


        while k:
            print(k)
            while minheap and w >= minheap[0][0]:
                # print(minheap[0])
                capital , profit = heapq.heappop(minheap)
                heapq.heappush(maxheap, (-profit, capital))
            
            if not maxheap:
                return w
                
            profit, capital = heapq.heappop(maxheap)
            profit = -profit

            w += profit
            k -= 1
        
        return w