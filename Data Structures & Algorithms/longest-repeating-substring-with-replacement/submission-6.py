class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_len = 0
        char_freq = dict()
        maxChar_freq = 0 #keeps track of highest freq of a character ever occured in window
        l = r = 0
        for r in range(len(s)):
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1

            maxChar_freq = max(maxChar_freq, char_freq[s[r]])

            while r-l+1 - maxChar_freq > k:
                char_freq[s[l]] -= 1
                l+= 1

            window_len = max(window_len, r-l+1)

        return window_len