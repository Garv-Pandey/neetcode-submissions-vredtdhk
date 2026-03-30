class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)

        # forward pass, inserting prefix
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix = nums[i] * prefix

        # backward pass, multplying suffix with prefix
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * suffix
            suffix = suffix * nums[i]

        return output