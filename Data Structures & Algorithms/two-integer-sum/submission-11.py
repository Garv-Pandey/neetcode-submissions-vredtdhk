class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map_seen = {}
        for i in range (len(nums)):
            if target - nums[i] in map_seen:
                return [map_seen[target - nums[i]][0], i]

            value = map_seen.get(nums[i], [])
            value.append(i)
            map_seen[nums[i]]= value