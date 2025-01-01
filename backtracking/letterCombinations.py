class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []

        ans,sol = [],[]
        dig_map = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }

        """
        + WHATS THE PLAN PHIEEL!@#!@

        - first create a hashmap to store in a key val thing.
        - then do backtrackin: draw that freakin tree...

        """
        n=len(digits)
        def backtracking(i):
            if i == n:
                ans.append("".join(sol))
                return 


            for letter in dig_map[digits[i]]:
                sol.append(letter)
                backtracking(i+1)
                sol.pop()


        backtracking(0)
        return ans

            
