from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.data = deque([], maxlen=k)
        self.maxlen = k
        
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.data.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.data.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.data.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.data.pop()
        return True

    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.data[0]

    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def isFull(self) -> bool:
        if len(self.data) == self.maxlen: return True
        return False

"""
THE FOLLOWING CODE RUNS FASTER, THE COST FOR THE SPEED IS MAINTAINABILITY
"""

from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.data = deque([], maxlen=k)
        self.maxlen = k
        
    def insertFront(self, value: int) -> bool:
        if len(self.data) == self.maxlen: return False
        self.data.appendleft(value)
        return True

    def insertLast(self, value: int) -> bool:
        if len(self.data) == self.maxlen: return False
        self.data.append(value)
        return True

    def deleteFront(self) -> bool:
        if len(self.data) == 0: return False
        self.data.popleft()
        return True

    def deleteLast(self) -> bool:
        if len(self.data) == 0: return False
        self.data.pop()
        return True

    def getFront(self) -> int:
        if len(self.data) == 0: return -1
        return self.data[0]

    def getRear(self) -> int:
        if len(self.data) == 0: return -1
        return self.data[-1]

    def isEmpty(self) -> bool:
        return len(self.data) == 0

    def isFull(self) -> bool:
        if len(self.data) == self.maxlen: return True
        return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()