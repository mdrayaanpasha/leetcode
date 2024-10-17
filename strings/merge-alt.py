class Solution(object):
    def mergeAlternately(self, word1, word2):
        word3=[]
        counter1=0
        counter2=0


        while counter2 < len(word2) or counter1 < len(word1):
            
            if counter1 < len(word1):
                word3.append(word1[counter1])
                counter1+=1
            if counter2 < len(word2):
                word3.append(word2[counter2])
                counter2+=1

        outp="".join(word3)
        return outp
        