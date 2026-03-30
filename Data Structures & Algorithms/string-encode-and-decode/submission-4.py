class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            part = f'{len(word)}#{word}'
            encoded = encoded + part
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        len_word_len = 0
        while i < len (s):
            
            if s[i] != "#":
                i+=1
                len_word_len +=1
                continue

            word_len = int(s[i-len_word_len:i])
            print (word_len)
            word = s[i+1: i+1+word_len]
            words.append(word)
            i += 1+word_len
            len_word_len = 0
            
        return words


