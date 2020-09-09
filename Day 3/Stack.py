class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_stack(self) -> [int]:
        return self.stack

    def length(self) -> int:
        return len(self.stack)

    def is_empty(self) -> bool:
        return self.stack == [] 
