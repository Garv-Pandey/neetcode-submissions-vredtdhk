class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefSum_count = dict()

        answer = 0
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            if total == k:
                print(l,r, "total == k")
                answer += 1

            if (total - k) in prefSum_count:
                print (l,r, "prefSum")
                answer += prefSum_count[total-k]

            prefSum_count[total] = 1 + prefSum_count.get(total, 0)

        return answer 