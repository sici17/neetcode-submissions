class Solution:
    def decodeString(self, s: str) -> str:

        stack=[]

        for char in s:
            if char != "]":
                stack.append(char)
            else:
                stringa=""
                while stack[-1] != "[":
                    stringa=stack.pop()+stringa
                stack.pop()
                intero=""
                while stack and  stack[-1].isdigit():
                    intero=stack.pop()+intero
                stack.append(int(intero)*stringa)
        
        return "".join(stack)





                    

        


                
                     
        