class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks_custom = []
        for i, task in enumerate(tasks):
            tasks_custom.append([*task, i])
        
        tasks_custom = sorted(tasks_custom, key= lambda x: x[0])

        time = 0
        minheap_queue = []
        heapq.heapify(minheap_queue) #(execution_time, [time_start, execution_time, pos_index])
        tasks_index = 0
        result = []
        while tasks_index < len(tasks) or minheap_queue:
            while tasks_index < len(tasks) and time > tasks_custom[tasks_index][0]:
                heapq.heappush(minheap_queue, (tasks_custom[tasks_index][1], tasks_custom[tasks_index]))
                tasks_index += 1
            
            if minheap_queue:
                exec_time, task = heapq.heappop(minheap_queue)
                result.append(task[2])
                time += exec_time
            
            else:
                time+=1
        
        return result

            

