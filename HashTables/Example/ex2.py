class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None]* size
    
    def hash_function(self, key):
        return hash(key) % self.size