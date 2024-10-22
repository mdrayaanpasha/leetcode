class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        Str1Arr=list(str1)
        Str2Arr=list(str2)
        lenStr1=len(str1)
        lenStr2=len(str2)

        largest = 1 if lenStr1 > lenStr2 else 2

        combinations=[]

        if largest == 1:
            for i in range(lenStr2):
                combinations.append("".join(Str2Arr[0:i+1]))
        else:
            for i in range(lenStr1):
                combinations.append("".join(Str1Arr[0:i+1]))
        Possible_Combinations=[]
        for i in range(len(combinations)):
            if largest == 1 and len("".join(str1.split("".join(combinations[i])))) == 0:
                Possible_Combinations.append("".join(combinations[i]))
            elif largest == 2 and len("".join(str2.split("".join(combinations[i])))) == 0:
                Possible_Combinations.append("".join(combinations[i]))
        Max=0  
        E=''
        for elem in Possible_Combinations:
            if(len(elem) > Max):
                E=elem
                Max=len(elem)
                
                
        return E

        
