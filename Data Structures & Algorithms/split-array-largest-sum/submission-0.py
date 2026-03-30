class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def subarrayCount(limit):
            count = 1
            total = 0
            for num in nums:
                if total + num > limit:
                    count += 1
                    total = num
                else:
                    total += num
            return count

        l, r = max(nums), sum(nums)
        answer = r

        while l <= r:
            mid = l + (r - l) // 2
            if subarrayCount(mid) <= k:
                answer = mid
                r = mid - 1
            else:
                l = mid + 1

        return answer
