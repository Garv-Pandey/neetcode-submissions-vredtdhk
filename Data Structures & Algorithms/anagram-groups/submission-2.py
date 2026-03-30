class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_strs = {}

        for word in strs:
            key = [0]*26
            for char in word:
                key[ord(char)-ord('a')]+=1

            key = tuple(key)
            value = map_strs.get(key, [])
            value.append(word)
            map_strs[key] = value

        return map_strs.values()