class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = dict()
        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        containers = [[] for i in range(len(nums) + 1)]
        for ele in hash_map.keys():
            containers[hash_map[ele]].append(ele)

        output = []
        index = len(containers) - 1
        while len(output) != k and index >= 0:
            output.extend(containers[index])
            index -= 1
        
        return output[:k]