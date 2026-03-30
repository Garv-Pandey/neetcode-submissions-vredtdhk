class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSum_freq = dict()

        answer = 0
        total = 0
        for i in range(len(nums)):
            total += nums[i]

            if total == k:
                answer+=1
            
            if total - k in preSum_freq:
                answer += preSum_freq[total-k]

            preSum_freq[total] = 1 + preSum_freq.get(total, 0)

        return answer
