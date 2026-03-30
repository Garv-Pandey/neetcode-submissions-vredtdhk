class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = []

        for i in range (len(strs)):
            encode = f"{len(strs[i])}#{strs[i]}"
            encoded.append(encode)

        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            str_len = 0
            len_str_len = 0

            while s[i] != '#':
                len_str_len +=1
                i+=1

            str_len = int(s[i - len_str_len : i])
            result.append(s[i+1 : i+1+str_len])
            i+= 1 + str_len

        return result


