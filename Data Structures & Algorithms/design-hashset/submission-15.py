class MyHashSet:
    
    def __init__(self, lst = []):
        self.lst = {}

    def add(self, key: int) -> None:
        self.lst[key] = True

    def remove(self, key: int) -> None:
        self.lst.pop(key, None)

    def contains(self, key: int) -> bool:
        return True if key in self.lst else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)