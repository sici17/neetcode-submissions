class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for i in range(len(tokens)):

            if tokens[i] not in {"+", "-", "*", "/"}:
                stack.append(int(tokens[i]))
            else:
                match tokens[i]:
                    case "+":
                        a=stack.pop()
                        stack.append(stack.pop()+a)
                    case "-":
                        a=stack.pop()
                        stack.append(stack.pop()-a)
                    case "*":
                        stack.append(stack.pop()*stack.pop())
                    case "/":
                        a=stack.pop()
                        stack.append(int(stack.pop()/a))
            
        return stack[0]



                

        