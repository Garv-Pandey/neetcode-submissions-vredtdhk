class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {} #char_pattern: [anagrams]

        for word in strs:
            char_pattern= [0]*26

            for char in word:
                char_pattern[ord(char)-ord('a')]+=1

            
            anagrams = hash_map.get(tuple(char_pattern), [])
            anagrams.append(word)
            hash_map[tuple(char_pattern)] = anagrams

        return hash_map.values()