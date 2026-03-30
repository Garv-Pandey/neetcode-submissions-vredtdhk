class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_index = 0

        for i in range (len(nums)):
            if nums[i] == val:
                continue 

            nums[replace_index] = nums[i]
            replace_index+=1

        return replace_index

            