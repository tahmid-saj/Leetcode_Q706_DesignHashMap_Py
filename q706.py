class Bucket:

    def __init__(self):
        self.bucket = []

    def get(self, key):
        for (k, v) in self.bucket:
            if k == key: return v
        return -1

    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        
        if found == False: self.bucket.append((key, value))

    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]: del self.bucket[i]

class MyHashMap:

    def __init__(self):
        self.key_space = 2069
        self.hash_map = [Bucket() for _ in range(self.key_space)]

    def put(self, key: int, value: int) -> None:
        k = key % self.key_space
        self.hash_map[k].update(key, value)

    def get(self, key: int) -> int:
        k = key % self.key_space
        return self.hash_map[k].get(key)

    def remove(self, key: int) -> None:
        k = key % self.key_space
        self.hash_map[k].remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
