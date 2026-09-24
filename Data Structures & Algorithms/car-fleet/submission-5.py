class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [(p, s) for p, s in zip(position, speed)]
        stack=[]
        pair.sort(reverse=True)
        count=1

        for p,s in pair:
            val=(target-p)/s
            if stack and val>stack[-1]:
                count+=1
                stack.append(val)
            elif stack:
                stack.append(stack[-1])
            else:
                stack.append(val)
        
        return count
            






        






            
            



            

        