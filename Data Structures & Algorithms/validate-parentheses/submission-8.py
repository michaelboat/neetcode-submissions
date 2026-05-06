class Solution:
    def isValid(self, s: str) -> bool:

        str_len = len(s)
        if str_len % 2 != 0 or str_len <= 1:
            return False
        
        open_bracks = ['[', '(', '{']
        close_bracks = [']', ')', '}']

        stk = []
        for i in range(len(s)):
            #print(i)
            if s[i] in open_bracks:
                #print(i)
                stk.append(s[i])
            elif s[i] in close_bracks and len(stk) != 0:
                print(i)
                if s[i] == '}' and stk[-1] == '{':
                    stk.pop()
                elif s[i] == ')' and stk[-1] == '(':
                    stk.pop()
                elif s[i] == ']' and stk[-1] == '[':
                    stk.pop()
                else:
                    return False
            else:
                return False
        
        return (not bool(stk))
        
        