class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        replace_pointer = 0

        for num in nums:
            if num == val:
                continue

            nums[replace_pointer] = num
            replace_pointer += 1

        return replace_pointer