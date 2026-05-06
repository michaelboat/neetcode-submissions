class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def execute(ls:list, op:str) -> None:
            if op == '+':
                curr = int(ls.pop())
                curr = int(ls.pop()) + curr
                ls.append(curr)

            elif op == '-':
                curr = int(ls.pop())
                curr = int(ls.pop()) - curr
                ls.append(curr)

            elif op == '*':
                curr = int(ls.pop())
                curr = int(ls.pop()) * curr
                ls.append(curr)
            
            elif op == '/':
                curr = int(ls.pop())
                curr = int(ls.pop()) / curr
                ls.append(curr)

    
        ls = []
        ops = ['+', '-', '*', '/']

        for item in tokens:
            if item not in ops:
                ls.append(item)
            else:
                execute(ls, item)
                

        return int(ls[0])

        

                
                
                


        