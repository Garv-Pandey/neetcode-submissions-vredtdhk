class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs ={}
        for s in strs:
            char_pattern = [0]*26
            for c in s:
                char_pattern[ord(c) - ord('a')] += 1
            
            key = tuple(char_pattern)
            value = map_strs.get(key, [])
            value.append(s)
            map_strs[key] = value
        
        return list(map_strs.values())

