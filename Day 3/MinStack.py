class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min:
            if x < self.min[-1] and x != self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)

    def pop(self) -> None:
        self.stack.pop()
        if self.min[-1] not in self.stack:
            self.min.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.min and self.stack:
            return self.min[-1]
        


obj = MinStack()
obj.push(5)
obj.push(4)
obj.pop()
obj.push(1)
print("Top: ",obj.top())
obj.push(7)
print("Top: ",obj.top())
obj.pop()
print("Top: ",obj.top())
obj.pop()
print("MIN: ",obj.getMin())