class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str


        well my brain is cooking something.

        so we gotta go from right to left.

        then move and append stuff in a temp string until we find a slash!
        if last char was a / remove it.

        - go on until you find the next /
        
        store in tmp:
            if tmp:
                - . then remove / & .
                - .. then remove .. & / & one dir before next //
        
        """
        curr=''
        stack = []
        
        for c in path + "/":
            if c == '/':
                if curr == '..':
                    if stack: stack.pop()
                    
                elif curr and curr != ".":
                    stack.append(curr)
                
                curr=''
            else:
                curr+=c
        
        return "/" + "/".join(stack)
        
