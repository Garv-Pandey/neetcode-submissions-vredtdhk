class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s = s+f'{len(word)}#{word}'

        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        prefix_len = 0
        while i < len(s):
            if s[i]!="#":
                i+=1
                prefix_len+=1
                continue

            word_len = int(s[i-prefix_len: i])
            word = s[i+1 : i+1+word_len]
            result.append(word)
            prefix_len = 0
            i += word_len + 1

        return result
