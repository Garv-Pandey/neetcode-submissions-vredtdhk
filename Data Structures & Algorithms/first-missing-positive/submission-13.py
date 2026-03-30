class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # converting negative number to 0
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        
        # making element on the index == number negative
        for j in range(len(nums)):
            if nums[j]==0 or abs(nums[j])>len(nums):
                continue

            print(nums[j])
            if nums[abs(nums[j])-1] == 0:
                nums[abs(nums[j])-1] = - (len(nums)+1)
                continue

            nums[abs(nums[j])-1] = - abs(nums[abs(nums[j])-1])

        print(nums)
        # finding smallest positive number
        k_count=0
        for k in range(len(nums)):
            if nums[k]<0:
                k_count+=1
                continue

            break

        return k_count+1