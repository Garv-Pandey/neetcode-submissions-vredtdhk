class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary_set = set(dictionary) 

        trie = {}
        for word in dictionary:
            level = trie
            for char in word:
                if char not in level:
                    level[char] = {}
                
                level = level[char]
            
            level['*'] = {}

        cache = {len(s): 0}

        def dfs(index):
            if index in cache:
                return cache[index]
            
            result = 1 + dfs(index + 1)

            level = trie
            for i in range(index, len(s)):
                if s[i] not in level:
                    break
                
                level = level[s[i]]

                if '*' in level:
                    result = min(result, dfs(i+1))
            
            cache[index] = result
            return result
        
        return dfs(0)





