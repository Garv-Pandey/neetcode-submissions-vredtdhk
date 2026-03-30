class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def maxSumValid(maxSum):
            subArray_count = 1
            empty = maxSum
            for num in nums:
                if num <= empty:
                   empty -= num
                   continue
               
                subArray_count += 1
                empty = maxSum-num

            return subArray_count<=k
        
        l = max(nums)
        r = sum(nums)
        maxSum = r

        while l <=r:
            mid = l + (r-l)//2
            print(l, r, mid, maxSumValid(mid))
            if maxSumValid(mid) == False:
                l = mid+1

            else:
                maxSum = min(maxSum, mid)
                r = mid-1

        return maxSum