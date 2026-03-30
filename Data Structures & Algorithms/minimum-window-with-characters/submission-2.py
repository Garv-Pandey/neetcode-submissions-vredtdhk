class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)> len(s):
            return ""

        t_char_freq = defaultdict(int)
        for char in t:
            t_char_freq[char]+=1

        window_char_freq = defaultdict(int)

        result_index = [-1,-1]
        result_len = float('inf')
        require_score = 0
        l=0
        for r in range(len(s)):
            window_char_freq[s[r]] += 1

            print(s[l:r+1])
            print(window_char_freq)

            if  s[r] in t_char_freq and window_char_freq[s[r]] == t_char_freq[s[r]]:
                require_score += 1

            print(require_score)

            # shrinking window until validity becomes false
            while require_score == len(t_char_freq):
                
                # updating result if smaller window
                if r-l+1 < result_len:
                    result_len = r-l+1
                    result_index = [l, r]

                # shrinking size and updating freq, require_score
                window_char_freq[s[l]] -= 1
                if s[l] in t_char_freq and window_char_freq[s[l]] + 1 == t_char_freq[s[l]]:
                    require_score -= 1
                l+=1

        return s[result_index[0] : result_index[1]+1]

                

            
