class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dict_strs = defaultdict(list)

        for word in strs:
            key = [0]*26

            for char in word:
                key[ord(char)- ord('a')] +=1

            dict_strs[tuple(key)].append(word)

        return list(dict_strs.values())
