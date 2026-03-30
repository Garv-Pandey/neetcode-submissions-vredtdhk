class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        char_map = dict()
        l,r,maxfreq = 0,0,0
        for r in range(len(s)):
            char_map[s[r]] = 1 + char_map.get(s[r], 0)
            maxfreq = max (maxfreq, char_map[s[r]])

            while not (r-l+1) - maxfreq <= k:
                char_map[s[l]] -= 1
                maxfreq = max (maxfreq, char_map[s[l]])
                l+=1

            result = max (result, r-l+1)

        return result