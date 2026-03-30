class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = defaultdict(int)
        for char in s:
            dict_s[char] += 1

        dict_t = defaultdict(int)
        for char in t:
            dict_t[char] += 1

        return dict_s == dict_t