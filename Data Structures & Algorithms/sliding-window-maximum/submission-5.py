class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        nums_downQue = collections.deque() #stores indices of decreasing values only
        answer = []
        # covering initial position of window
        l=0
        for r in range(len(nums)):
            # adding the element on right
            while len(nums_downQue)>0 and nums[nums_downQue[-1]] < nums[r]:
                nums_downQue.pop()

            nums_downQue.append(r)

            if r > k-1:
                l+=1
                while nums_downQue[0] < l:
                    nums_downQue.popleft()

            if r >= k-1:
                answer.append(nums[nums_downQue[0]])

        return answer