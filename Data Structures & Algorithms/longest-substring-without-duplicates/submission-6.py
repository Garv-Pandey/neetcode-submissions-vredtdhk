class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_char = set()

        l = r = 0
        window_len = 0
        for r in range(len(s)):
            if s[r] not in window_char:
                window_char.add(s[r])
                window_len = max(window_len, r-l+1)
                continue

            while s[r] in window_char:
                window_char.remove(s[l])
                l+=1

            window_char.add(s[r])
            window_len = max(window_len, r-l+1)

        return window_len