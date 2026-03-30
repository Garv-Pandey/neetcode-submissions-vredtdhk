class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l<r:
            if (not s[l].isalnum()) or s[l] == " ":
                l+=1
                continue

            if not (s[r].isalnum()) or s[l] == " ":
                r-=1
                continue

            if s[l].lower() != s[r].lower():
                print(s[l])
                print(s[r])
                return False

            l+=1
            r-=1

        return True