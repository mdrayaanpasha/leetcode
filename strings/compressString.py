class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        Word=chars[0]
        lenght=0
        Words=[]
        
        for i in range(len(chars)):
            if chars[i] == Word:
                lenght+=1
            else:
                Words.append(Word)
                if lenght > 1:
                    if lenght >= 10:
                        l=list(str(lenght))
                        Words.extend(l)
                        
                    else:
                        Words.append(str(lenght))
                
                Word=chars[i]
                lenght=1
                
        Words.append(Word)
        if lenght > 1:
            if lenght >= 10:
                l=list(str(lenght))
               
                Words.extend(l)
            else:
                Words.append(str(lenght))
            
        
        for i in range(len(chars)):
            
            if i < len(Words):
                chars[i]=Words[i]
            else:
                chars.pop()
        
        return len(Words)