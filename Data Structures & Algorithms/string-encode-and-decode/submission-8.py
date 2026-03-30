class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += f'{len(word)}#{word}'

        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            len_word_len = 0
            while s[i]!='#':
                len_word_len+=1
                i+=1

            word_len = int(s[i-len_word_len:i])
            word = s[i+1: i+1+word_len]
            result.append(word)
            i+=word_len+1

        return result
