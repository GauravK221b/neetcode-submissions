class MinStack:

    def __init__(self):
        self.res = []

    def push(self, val: int) -> None:
        self.res.append(val)

    def pop(self) -> None:
        self.res.pop()

    def top(self) -> int:
        return self.res[-1]

    def getMin(self) -> int:
        return min(self.res)
        
