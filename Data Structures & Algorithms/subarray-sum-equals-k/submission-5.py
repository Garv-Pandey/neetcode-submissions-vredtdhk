class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum_count = defaultdict(int)
        
        answer = 0
        total = 0
        for i in range (len(nums)):
            total += nums[i]

            if total == k:
                answer += 1

            if total - k in preSum_count:
                answer += preSum_count[total-k]

            preSum_count[total] += 1

        return answer