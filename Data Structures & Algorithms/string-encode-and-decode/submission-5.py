class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for i in strs:
            encoded = encoded + f'{len(i)}#{i}'  
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        prefix_len = 0
        while i < len(s):
            if s[i] != "#":
                i += 1
                prefix_len += 1
                continue

            len_word = int(s[i-prefix_len : i])
            word = s[i + 1 : i + 1 + len_word]
            result.append(word)
            i += 1 + len_word
            prefix_len = 0
            print (word)

        return result
        
