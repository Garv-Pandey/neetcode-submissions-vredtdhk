class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        skips_left = 1
        l=0
        r=len(s)-1

        while l<r:
            if s[l] == s[r]:
                l+=1
                r-=1
                continue

            if skips_left>0:
                if s[l+1] == s[r]:
                    l+=1
                elif s[l] == s[r-1]:
                    r-=1
                else :
                    return False
                skips_left-=1
                continue

            return False

        return True