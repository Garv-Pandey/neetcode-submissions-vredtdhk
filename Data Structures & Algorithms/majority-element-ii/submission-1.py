class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [] #the ans cannot have more than 2 numbers. 
        # as we need to find the numbers which occur more than third. which only is possible by maximum of 2 numbers.
        
        nums_map = defaultdict(int)

        for i in range (len(nums)):
            nums_map[nums[i]] += 1

            # reducing the dict when more than 2 elements
            keys_to_delete = []
            if len(nums_map) >=3:
                for key, value in nums_map.items():
                    if value - 1 == 0:
                        keys_to_delete.append(key)
                    else:
                        nums_map[key] -= 1

            for key in keys_to_delete:
                del nums_map[key]

        # checking the correctness of number left in dict
        for num in nums_map.keys():
            count = 0
            for i in range(len(nums)):
                if nums[i]==num:
                    count+=1

            if count > len(nums)//3:
                ans.append(num)

        return ans

            
