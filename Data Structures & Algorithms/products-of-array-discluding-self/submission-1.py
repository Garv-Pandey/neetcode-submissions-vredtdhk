class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_r_pass = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                l_r_pass[i] = nums[i]
                continue
            
            l_r_pass[i] = l_r_pass[i-1]*nums[i]
        print(l_r_pass)
        
        r_l_pass = [0]*len(nums)
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums)-1:
                r_l_pass[j] = nums[j]
                continue
            
            r_l_pass[j] = r_l_pass[j+1]*nums[j]
        print(r_l_pass)
        
        result = []
        for k in range(len(nums)):
            ans = 1
            if k==0:
                ans = r_l_pass[k+1]
            elif k==len(nums)-1:
                ans = l_r_pass[k-1]
            else:
                ans = l_r_pass[k-1]*r_l_pass[k+1]

            result.append(ans)

        return result