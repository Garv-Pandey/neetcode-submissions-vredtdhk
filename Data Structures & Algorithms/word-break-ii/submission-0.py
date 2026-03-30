class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        substrings = [] 

        def dfs(i):
            if i == len(s) and len(substrings)!=0:
                result.append(" ".join(substrings))
            
            for j in range(i, len(s)):
                if s[i:j+1] in wordDict:
                    substrings.append(s[i:j+1])
                    dfs(j+1)

                    substrings.pop()

        dfs(0)
        return result
