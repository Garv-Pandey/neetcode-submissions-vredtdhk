class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count_s1 = [0]*26
        count_window = [0]*26

        for i in range (len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1
            count_window[ord(s2[i]) - ord('a')] += 1

        # print (count_s1)
        # print (count_window)

        matches = 0
        for i in range (26):
            if count_s1[i] == count_window[i]:
                matches += 1

        # print (matches)

        l = 0
        for r in range(len(s1)-1, len(s2)-1):
            # print(l, r)
            if matches == 26:
                return True

            r_match_index = ord(s2[r+1])-ord('a')
            count_window[r_match_index] += 1
            if count_window[r_match_index] == count_s1[r_match_index]:
                matches += 1

            elif count_window[r_match_index]-1 == count_s1[r_match_index]:
                matches -= 1

            l_match_index = ord(s2[l])-ord('a')
            count_window[l_match_index] -= 1
            if count_window[l_match_index] == count_s1[l_match_index]:
                matches += 1

            elif count_window[l_match_index] + 1 == count_s1[l_match_index]:
                matches -= 1

            l+=1


        return matches==26