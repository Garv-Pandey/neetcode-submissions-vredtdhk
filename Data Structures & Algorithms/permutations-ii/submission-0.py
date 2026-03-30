class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_map = {}
        for n in nums:
            if n not in nums_map:
                nums_map[n] = 0
            
            nums_map[n]+=1
        
        result = []
        perm = []
        def dfs():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            
            for n in nums_map.keys():
                if nums_map[n] > 0:
                    perm.append(n)
                    nums_map[n] -= 1

                    dfs()

                    nums_map[n] += 1
                    perm.pop()
        
        dfs()
        return result

