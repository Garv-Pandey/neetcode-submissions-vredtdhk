class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def isValid(max_sum):
            subarray_count = 1
            cur_sum = 0

            for num in nums:
                cur_sum += num

                if cur_sum <= max_sum:
                    continue
                
                subarray_count += 1
                cur_sum = num

        
            return subarray_count<=k
        
        l = max(nums)
        r = sum(nums)
        answer = None
        while l<=r:
            mid = l + (r-l)//2

            if isValid(mid):
                answer = mid
                r = mid-1

            else:
                l = mid+1

        return answer