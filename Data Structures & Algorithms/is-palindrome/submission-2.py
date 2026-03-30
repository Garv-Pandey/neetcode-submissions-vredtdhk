class Solution:
    def isPalindrome(self, s: str) -> bool:
        l_point = 0
        r_point = len(s)-1

        while l_point <= r_point:
            if not s[l_point].isalnum() or s[l_point] == " ":
                l_point+=1
                continue

            if not s[r_point].isalnum() or s[r_point] == " ":
                r_point-=1
                continue

            if s[l_point].lower() == s[r_point].lower():
                l_point+=1
                r_point-=1
                continue

            return False

        return True
