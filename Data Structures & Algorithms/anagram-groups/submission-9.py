class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = dict()

        for s in strs:
            key = [0]*26

            for char in s:
                key[ord(char) - ord('a')] += 1

            anagram[tuple(key)] = anagram.get(tuple(key), [])
            anagram[tuple(key)].append(s)

        print(anagram)

        return anagram.values()