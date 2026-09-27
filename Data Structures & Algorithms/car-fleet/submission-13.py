class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        dati = list(zip(position,speed))
        dati.sort(reverse=True)
        stack=[]

        for position,speed in dati:
            time=(target-position)/speed
            stack.append(time)
            while len(stack)>1 and stack[-1]<=stack[-2]:
                stack.pop()

        return len(stack) 


        
                










        






        






            
            



            

        