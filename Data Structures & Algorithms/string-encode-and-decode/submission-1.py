class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_list = list()

        for word in strs:
            encoded_list.extend([str(len(word)), "#", word])

        return "".join(encoded_list)


    def decode(self, s: str) -> List[str]:
        decoded_list = list()
        index = 0
        while index < len(s):
            deli_start = index
            deli_end = deli_start
            while s[deli_end] != "#":
                deli_end += 1

            deli_len = deli_end - deli_start + 1
            word_len = int(s[deli_start:deli_end])
            decoded_list.append(s[index + deli_len : index + deli_len + word_len])

            index = index + deli_len + word_len

        return decoded_list