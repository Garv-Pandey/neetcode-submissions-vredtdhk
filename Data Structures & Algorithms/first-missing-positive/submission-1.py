class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if nums[i]<0:
                nums[i]=0
        
        for j in range (len(nums)):
            if abs(nums[j]) > len(nums) or nums[j]==0:
                continue

            if nums[abs(nums[j]) - 1] == 0 :
                nums[abs(nums[j]) - 1] = -(len(nums)+1)
                continue

            nums[abs(nums[j]) -1 ] = - abs(nums[abs(nums[j]) -1 ]) 

        print (nums)
        answer = len(nums)+1
        for k in range (len(nums)):
            if nums[k] >= 0:
                answer = min (k+1, answer)

        return answer
            