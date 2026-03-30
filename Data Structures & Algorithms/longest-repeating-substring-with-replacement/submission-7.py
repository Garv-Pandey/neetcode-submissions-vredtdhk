class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_len = 0
        char_freq =dict()
        maxChar =0

        l = r= 0
        for r in range(len(s)):
            char_freq[s[r]] = 1+char_freq.get(s[r], 0)

            maxChar = max(maxChar, char_freq[s[r]])

            while r-l+1 - maxChar > k:
                char_freq[s[l]] -= 1
                l+=1

            window_len = max(window_len, r-l+1)

        return window_len