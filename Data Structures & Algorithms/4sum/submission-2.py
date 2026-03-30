class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            answer = []

            for h in range(len(nums)-3):
                if h>0 and nums[h-1] == nums[h]:
                    continue
                for i in range(h+1, len(nums)-2):
                    if i>h+1 and nums[i-1] == nums[i]:
                        continue
                    
                    j = i+1
                    k = len(nums)-1
                    while j<k:
                        if j>i+1 and nums[j] == nums[j-1]:
                            j+=1
                            continue

                        if nums[h] + nums[i] + nums[j] + nums[k] == target:
                            answer.append([nums[h] , nums[i] , nums[j] , nums[k]])
                            j+=1
                            k-=1
                        
                        elif nums[h] + nums[i] + nums[j] + nums[k] < target:
                            j+=1

                        elif nums[h] + nums[i] + nums[j] + nums[k] > target:
                            k-=1
            
            return answer