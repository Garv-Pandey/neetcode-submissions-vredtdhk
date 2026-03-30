class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        skip_count = 1
        while l < r:
            if s[l] == s[r]:
                l+=1
                r-=1
                continue

            if skip_count>0 and s[l+1] == s[r]:
                l+=1
                skip_count-= 1
                continue

            elif skip_count>0 and s[l] == s[r-1]:
                r-=1
                skip_count-=1
                continue

            return False
        
        return True