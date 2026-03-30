class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = {}
        for i in range(len(nums)):
            if target-nums[i] in map_nums:
                return [ map_nums[target-nums[i]][0], i]

            value = map_nums.get(nums[i], [])
            value.append(i)
            map_nums[nums[i]] = value
        