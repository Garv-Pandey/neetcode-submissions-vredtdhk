class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for string in strs:
            key = [0]*26
            for char in string:
                key[ord(char) - ord('a')] += 1

            anagram_dict[tuple(key)].append(string)
        
        # print(anagram_dict.values())

        return anagram_dict.values()

