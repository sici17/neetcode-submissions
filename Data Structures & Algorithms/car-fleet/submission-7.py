class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        data= zip(position, speed)
        data=list(data)
        data.sort(reverse=True)
        stack=[]
        count=1

        for posizione, velocità in data:
            left=(target-posizione)/velocità
            if stack and left<=stack[0]:
                stack.append(left)
            elif stack:
                while stack:
                    stack.pop()
                count+=1
                stack.append(left)
            else:
                stack.append(left)
        
        return count
                










        






        






            
            



            

        