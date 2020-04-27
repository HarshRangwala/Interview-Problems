class hashtable:
 
    def __init__(self, size_table = 4):
        self.hash_table = [None]*size_table
        print(self.hash_table)        
        
    def hash_function(self, key, size_table = None):
        size_table = len(self.hash_table) 
        return key % size_table
    
        
    def put(self, key, value):
        index = self.hash_function(key)
        if self.hash_table[index] is not None:
            for k in self.hash_table[index]:
                if k[0] == key:
                    k[1] = value
                    break
            else:
                self.hash_table[index].append([key, value])
        else:
            self.hash_table[index] = []
            self.hash_table[index].append([key, value])
        print(self.hash_table)
            
    def get(self, key):
        index = self.hash_function(key)
        if self.hash_table[index] is None:
            raise KeyError()
        else:
            for key_value_pairs in self.hash_table[index]:
                if key_value_pairs[0] == key:
                    return key_value_pairs[1]                

            raise KeyError()
    def remove(self, key):
        val = self.hash_function(key)
        if self.hash_table[val] != None:
            if type(self.hash_table[val]) == list:
                r = self.hash_table[val].index(key)
                self.hash_table[val][r] = None
            else:
                self.hash_table[val] = None
        else:
            KeyError()

        