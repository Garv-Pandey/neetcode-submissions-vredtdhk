class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = defaultdict(list)

        for i in range(len(nums)):
            if target - nums[i] in dict_nums:
                return [dict_nums[target - nums[i]][0], i]

            dict_nums[nums[i]].append(i)