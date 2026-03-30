class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_nums = defaultdict(int)

        for i in range (len (nums)):
            if target - nums[i] in map_nums:
                return [map_nums[target - nums[i]], i]

            map_nums[nums[i]]=i