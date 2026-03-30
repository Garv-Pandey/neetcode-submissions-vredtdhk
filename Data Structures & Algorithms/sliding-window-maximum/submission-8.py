class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if  k==1:
            return nums
        
        decreasing_q = collections.deque()
        answer = []
        l=0
        for r in range(len(nums)):
            if not decreasing_q:
                decreasing_q.append(nums[r])
                continue

            while decreasing_q and nums[r] > decreasing_q[-1]:
                decreasing_q.pop()

            decreasing_q.append(nums[r])

            if r-l+1> k:
                if decreasing_q[0] == nums[l]:
                    decreasing_q.popleft()

                l+=1

            if r-l+1 == k:
                answer.append(decreasing_q[0])

        return answer