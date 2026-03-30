class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index = defaultdict(int)

        for i in range(len(nums)):
            if nums_index and target-nums[i] in nums_index:
                return [nums_index[target-nums[i]], i]

            nums_index[nums[i]] = i

            