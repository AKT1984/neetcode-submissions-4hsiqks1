class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.stack = []

    def push(self, val: int) -> None:
        # if stack empty
        if not self.stack:
            self.min = val
            self.stack.append(0)
        else:
            diff = val - self.min
            if diff < 0:
                self.min = val
            self.stack.append(diff)


    def pop(self) -> None:
        diff = self.stack.pop()
        if diff < 0:
            self.min -= diff

    def top(self) -> int:
        diff = self.stack[-1]
        if diff > 0:
            return diff + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min
        
