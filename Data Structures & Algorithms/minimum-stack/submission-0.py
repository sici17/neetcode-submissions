class MinStack:

    def __init__(self):
        self.stack=[]
        self.minimi=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minimi[-1] if self.minimi else val)
        self.minimi.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimi.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimi[-1]
        
