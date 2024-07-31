from collections import deque

class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()


    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                last = self.stack1.pop()
                self.stack2.append(last)
        if self.stack2:
            return self.stack2.pop()
        return None
    

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                last = self.stack1.pop()
                self.stack2.append(last)
        if self.stack2:
            return self.stack2[-1]
        return None

    def empty(self) -> bool:
        if not self.stack1 and not self.stack2:
            return True
        else:
            return False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
