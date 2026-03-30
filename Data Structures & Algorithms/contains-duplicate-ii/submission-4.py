class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nums_visited = defaultdict(list)

        for i in range(len(nums)):
            if nums[i] not in nums_visited:
                nums_visited[nums[i]].append(i)
                continue
            
            for index in nums_visited[nums[i]]:
                if abs(index - i) <= k:
                    return True

            nums_visited[nums[i]].append(i)
        
        return False
