class Solution:
    def romanToInt(self, s: str) -> int:
        """
        two cases, the char encounter now is greater then next then we 
        we can procceed, else we have to subtract.
        """
        roman_dict = {
            'I':1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        num=0

        for i in range(len(s)):
            #case 1:
            if i+1 < len(s) and roman_dict[s[i+1]] > roman_dict[s[i]]:
                num-=roman_dict[s[i]]
            else:
                num+=roman_dict[s[i]]

        return num
