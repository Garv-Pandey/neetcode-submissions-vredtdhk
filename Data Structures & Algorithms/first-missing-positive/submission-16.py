class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # converting negative numers to zero
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i]=0

        for j in range(len(nums)):
            if nums[j] == 0 or abs(nums[j]) > len(nums):
                continue

            elif nums[abs(nums[j])-1] == 0:
                nums[abs(nums[j])-1] = -(len(nums)+1)

            nums[abs(nums[j])-1] = - abs(nums[abs(nums[j])-1])

        print (nums)
        min_positive_exist = 0
        
        for k in range(len(nums)):
            if nums[k] >= 0:
                break

            elif nums[k]<0:
                min_positive_exist = k+1

        return min_positive_exist+1