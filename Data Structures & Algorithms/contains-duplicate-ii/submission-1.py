class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_index = dict()

        for i in range(len(nums)):
            if nums[i] not in num_index:
                num_index[nums[i]] = i
                continue

            if abs(num_index[nums[i]] - i) <= k:
                return True

            num_index[nums[i]] = i

        return False