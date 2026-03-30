class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_index = defaultdict(int)

        for i in range(len(numbers)):
            if target - numbers[i] in num_index:
                return [num_index[target - numbers[i]] + 1, i + 1]

            num_index[numbers[i]] = i

        return []