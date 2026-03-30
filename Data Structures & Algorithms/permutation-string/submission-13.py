class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        
        s_pattern = [0]*26
        for s in s1:
            s_pattern[ord(s) - ord('a')] += 1

        window_pattern = [0]*26
        for i in range(len(s1)):
            window_pattern[ord(s2[i])-ord('a')] += 1

        match_count = 0
        for j in range(26):
            if s_pattern[j] == window_pattern[j]:
                match_count+=1

        l = 0
        for r in range(len(s1), len(s2)):
            if match_count == 26:
                return True
            
            add_char_index = ord(s2[r]) - ord('a')
            remove_char_index = ord(s2[l]) - ord('a')
            
            window_pattern[add_char_index]+=1
            if window_pattern[add_char_index] == s_pattern[add_char_index]:
                match_count+=1
            elif window_pattern[add_char_index] -1 == s_pattern[add_char_index]:
                match_count-=1
            
            window_pattern[remove_char_index]-=1
            if window_pattern[remove_char_index] == s_pattern[remove_char_index]:
                match_count+=1
            elif window_pattern[remove_char_index] +1 == s_pattern[remove_char_index]:
                match_count-=1

            l+=1

        return match_count == 26