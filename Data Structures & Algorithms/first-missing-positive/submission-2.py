class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        # converting negative integers to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # for a positive number, converting the element on index with that number as negative
        for j in range(len(nums)):
            if nums[j] == 0 or abs(nums[j]) > len(nums):
                continue

            if nums[abs(nums[j])-1] == 0:
                nums[abs(nums[j])-1] = - (len(nums)+1)
                continue

            nums[abs(nums[j])-1] = -abs(nums[abs(nums[j])-1])

        print(nums)

        # finding the smallest positive integer
        
        for k in range(len(nums)):
            if nums[k] >= 0:
                return k+1

        return (len(nums)+1)