class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        replace_point = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                continue

            nums[replace_point] = nums[i]
            replace_point+=1
            

        return replace_point