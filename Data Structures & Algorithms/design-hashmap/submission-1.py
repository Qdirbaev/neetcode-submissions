class MyHashMap:

    def __init__(self):
        self.arr = []

    def put(self, key: int, value: int) -> None:
        found = False
        for elem in range(len(self.arr)):
            if self.arr[elem][0] == key:
                self.arr[elem][1] = value
                found = True
                break
        if not found: 
            self.arr.append([key, value])

    def get(self, key: int) -> int:
        for elem in range(len(self.arr)):
            if self.arr[elem][0] == key:
                return self.arr[elem][1]
        return -1

    def remove(self, key: int) -> None:
        for elem in range(len(self.arr)):
            if self.arr[elem][0] == key:
                del self.arr[elem]
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)