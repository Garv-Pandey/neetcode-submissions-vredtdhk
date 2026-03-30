class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends_set = set(deadends)
        visited = set()
        q = deque()

        def children_values(value):
            if value in deadends_set or value in visited:
                return
            
            visited.add(value)

            for i in range(4):
                digit_inc = str((int(value[i]) + 1) % 10)
                q.append(value[:i] + digit_inc + value[i+1:])

                digit_dec = str((int(value[i]) - 1 + 10) % 10)
                q.append(value[:i] + digit_dec+ value[i+1:])



        q.append("0000")
        move = 0 
        while q:
            for i in range(len(q)):
                value = q.popleft()
                if value == target:
                    return move

                children_values(value)
            
            move+=1
        
        return -1

