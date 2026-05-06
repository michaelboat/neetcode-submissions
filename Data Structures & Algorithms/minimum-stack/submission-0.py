class MinStack:

    def __init__(self):
        self.items = []
        

    def push(self, val: int) -> None:
        self.items.append(val)
        

    def pop(self) -> None:
        lth = len(self.items)
        self.items.pop(lth-1)
        

    def top(self) -> int:
        lth = len(self.items)
        return self.items[lth - 1]

        

    def getMin(self) -> int:
        return min(self.items)
        
