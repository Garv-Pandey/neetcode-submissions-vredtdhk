class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)

        prod = 1 
        for i in range (0, len(nums)):
            ans[i] = prod

            prod = prod * nums[i]

        print (ans)

        prod = 1
        for j in range (len(nums)-1 ,-1, -1):
            ans[j] = ans[j]*prod
            prod = prod*nums[j]
        
        return ans