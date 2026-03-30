class PrefixTree:

    def __init__(self):
        self.trie = dict()
        

    def insert(self, word: str) -> None:
        level = self.trie
        for char in word:
            if char not in level:
                level[char] = {}

            level = level[char]
        
        level['*'] = {}

        print(self.trie)
            
        

    def search(self, word: str) -> bool:
        level = self.trie

        for char in word:
            if char not in level:
                return False
            
            level = level[char]
        
        return '*' in level

    def startsWith(self, prefix: str) -> bool:
        level = self.trie

        for char in prefix:
            if char not in level:
                return False
            
            level = level[char]
        
        return True
        
        
        