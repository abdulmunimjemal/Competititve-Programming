class MyLinkedList:

    def __init__(self):
        self.items = []
        
    def get(self, index: int) -> int:
        if index > len(self.items)-1: return -1
        return self.items[index]

    def addAtHead(self, val: int) -> None:
        self.items.insert(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.items.append(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > len(self.items): return
        if index == len(self.items): 
            self.items.append(val)
        else:
            self.items.insert(index, val)

        

    def deleteAtIndex(self, index: int) -> None:
        if index > len(self.items)-1: return
        self.items.pop(index)
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)