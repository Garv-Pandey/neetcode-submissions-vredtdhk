class WordDictionary:

    def __init__(self):
        self.trie = dict()

    def addWord(self, word: str) -> None:
        level = self.trie

        for char in word:
            if char not in level:
                level[char] = {}
            
            level = level[char]
        
        level['*'] = {}
        

    def search(self, word: str) -> bool:
        def search_custom(level, index):
            if index == len(word):
                return '*' in level

            if word[index] == '.':
                for key_char in level.keys():
                    if search_custom(level[key_char], index+1):
                        return True
                    else: continue
                
                return False

            else:
                if word[index] not in level:
                    return False
                
                else:
                    return search_custom(level[word[index]], index+1)

            
        return search_custom(self.trie, 0)

            


        
