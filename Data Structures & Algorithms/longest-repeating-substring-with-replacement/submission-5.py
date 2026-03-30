class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        answer = 0
        char_freq = defaultdict(int)

        l=0
        highest_freq = 0
        highest_freq_char = None
        for r in range(len(s)):
            char_freq[s[r]] += 1

            if char_freq[s[r]] > highest_freq:
                highest_freq = char_freq[s[r]]
                highest_freq_char = s[r]


            while (r-l+1) - highest_freq > k:
                char_freq[s[l]]-=1
                l+=1

            answer = max(answer, r-l+1)

        return answer
