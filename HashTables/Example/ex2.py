class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]* size
    
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (existing_key, existing_value) in enumerate(self.table[index]):
                if existing_key == key:
                    self.table[index][i] =(key, value)
                    break
                else:
                    self.table[index].append((key, value))
    
    def get(self,key):
        index = self.hash_function(key)
        if self.table[index] is not None:
            for existing_key ==key:
                return existing_value
        raise KeyError(f"Key '{key}' not found")