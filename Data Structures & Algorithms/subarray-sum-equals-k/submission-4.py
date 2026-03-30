class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum_found = defaultdict(int)

        answer = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            
            if total == k:
                answer += 1

            if (total - k) in presum_found:
                answer += presum_found[total-k]

            presum_found[total] += 1
            # print(r, presum_found)

        return answer