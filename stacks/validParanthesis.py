class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            '{':'}',
            '[':']',
            "(":")",
        }
        for sy in s:
            if st and d.get(st[-1]) == sy:
                st.pop()
            else:
                st.append(sy)
                    
            

        return True if not st else False


