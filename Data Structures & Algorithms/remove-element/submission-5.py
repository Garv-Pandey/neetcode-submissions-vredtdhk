class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_point = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue

            nums[replace_point] = nums[i]
            replace_point+=1

        return replace_point