class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() #indices
        l = 0

        for r in range(len(nums)):
            while len(q)!=0 and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # incrementing the index and removing it from queue, if it exist
            if l > q[0]:
                q.popleft()

            if (r+1) >= k:
                output.append(nums[q[0]])
                l+=1

        return output