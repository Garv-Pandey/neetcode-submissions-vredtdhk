class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        s1_char_freq = defaultdict(int)
        for char in s1:
            s1_char_freq[char]+=1
        
        window_char_freq = defaultdict(int)
        for i in range (len(s1)):
            window_char_freq[s2[i]] += 1

        present = True
        for char, freq in s1_char_freq.items():
            if char in window_char_freq and window_char_freq[char] == freq:
                continue

            present = False
            break
        
        if present == True:
            return True

        l = 0
        for r in range (len(s1), len(s2)):
            window_char_freq[s2[r]] += 1
            window_char_freq[s2[l]] -= 1
            l+=1
            
            present = True
            for char, freq in s1_char_freq.items():
                if char in window_char_freq and window_char_freq[char] == freq:
                    continue

                present = False
                break
            
            if present == True:
                return True
        
        # print(window_char_freq)
        # print(s1_char_freq)
        return False