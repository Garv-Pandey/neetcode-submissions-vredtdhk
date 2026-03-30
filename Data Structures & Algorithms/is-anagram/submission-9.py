class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for char in s:
            dict_s[char] += 1

        for char in t:
            dict_t[char] += 1

        return dict_s == dict_t