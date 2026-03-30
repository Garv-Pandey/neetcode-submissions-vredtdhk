class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = Counter(tasks)
        queue = collections.deque()

        maxheap = tasks_count
        maxheap = [-task_count for task_count in tasks_count.values()]
        heapq.heapify(maxheap)

        time = 0
        while len(maxheap)!=0 or len(queue) != 0:
            if len(queue) > 0 and queue[0][1] < time:
                task = queue.popleft() 
                heapq.heappush(maxheap, task[0])

            if len(maxheap)> 0:
                task_count = abs(heapq.heappop(maxheap))
                task_count -= 1
                if task_count > 0:
                    queue.append((-task_count, time + n))

            time += 1
        
        return time

