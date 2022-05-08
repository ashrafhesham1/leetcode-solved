from collections import deque

class MyStack:

    class Queue :
        def __init__(self):
            self.queue = deque()
        def enqueue(self,val):
            self.queue.append(val)
        def dequeue(self):
            return self.queue.popleft()
        def top(self):
            return self.queue[0] if self.queue else None
        def isEmpty(self):
            return len(self.queue) == 0

    def __init__(self):
        self.queue = self.Queue()

    def push(self, x: int) -> None:
        self.queue.enqueue(x)

    def pop(self) -> int:
        temp = self.Queue()
        while True :
            top = self.queue.dequeue()
            if self.queue.isEmpty():
                self.queue = temp
                return top
            temp.enqueue(top)

    def top(self) -> int:
        temp = self.Queue()
        while True:
            top = self.queue.dequeue()
            temp.enqueue(top)
            if self.queue.isEmpty():
                self.queue = temp
                return top
            
    def empty(self) -> bool:
        return self.queue.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()