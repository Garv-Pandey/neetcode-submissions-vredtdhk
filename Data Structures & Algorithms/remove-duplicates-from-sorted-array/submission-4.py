class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace_point = 0

        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue

            nums[replace_point] = nums[i]
            replace_point+=1

        return replace_point