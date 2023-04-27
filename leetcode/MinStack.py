class MinStack:

    def __init__(self):
        self.__arr = []
        self.min = []

    def push(self, val: int) -> None:
        if self.min == [] or self.min[-1] >= val:
            self.min.append(val)
        self.__arr.append(val)

    def pop(self) -> None:
        x = self.__arr.pop()
        if x == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.__arr[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()