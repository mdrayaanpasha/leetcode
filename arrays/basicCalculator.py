class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        n=len(s)
        curr_num = 0
        sign=1
        res=0


        for i in range(n):
            char = s[i]

            if char == ' ':
                continue
            if char.isdigit():
                curr_num=curr_num*10+int(char)
            
            if char == '+' or char == '-' or i == n-1:
                res+=sign*curr_num
                curr_num=0
                sign= 1 if char == '+' else -1
            
            if char == '(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1

            if char == ')':
                res+=sign*curr_num
                curr_num=0
                res*=stack.pop()
                res+=stack.pop()

            

        return res + (sign * curr_num)
