class Solution:
    def reorganizeString(self, s: str) -> str:
        count_map = Counter(s)

        maxheap = [[-count, char] for char, count in count_map.items()]

        heapq.heapify(maxheap)

        reserve_var = None
        result = ""
        while maxheap or reserve_var:
            if not maxheap and reserve_var:
                return ""
            
            count, char = heapq.heappop(maxheap)
            result += char
            count += 1

            if reserve_var:
                heapq.heappush(maxheap,reserve_var)
                reserve_var = None
            
            if count < 0:
                reserve_var = [count, char]
        
        return result
