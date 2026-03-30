class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l_point = 0
        r_point = len(s) - 1

        while l_point < r_point:
            if not s[l_point].isalnum():
                # print(f"l_point at index {l_point} is not alpha: {s[l_point]}")
                l_point += 1
                continue

            if not s[r_point].isalnum():
                # print(f"r_point at index {r_point} is not alpha: {s[r_point]}")
                r_point -= 1
                continue

            if s[l_point] != s[r_point]:
                # print(
                #     f"unequal at lpoint: {l_point}, r_point: {r_point}. Values {s[l_point]}, {s[r_point]}"
                # )
                return False

            l_point += 1
            r_point -= 1

        return True
