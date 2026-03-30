class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        length = float('inf')

        l = 0
        r = 0

        for r in range(len(nums)):
            total += nums[r]

            if total < target:
                continue

            while l<=r and total>=target:

                if r-l+1 < length:
                    length = r-l+1

                total -= nums[l]
                l+=1

        if length == float('inf'):
            return 0

        return length