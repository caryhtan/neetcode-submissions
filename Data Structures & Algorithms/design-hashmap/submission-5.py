class ListNode():
    def __init__(self, key = -1, value = -1, next = None):
        self.value = value
        self.key = key
        self.next = next

class MyHashMap:
    def __init__(self):
        self.myMap = [ListNode() for _ in range(1000)]
    
    def hash(self, key: int) -> int:
        return key % len(self.myMap)

    def put(self, key: int, value: int) -> None:
        cur = self.myMap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.value = value
                return
            cur = cur.next
        cur.next = ListNode(value = value, key = key)

    def get(self, key: int) -> int:
        cur = self.myMap[self.hash(key)].next
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.myMap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)