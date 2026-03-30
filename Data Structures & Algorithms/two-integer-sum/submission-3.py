class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map
        map_nums = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in map_nums:
                return [map_nums[target-nums[i]][0], i]

            indices = map_nums.get(nums[i], [])
            indices.append(i)
            map_nums[nums[i]] = indices