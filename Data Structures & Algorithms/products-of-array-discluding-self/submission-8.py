class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ansewer = [1]*len(nums)

        product = 1 
        for i in range (len(nums)):
            ansewer[i] = product

            product *= nums[i]

        product = 1
        for j in range(len(nums)-1, -1, -1):
            ansewer[j] *= product

            product *= nums[j]

        return ansewer