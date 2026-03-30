class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLen = len(nums)+1
        l = r = 0
        total = 0 
        for r in range(len(nums)):
            # print(l,r)
            total+=nums[r]

            while l<=r and total >= target:
                print(l,r, total)
                total-=nums[l]
                minLen = min(minLen, r-l+1)
                l+=1

        if minLen == len(nums)+1:
            return 0
        return minLen