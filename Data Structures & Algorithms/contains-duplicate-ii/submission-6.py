class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_visited = set() #stores only the elements withing window r-k+1 till r

        l=0
        for r in range(len(nums)):
            if nums[r] in nums_visited:
                return True
            
            nums_visited.add(nums[r])

            if l< r-k+1:
                nums_visited.remove(nums[l])
                l+=1

        return False
