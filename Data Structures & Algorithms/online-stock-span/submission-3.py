class StockSpanner:

    def __init__(self):

        self.stack=[]
        self.ret={}
        self.i=0

        

    def next(self, price: int) -> int:

        c=1

        while self.stack and price>=self.stack[-1]:
            c+=self.ret[self.stack[-1]]
            print(self.i)
            print(c)
            self.stack.pop()
        
        self.stack.append(price)
        self.ret[price]=c
        self.i+=1
        return c
            
            


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)