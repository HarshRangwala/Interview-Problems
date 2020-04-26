from collections import defaultdict
class Trie:
    def __init__(self):
        self.nodes = defaultdict()
        self.is_leaf = False
    def multiinsert(self, words = []):
        for word in words:
            self.nodes.insert(word)
    def insert(self, word = str):
        current = self.nodes
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")
        #print(current)
        #current.is_leaf = True
    def search(self, word = str):
        current = self.nodes
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        if "_end" in current:
            return True
        return False
    def prefixSearch(self, prefix):
        current = self.nodes
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True
                
test = Trie()
test.insert('helloworld')
test.insert('foobar')
test.insert('choco')

print( test.search('helloworld'))
print( test.prefixSearch('ch'))
print( test.search('ilikeapple'))


            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    