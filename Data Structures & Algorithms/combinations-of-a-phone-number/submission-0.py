class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0 or digits is None:
            return []
            
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        subset = []
        def dfs(i):
            if i>=len(digits):
                result.append("".join(subset))
                return
            

            for char in digitToChar[digits[i]]:
                subset.append(char)
                dfs(i+1)
                subset.pop()

        dfs(0)
        return result
            
