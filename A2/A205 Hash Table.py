class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        hash_value = self.hash_function(key)
        self.table[hash_value].append((key, value))

    def find(self, key):
        hash_value = self.hash_function(key)
        for k, v in self.table[hash_value]:
            if k == key:
                return v
        return None

    def delete(self, key):
        hash_value = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[hash_value]):
            if k == key:
                del self.table[hash_value][i]
                return

hash_table = HashTable()
hash_table.insert('a', 1)
hash_table.insert('b', 2)
hash_table.insert('c', 3)

value = hash_table.find('b')
print(value)

hash_table.delete('b')
value = hash_table.find('b')
print(value)
